from PIL import Image, ImageEnhance, ImageFilter
import os
from pathlib import Path

def process_image(input_path, output_path):
    print(f"Traitement de l'image : {input_path}")
    
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

if __name__ == "__main__":
    # Chemins des images
    input_path = "/Users/sylvainbonal/Documents/Cline/memory-bank/livre/illustrations/working/personnages/ecureuil_gris_working.png"
    output_path = "/Users/sylvainbonal/Documents/Cline/memory-bank/livre/illustrations/processed/personnages/ecureuil_gris_processed.png"
    
    # Traitement
    process_image(input_path, output_path)