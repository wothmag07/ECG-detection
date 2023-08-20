# ECG-detection
This GitHub repo contains a deep learning project focused on detecting arrhythmias in electrocardiogram (ECG) data and how to extract ECG signals from human.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Pre-requisites](#pre-requisites)
- [References](#references)

# Project Overview



# Dataset
Kaggle - ECG Heartbeat Categorization Dataset | [Link](https://www.kaggle.com/datasets/shayanfazeli/heartbeat)

This dataset consist of 2 types of datasets. i.e. MIT-BIH Arrhythmia Dataset and PTB Diagnostic ECG dataset. In this, I considered arrhythmia dataset for building my project.

__Dataset info:__

Number of Samples: 109446
Number of Categories: 5
Sampling Frequency: 125Hz

Classes: ['N': 0, 'S': 1, 'V': 2, 'F': 3, 'Q': 4]

-N : Non-ecotic beats (normal beat)
-S : Supraventricular ectopic beats
-V : Ventricular ectopic beats
-F : Fusion Beats
-Q : Unknown Beats

# Features

__Feature 1 :__
  Extracting ECG signals from humans using ECG AD8252 sensor along with arduino UNO. This can also be implemented using ESP32 module.

  This is how the connectivity looks like:

  ![Circuit-DiagramConnection-between-Arduino-and-ECG-Sensor-AD8232](https://github.com/wothmag07/ECG-detection/assets/68963222/56134468-b1b8-4079-8053-2532c10189f9)

  I have included a live video demo under ECG extraction folder. [Link](https://github.com/wothmag07/ECG-detection/tree/main/ECG%20extraction/Human%20Sample%20ECG)

__Feature 2:__
  Trained a model with deep convolutional neural network architecture for detecting the type of arrhythmic condition.


# Pre-requisites

Use Python 3.8.5. Setup conda environment, git clone repo and run the below commands,

pip install -r requirements.txt

For extracting ECG signals, you need hardware components. i.e, Arduino UNO/ESP32/ESP8266 , ECG sensor(AD8232), connecting wires, ECG electrodes and software tools like Arduino IDE and Pycharm.

Use the ECG extraction folder and circuit diagram for implementing this segment and set the baud rate to 9600 in arduino ide for viewing the ECG signal.

For training the model, edit the path directory of dataset and path where the model has to be placed and run the notebook. You can twirk hyperparameter values for seeing the performance of the model.

# References:
- [Medium](https://medium.com/)
- [Kaggle](https://www.kaggle.com/datasets/shayanfazeli/heartbeat)
- [Blog on ECG signal extraction](https://circuitdigest.com/microcontroller-projects/understanding-ecg-sensor-and-program-ad8232-ecg-sensor-with-arduino-to-diagnose-various-medical-conditions)
- Paper publication on Arrhythmia detection by Acharya





