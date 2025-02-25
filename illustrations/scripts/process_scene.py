from PIL import Image, ImageEnhance, ImageFilter
import os
from pathlib import Path
import json
import re

def load_metadata():
    """Charger les métadonnées des scènes"""
    metadata_path = Path("/Users/sylvainbonal/Documents/Cline/memory-bank/livre/illustrations/metadata/index.json")
    with open(metadata_path) as f:
        return json.load(f)

def enhance_colors(img, colors):
    """Améliorer les couleurs selon les spécifications"""
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(1.2)  # Renforcer légèrement les couleurs
    
    # Luminosité pour les effets d'aube/crépuscule
    brightness = ImageEnhance.Brightness(img)
    img = brightness.enhance(1.1)
    
    return img

def apply_atmospheric_effects(img, scene_type):
    """Appliquer les effets atmosphériques"""
    if "foret_aube" in scene_type:
        # Effet de brume matinale
        blur = img.filter(ImageFilter.GaussianBlur(radius=1))
        return Image.blend(img, blur, 0.3)
    return img

def process_scene(input_path, output_path, scene_metadata):
    """Traiter une scène avec ses paramètres spécifiques"""
    print(f"\nTraitement de la scène : {input_path}")
    
    with Image.open(input_path) as img:
        print(f"Image source : {img.size}x{img.mode}")
        
        # Appliquer les transformations de base
        print("Application des transformations...")
        
        # Amélioration de la netteté
        img = img.filter(ImageFilter.SHARPEN)
        
        # Contraste
        contrast = ImageEnhance.Contrast(img)
        img = contrast.enhance(1.15)
        
        # Effets spécifiques à la scène
        scene_type = scene_metadata.get("name", "").lower().replace(" ", "_")
        img = apply_atmospheric_effects(img, scene_type)
        
        # Couleurs selon le style guide
        if "styleGuide" in scene_metadata and "colors" in scene_metadata["styleGuide"]:
            img = enhance_colors(img, scene_metadata["styleGuide"]["colors"])
        
        # Vérifier/ajuster la résolution pour l'impression
        required_dpi = 300
        if img.info.get("dpi", (72, 72))[0] < required_dpi:
            print(f"Ajustement de la résolution à {required_dpi} DPI")
            w, h = img.size
            scale = required_dpi / 72  # Supposant une résolution de base de 72 DPI
            new_size = (int(w * scale), int(h * scale))
            img = img.resize(new_size, Image.Resampling.LANCZOS)
        
        # Créer le dossier de sortie si nécessaire
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Sauvegarder en haute qualité
        img.save(output_path, "PNG", quality=95, dpi=(300, 300))
        print(f"Image traitée sauvegardée : {output_path}")

def extract_scene_name(filename):
    """Extraire le nom de la scène du nom de fichier"""
    # Pattern pour matcher le nom de la scène dans le nom de fichier
    pattern = r"scene_chapitre1_([^_]+_[^_]+)_"  # Modifié pour capturer le nom complet
    match = re.search(pattern, filename)
    if match:
        scene_name = match.group(1)
        # Convertir en format attendu par les métadonnées
        scene_key = f"chapitre1_{scene_name}"
        print(f"Nom de scène extrait : {scene_key}")
        return scene_key
    return None

def process_chapter_scenes(raw_dir, processed_dir):
    """Traiter toutes les scènes du chapitre"""
    print("\nTraitement des scènes du chapitre 1...")
    
    # Charger les métadonnées
    metadata = load_metadata()
    scenes_metadata = metadata.get("collections", {}).get("scenes", {})
    
    # Créer le dossier de sortie
    os.makedirs(processed_dir, exist_ok=True)
    
    # Liste des scènes traitées
    processed_scenes = set()
    
    # Traiter chaque scène finale
    input_dir = Path(raw_dir)
    for input_file in input_dir.glob("scene_chapitre1_*_final_*.png"):
        scene_key = extract_scene_name(input_file.name)
        
        if scene_key and scene_key not in processed_scenes:
            if scene_key in scenes_metadata:
                processed_scenes.add(scene_key)
                
                # Générer le nom du fichier de sortie
                scene_name = scene_key.split("_", 1)[1]  # Retirer "chapitre1_"
                output_name = f"scene_{scene_name}_processed.png"
                output_path = Path(processed_dir) / output_name
                
                # Traiter la scène
                process_scene(str(input_file), str(output_path), scenes_metadata[scene_key])
                print(f"Scène traitée : {scene_key}")
            else:
                print(f"Métadonnées non trouvées pour la scène : {scene_key}")

if __name__ == "__main__":
    # Chemins des dossiers
    raw_dir = "/Users/sylvainbonal/Documents/Cline/memory-bank/livre/illustrations/raw/scenes"
    processed_dir = "/Users/sylvainbonal/Documents/Cline/memory-bank/livre/illustrations/processed/scenes"
    
    # Lancer le traitement
    process_chapter_scenes(raw_dir, processed_dir)