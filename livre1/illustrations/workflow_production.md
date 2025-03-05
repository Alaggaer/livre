# Workflow de Production des Illustrations

## 1. Design des Personnages

### Ordre de Production
1. Écureuil Gris (personnage principal)
   - Base design
   - Expressions clés (inquiétude, curiosité, joie)
   - Poses d'action

2. Lapin Blanc (deutéragoniste)
   - Base design
   - Expressions clés (détermination, réflexion, satisfaction)
   - Poses d'action

3. Olivia la Chouette
   - Base design
   - Expressions clés (sagesse, bienveillance)
   - Poses statiques

4. Coccinelle Arc-en-Ciel
   - Base design
   - Variations de vol
   - Effets lumineux

5. Carlos le Coati
   - Base design
   - Expressions clés (gêne, amitié)
   - Poses d'action

### Structure des Dossiers
```
illustrations/personnages/
├── ecureuil_gris/
│   ├── development.md
│   ├── finals/
│   └── resources/
├── lapin_blanc/
│   ├── development.md
│   ├── finals/
│   └── resources/
...etc
```

## 2. Production des Scènes

### Ordre de Production
1. Scènes du Chapitre 1
   - Le réveil dans la forêt
   - La cache vide

2. Scènes du Chapitre 2
   - La découverte de la plume
   - L'arrivée chez Olivia

3. Scène du Chapitre 5
   - La clairière magique

4. Scènes du Chapitre 7
   - La maison de Carlos
   - La grande fête finale

### Structure des Dossiers
```
illustrations/scenes/
├── chapitre1/
│   ├── README.md
│   ├── finals/
│   └── resources/
├── chapitre2/
...etc
```

## 3. Workflow par Illustration

### Phase 1 : Préparation
1. Créer le dossier approprié selon la structure
2. Initialiser le fichier development.md ou README.md
3. Préparer les ressources de référence

### Phase 2 : Génération
1. Générer la version de base selon le prompt défini
2. Itérer avec de légères variations (3-5 versions)
3. Sélectionner la meilleure version

### Phase 3 : Raffinement
1. Ajuster les paramètres si nécessaire
2. Ajouter les détails et effets spécifiques
3. Générer la version finale

### Phase 4 : Post-Production
1. Vérifier la cohérence avec les autres illustrations
2. Optimiser l'image selon les standards
3. Archiver dans le dossier finals/

## 4. Standards de Qualité

### Pour les Personnages
- Format : --ar 1:1
- Résolution : --s 750
- Qualité : --q 2
- Fond : Pure white background
- Style : Pixar style 3D animation

### Pour les Scènes
- Format : --ar 16:9
- Résolution : --s 750
- Qualité : --q 2
- Fond : Pure white background
- Style : Pixar style 3D animation

## 5. Documentation

### Pour Chaque Personnage (development.md)
```markdown
# [Nom du Personnage]

## Design de Base
- Prompt utilisé
- Paramètres
- Notes sur les itérations

## Variations d'Expression
- Liste des expressions
- Prompts et paramètres
- Références utilisées

## Versions Finales
- Liste des fichiers
- Localisation
- Notes techniques
```

### Pour Chaque Scène (README.md)
```markdown
# [Nom de la Scène]

## Description
- Moment de l'histoire
- Ambiance recherchée
- Éléments clés

## Génération
- Prompt utilisé
- Paramètres
- Itérations

## Version Finale
- Fichier final
- Notes techniques
- Points d'attention
```

## 6. Conventions de Nommage

### Fichiers de Travail
- Format : `[type]_[nom]_v[X]_[timestamp]`
- Exemple : `character_ecureuil_gris_v1_1234567890`

### Fichiers Finaux
- Format : `[type]_[nom]_[version]`
- Exemple : `character_ecureuil_gris_final_v1`

## 7. Points d'Attention
1. Maintenir la cohérence du style entre toutes les illustrations
2. Respecter les proportions adaptées au jeune public
3. S'assurer de la lisibilité des expressions
4. Documenter chaque étape du processus
5. Sauvegarder régulièrement les versions de travail