# Expérience d'Hydrophobie Dynamique avec Arduino et Analyse Python

## Description
Ce projet vise à explorer les propriétés hydrophobes de différents matériaux, notamment en mesurant l'angle d'arrachement des gouttes d'eau sur des surfaces traitées avec diverses cires. Le projet comprend deux parties :
1. **Contrôle du moteur pas à pas avec Arduino** : Utilisé pour faire varier l'angle d'une plateforme en verre où les gouttes d'eau sont déposées.
2. **Traitement d'image avec Python** : Analyse des images prises pour déterminer l'angle d'arrachement des gouttes d'eau en fonction des surfaces testées.

## Matériel Utilisé
- Arduino Uno
- Moteur pas à pas (3200 pas par tour)
- Lame de microscope en verre
- Alimentation stabilisée 12V, 3A
- Caméra pour prendre des photos des gouttes d'eau
- Ordinateur pour exécuter l'analyse Python

## Installation
### Arduino
1. Connecter la carte Arduino au moteur pas à pas selon le schéma.
2. Charger le programme `moteur_control.ino` dans la carte Arduino via l'IDE Arduino.

### Python
1. Installer les bibliothèques nécessaires :
    ```bash
    pip install opencv-python numpy matplotlib
    ```
2. Utiliser le script `analyse_image.py` pour analyser les images et obtenir les angles des gouttes.

## Usage
### Arduino
1. Le programme contrôle la rotation de la plateforme.
2. L'angle de rotation est ajusté automatiquement pour permettre de capturer des images à différents angles.

### Python
1. Le script analyse les images des gouttes d'eau pour mesurer l'angle de contact.
2. Exécute le script comme suit :
    ```bash
    python analyse_image.py --image images/example_image.jpg
    ```

## Structure du Projet
- `arduino/moteur_control.ino` : Le code Arduino pour contrôler le moteur pas à pas.
- `python/analyse_image.py` : Le script Python pour analyser les images et obtenir l'angle de la goutte d'eau.
- `images/` : Dossier contenant les images à analyser.
