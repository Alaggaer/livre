from PIL import Image, ImageEnhance, ImageFilter
import os
from pathlib import Path

def process_image(input_path, output_path):
    print(f"\nTraitement de l'image : {input_path}")
    
    # Ouvrir l'image
    with Image.open(input_path) as img:
        # Informations sur l'image source
        print(f"Image source : {img.size}x{img.mode}")
        
        # Appliquer les transformations
        print("Application des transformations...")
        
        # Luminosité et contraste
        enhancer = ImageEnhance.Brightness(img)
        img = enhancer.enhance(1.1)  # Légère augmentation
        
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(1.2)  # Plus de contraste
        
        # Netteté
        img = img.filter(ImageFilter.SHARPEN)
        
        # Redimensionnement si nécessaire
        max_size = (512, 512)
        if img.size[0] > max_size[0] or img.size[1] > max_size[1]:
            print("Redimensionnement...")
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # Créer le dossier de destination si nécessaire
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        # Sauvegarder l'image
        img.save(output_path, "PNG", quality=95)
        print(f"Image sauvegardée : {output_path}")
        
        # Vérification finale
        with Image.open(output_path) as final:
            print(f"Image finale : {final.size}x{final.mode}")

def process_character_images(working_dir, processed_dir):
    print("Traitement de toutes les images des personnages...")
    
    # Créer les dossiers si nécessaire
    os.makedirs(processed_dir, exist_ok=True)
    
    # Traiter chaque image PNG dans le dossier working
    input_dir = Path(working_dir)
    for input_file in input_dir.glob("*_working.png"):
        # Générer le nom du fichier de sortie
        output_name = input_file.stem.replace("_working", "_processed") + ".png"
        output_path = Path(processed_dir) / output_name
        
        # Traiter l'image
        process_image(str(input_file), str(output_path))

if __name__ == "__main__":
    # Chemins des dossiers
    working_dir = "/Users/sylvainbonal/Documents/Cline/memory-bank/livre/illustrations/working/personnages"
    processed_dir = "/Users/sylvainbonal/Documents/Cline/memory-bank/livre/illustrations/processed/personnages"
    
    # Traitement par lots
    process_character_images(working_dir, processed_dir)