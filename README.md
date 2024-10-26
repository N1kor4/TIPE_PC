# Dynamic Hydrophobia Experiment with Arduino and Python Analysis

## Description
The aim of this project is to explore the hydrophobic properties of different materials, in particular by measuring the angle at which water drops are pulled off surfaces treated with various waxes. The project has two parts:
1. **Stepper motor control with Arduino**: Used to vary the angle of a glass platform where water drops are deposited.
2. **Image processing with Python**: Analysis of the images taken to determine the angle at which the water drops are pulled away from the surfaces tested.

## Hardware used
- Arduino Uno
- Stepper motor (3200 steps per revolution)
- Glass microscope slide
- 12V, 3A stabilised power supply
- Camera to take pictures of the water drops
- Computer to run the Python analysis

## Installation
### Arduino
1. Connecter la carte Arduino au moteur pas à pas selon le schéma.
2. Charger le programme `moteur_control.ino` dans la carte Arduino via l'IDE Arduino.

### Python
1. Install the necessary libraries:
    ```bash
    pip install opencv-python numpy matplotlib
    ```
2. Use the `analyse_image.py` script to analyse the images and obtain the angles of the drops.

## Usage
### Arduino
1. The program controls the rotation of the platform.
2. The rotation angle is automatically adjusted to capture images at different angles.

### Python
1. The script analyses the images of the water drops to measure the contact angle.
2. Run the script as follows:
    ```bash
    python analyse_image.py --image images/example_image.jpg
    ```
    
## Project structure
- `arduino/moteur_control.ino` : The Arduino code to control the stepper motor.
- `python/analyse_image.py` : The Python script to analyse the images and obtain the angle of the water drop.
- `images/` : Folder containing the images to be analysed.
