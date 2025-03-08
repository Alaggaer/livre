#!/bin/bash

# Configuration
WORKSPACE_ROOT="/Users/sylvainbonal/Documents/Cline/memory-bank/livre-enfant-serie"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
MAX_VERSIONS=5

# Liste des dossiers à surveiller
MONITORED_DIRS=(
    "livre1/chapitres"
    "livre2/chapitres"
    "livre3/chapitres"
    "common"
    "docs"
)

save_modified_files() {
    local source_dir="$1"
    local base_dir=$(echo "$source_dir" | cut -d'/' -f1)
    
    # Détermine le dossier de destination en fonction du type de contenu
    if [[ $source_dir == livre* ]]; then
        dest_category="livres/$base_dir"
    else
        dest_category="$base_dir"
    fi
    
    # Parcourt les fichiers modifiés dans les dernières 24 heures
    find "$WORKSPACE_ROOT/$source_dir" -type f -mtime -1 -name "*.md" | while read file; do
        # Extrait le nom du fichier
        filename=$(basename "$file")
        
        # Crée le nom de fichier avec timestamp
        versioned_filename="${filename%.*}_${TIMESTAMP}.md"
        
        # Copie vers le dossier versions-travail
        mkdir -p "$WORKSPACE_ROOT/versions/travail/$dest_category"
        cp "$file" "$WORKSPACE_ROOT/versions/travail/$dest_category/$versioned_filename"
        
        echo "Sauvegarde : $file -> versions/travail/$dest_category/$versioned_filename"
        
        # Nettoie les anciennes versions si nécessaire
        cleanup_old_versions "$dest_category" "$filename"
    done
}

cleanup_old_versions() {
    local category="$1"
    local base_filename="$2"
    
    # Garde uniquement les MAX_VERSIONS plus récentes versions
    cd "$WORKSPACE_ROOT/versions/travail/$category" || return
    
    ls -t "${base_filename%.*}"_*.md 2>/dev/null | awk "NR>$MAX_VERSIONS" | xargs -r rm
    
    cd - >/dev/null
}

# Exécute la sauvegarde pour chaque dossier surveillé
for dir in "${MONITORED_DIRS[@]}"; do
    if [ -d "$WORKSPACE_ROOT/$dir" ]; then
        save_modified_files "$dir"
    fi
done

echo "Sauvegarde automatique terminée à $(date)"