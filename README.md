# Dynamic Hydrophobia Experiment with Arduino and Python

## 📖 Description

This project explores the **hydrophobic properties of materials** by measuring the angle at which water drops detach from surfaces treated with different waxes.

The project consists of two main parts:

1. **Stepper motor control with Arduino** – rotates a glass platform where water drops are placed.
2. **Image processing with Python** – analyses captured images to determine the angle at which water drops detach.

---

## 🔧 Hardware Used

* Arduino Uno
* Stepper motor (3200 steps/rev)
* Glass microscope slide
* 12V, 3A stabilized power supply
* Camera for capturing water drop images
* Computer for Python analysis

---

## ⚙️ Installation

### Arduino

1. Connect the Arduino board to the stepper motor according to the wiring diagram.
2. Upload the program `moteur_control.ino` to the Arduino using the Arduino IDE.

### Python

1. Install the required libraries:

   ```bash
   pip install opencv-python numpy matplotlib
   ```
2. Use the `analyse_image.py` script to process the images and calculate drop angles.

---

## 🚀 Usage

### Arduino

* The Arduino program controls the platform rotation.
* Rotation is automatically adjusted to allow image capture at different angles.

### Python

* The Python script analyses water drop images to measure the contact angle.
* Run the script as follows:

  ```bash
  python analyse_image.py --image images/example_image.jpg
  ```

---

## 📂 Project Structure

* `arduino/moteur_control.ino` → Arduino code for stepper motor control
* `python/analyse_image.py` → Python script for image analysis and angle calculation
* `images/` → Folder containing test images
