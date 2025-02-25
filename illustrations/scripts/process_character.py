from PIL import Image, ImageEnhance, ImageFilter
import os
from pathlib import Path
import colorsys

def hex_to_rgb(hex_color):
    """Convertir une couleur hexadécimale en RGB."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def process_character(input_path, color_palette, output_path):
    """Traiter un personnage avec une palette de couleurs spécifique."""
    print(f"Traitement du personnage : {input_path}")
    
    # Couleurs de la palette
    main_color = hex_to_rgb(color_palette['principal'])
    secondary_color = hex_to_rgb(color_palette['secondaire'])
    detail_color = hex_to_rgb(color_palette['details'])
    
    # Ouvrir l'image
    with Image.open(input_path) as img:
        # Informations sur l'image source
        print(f"Image source : {img.size}x{img.mode}")
        
        # Harmonisation des couleurs
        print("Harmonisation des couleurs...")
        img = img.convert('RGB')  # Assurer le mode RGB
        
        # Ajuster les tons
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(1.2)  # Augmenter légèrement la saturation
        
        # Renforcer le contraste
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.1)
        
        # Ajouter de la netteté
        img = img.filter(ImageFilter.SHARPEN)
        
        # Texture douce
        img = img.filter(ImageFilter.SMOOTH)
        
        # Créer le dossier de destination si nécessaire
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Sauvegarder l'image
        img.save(output_path, "PNG", quality=95)
        print(f"Image sauvegardée : {output_path}")
        
        # Vérification finale
        with Image.open(output_path) as final:
            print(f"Image finale : {final.size}x{final.mode}")

if __name__ == "__main__":
    # Configuration pour Écureuil Gris
    ecureuil_config = {
        'principal': '#808080',    # Gris moyen
        'secondaire': '#A9A9A9',   # Gris clair
        'details': '#696969'       # Gris foncé
    }
    
    # Chemins des fichiers
    input_path = "/Users/sylvainbonal/Documents/Cline/memory-bank/livre/illustrations/working/personnages/ecureuil_gris_working.png"
    output_path = "/Users/sylvainbonal/Documents/Cline/memory-bank/livre/illustrations/processed/personnages/ecureuil_gris_processed.png"
    
    # Traitement
    process_character(input_path, ecureuil_config, output_path)