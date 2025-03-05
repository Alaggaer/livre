# Test Pipeline IA - Écureuil Gris

## Configuration ComfyUI

### Installation Test
```bash
# Clone et setup
git clone https://github.com/comfyanonymous/ComfyUI
cd ComfyUI
pip install -r requirements.txt

# Extensions nécessaires
pip install opencv-python
pip install controlnet-tools
pip install color-matcher
```

## Workflow Test

```json
{
  "nodes": {
    "load_image": {
      "type": "LoadImage",
      "inputs": {
        "path": "working/personnages/ecureuil_gris_working.png"
      }
    },
    "color_correction": {
      "type": "ColorMatcher",
      "inputs": {
        "image": "load_image.output",
        "target_colors": {
          "primary": "#808080",
          "secondary": "#A9A9A9",
          "details": "#696969"
        }
      }
    },
    "enhance_details": {
      "type": "ControlNetDetailer",
      "inputs": {
        "image": "color_correction.output",
        "focus_areas": ["eyes", "tail", "expression"],
        "enhancement_level": 0.7
      }
    },
    "final_adjustments": {
      "type": "ImageProcessor",
      "inputs": {
        "image": "enhance_details.output",
        "brightness": 1.05,
        "contrast": 1.1,
        "sharpness": 1.2
      }
    },
    "save_image": {
      "type": "SaveImage",
      "inputs": {
        "image": "final_adjustments.output",
        "path": "processed/personnages/ecureuil_gris_final.png"
      }
    }
  }
}
```

## Instructions LLM

### Prompt de Guidage
```python
def create_adjustment_prompt(retouches_md):
    return f"""
    Guide les ajustements de l'image en suivant ces étapes :

    1. Analyse le guide de retouche :
    {retouches_md}

    2. Pour chaque étape :
    - Identifie les paramètres ComfyUI appropriés
    - Suggère les valeurs optimales
    - Valide les résultats

    3. Points de contrôle :
    - Vérification des couleurs
    - Qualité des détails
    - Expression du personnage
    """
```

## Test de Workflow

### Étape 1 : Harmonisation des Couleurs
```python
def harmonize_colors(image):
    # Lecture des tons cibles
    target_grays = {
        "main": (128, 128, 128),    # #808080
        "light": (169, 169, 169),   # #A9A9A9
        "dark": (105, 105, 105)     # #696969
    }
    
    # Application des corrections
    corrected = color_matcher.match_histogram(
        image,
        target_grays,
        method='mvgd'
    )
    
    return corrected
```

### Étape 2 : Amélioration des Détails
```python
def enhance_features(image):
    # Zones d'intérêt
    regions = {
        "eyes": {
            "enhance": 1.2,
            "sharpen": 1.1
        },
        "tail": {
            "enhance": 1.15,
            "texture": 1.1
        },
        "expression": {
            "enhance": 1.1,
            "contrast": 1.05
        }
    }
    
    # Application des améliorations
    for region, params in regions.items():
        image = controlnet.enhance_region(
            image,
            region,
            params
        )
    
    return image
```

### Étape 3 : Validation
```python
def validate_results(image, guide):
    # Critères de validation
    criteria = {
        "colors": check_color_harmony,
        "details": verify_detail_quality,
        "expression": evaluate_expression,
        "print_ready": check_print_specs
    }
    
    # Exécution des tests
    results = {}
    for name, test in criteria.items():
        results[name] = test(image)
    
    return results
```

## Métriques de Qualité

### Tests Automatiques
- [ ] Respect de la palette
- [ ] Netteté des détails
- [ ] Contraste et luminosité
- [ ] Format et résolution

### Validation Humaine
- [ ] Expression naturelle
- [ ] Cohérence du style
- [ ] Aspect enfantin
- [ ] Impression test

## Notes de Développement

### Priorités
1. Pipeline de base fonctionnel
2. Tests sur l'Écureuil Gris
3. Ajustements des paramètres
4. Extension aux autres personnages

### Points d'Attention
- Maintenir la simplicité du style
- Éviter la sur-retouche
- Garder des sauvegardes
- Documenter les réussites/échecs

### Prochaines Étapes
1. Setup environnement ComfyUI
2. Test du workflow basique
3. Ajustements guidés par LLM
4. Validation des résultats