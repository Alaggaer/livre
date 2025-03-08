# Système de Versionnement du Projet Livre-Enfant-Serie

## Structure des Dossiers

```
versions/
├── finales/          # Versions validées et finalisées
│   ├── livres/       # Contenu des livres
│   ├── common/       # Ressources communes
│   └── docs/         # Documentation
├── travail/          # Versions en cours de travail
│   ├── livres/       # Versions temporaires des livres
│   ├── common/       # Modifications des ressources communes
│   └── docs/         # Documentation en cours
└── archive/          # Anciennes versions conservées
    ├── livres/
    ├── common/
    └── docs/
```

## Fonctionnement

### 1. Sauvegarde Automatique

Le script `scripts/auto-save.sh` s'occupe de :
- Surveiller les modifications des fichiers
- Créer des versions horodatées dans `versions/travail/`
- Conserver les 5 dernières versions de chaque fichier
- Organiser les fichiers par catégorie (livres, common, docs)

### 2. Organisation des Versions

- **versions/travail/** : Contient les versions en cours de modification. Les fichiers sont automatiquement sauvegardés avec un horodatage (ex: `chapitre1_20250307_085100.md`)
- **versions/finales/** : Une fois qu'une version est validée, elle doit être déplacée ici
- **versions/archive/** : Pour conserver les anciennes versions importantes

### 3. Utilisation

1. **Sauvegarde automatique** :
   ```bash
   ./scripts/auto-save.sh
   ```
   Exécutez cette commande après chaque session de travail ou configurez-la comme tâche automatique.

2. **Finaliser une version** :
   - Une fois satisfait d'une version, copiez-la manuellement dans le dossier `versions/finales/`
   - Utilisez une nomenclature claire : `nom-fichier_v1.0.md`

3. **Archiver une version** :
   - Les versions importantes mais obsolètes doivent être déplacées dans `versions/archive/`
   - Utile pour conserver l'historique des changements majeurs

### 4. Bonnes Pratiques

1. **Nommage des Fichiers** :
   - Versions de travail : `nom-fichier_YYYYMMDD_HHMMSS.md`
   - Versions finales : `nom-fichier_v1.0.md`
   - Versions archivées : `nom-fichier_v1.0_archive.md`

2. **Gestion des Versions** :
   - Limitez-vous aux 5 dernières versions de travail
   - Conservez toutes les versions finales importantes
   - Documentez les changements majeurs

3. **Synchronisation** :
   - Utilisez Dropbox pour synchroniser tout le dossier `versions/`
   - Dropbox conserve aussi un historique supplémentaire (30 jours)

### 5. En Cas de Problème

1. **Retrouver une version récente** :
   - Regardez dans `versions/travail/` pour les 5 dernières versions
   - Vérifiez l'historique Dropbox pour les versions plus anciennes

2. **Restaurer une version** :
   - Copiez la version souhaitée depuis `versions/travail/` ou `versions/finales/`
   - Replacez-la dans le répertoire de travail approprié

3. **Versions perdues** :
   - Vérifiez `versions/archive/`
   - Consultez l'historique Dropbox
   - Contactez l'équipe technique si nécessaire

## Notes Importantes

- Le script de sauvegarde s'exécute sur les fichiers modifiés dans les dernières 24 heures
- Les fichiers sont organisés automatiquement par catégorie
- Dropbox fournit une couche de sécurité supplémentaire
- Ne supprimez jamais directement des fichiers dans `versions/finales/`