# ECG-detection
This GitHub repo contains a deep learning project focused on detecting arrhythmias in electrocardiogram (ECG) data.

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Features](#features)
- [Pre-requisites](#pre-requisites)
- [Usage](#usage)
- [References](#references)

# Project Overview



# Dataset
Kaggle - ECG Heartbeat Categorization Dataset | [Link](https://www.kaggle.com/datasets/shayanfazeli/heartbeat)

This dataset consist of 2 types of datasets. i.e. MIT-BIH Arrhythmia Dataset and PTB Diagnostic ECG dataset. In this, I considered arrhythmia dataset for building my project.

Dataset info:

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

Feature 1 :
  Extracting ECG signals from humans using ECG AD8252 sensor along with arduino UNO. This can also be implemented using ESP32 module.

  This is how the connectivity looks like:

  ![ECG-Monitoring-system-using-AD8232-with-Arduino](https://github.com/wothmag07/ECG-detection/assets/68963222/be5ebba3-08c9-40d8-b8b5-2a7d766780c0)


  I have included a live video demo under ECG extraction folder.


# Pre-requisites

Use Python 3.8.5. Setup conda environment, git clone repo and run the below commands,

pip install -r requirements.txt

For extracting ECG signals, you need hardware components. i.e, Arduino UNO/ESP32/ESP8266 , ECG sensor(AD8232), connecting wires, ECG electrodes and software tools like Arduino IDE and Pycharm.

Use the ECG extraction folder and circuit diagram for implementing this segment.

For training the model, edit the path directory of dataset and path where the model has to be placed and run the notebook. You can twirk hyperparameter values for seeing the performance of the model.





