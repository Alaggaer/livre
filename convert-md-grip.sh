#!/bin/bash

# Vérifie si un fichier est fourni en argument
if [ $# -eq 0 ]; then
    echo "Usage: ./convert-md-grip.sh fichier.md"
    exit 1
fi

# Vérifie si le fichier existe
if [ ! -f "$1" ]; then
    echo "Erreur: Le fichier $1 n'existe pas"
    exit 1
fi

# Extrait le nom du fichier sans extension
filename=$(basename -- "$1")
filename="${filename%.*}"
dirname=$(dirname "$1")

# Convertit d'abord en HTML avec grip
echo "Conversion de $1 en HTML..."
grip "$1" --export "${dirname}/${filename}.html"

# Puis convertit l'HTML en PDF avec Chrome headless
echo "Conversion de ${dirname}/${filename}.html en PDF..."
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
    --headless \
    --disable-gpu \
    --print-to-pdf="${dirname}/${filename}.pdf" \
    "file://${PWD}/${dirname}/${filename}.html"

# Nettoie le fichier HTML temporaire
rm "${dirname}/${filename}.html"

if [ -f "${dirname}/${filename}.pdf" ]; then
    echo "✅ Conversion réussie ! Fichier créé : ${dirname}/${filename}.pdf"
else
    echo "❌ Erreur lors de la conversion"
fi