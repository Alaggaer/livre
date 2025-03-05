#!/bin/bash

# Vérifie si un fichier est fourni en argument
if [ $# -eq 0 ]; then
    echo "Usage: ./convert-md-wk.sh fichier.md"
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

# Convertit le fichier
echo "Conversion de $1 en ${dirname}/${filename}.pdf..."
pandoc --pdf-engine=wkhtmltopdf \
    --variable papersize=a4paper \
    --variable geometry="margin=2.5cm" \
    --variable fontsize=11pt \
    -f markdown \
    -t pdf \
    "$1" \
    -o "${dirname}/${filename}.pdf"

if [ $? -eq 0 ]; then
    echo "✅ Conversion réussie ! Fichier créé : ${dirname}/${filename}.pdf"
else
    echo "❌ Erreur lors de la conversion"
fi