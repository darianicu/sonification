MediaPipe Hand Gestures → Wekinator → Max (Drum Control)

This project uses MediaPipe hand tracking in Python to capture one-hand gestures, sends the data to Wekinator via OSC, and maps five learned gesture classes to drum sounds in Max(kick, snare, hi-hat, all, silence).

 Overview
Pipeline:
# Webcam
# &nbsp; ↓
# Python (MediaPipe Hands)
# &nbsp; ↓  OSC (/wek/inputs)
# Wekinator (5 gesture classes)
# &nbsp; ↓  OSC
# Max/MSP (Drum control)
#
#  Gesture Mapping
#
# | Gesture Class | Function in Max |
# | Class 1       | Kick only       |
# | Class 2       | Snare only      |
# | Class 3       | Hi-hat only     |
# | Class 4       | Start sound     |
# | Class 5       | stop sound      |
#
# All gestures are trained by the user in Wekinator.
#
# Requirements
#  Software
# \* Python 3.9 or higher
# \* Webcam
# \* Wekinator
# \* Max/MSP
# 
# Python Libraries
# Install required libraries with:
# ```  pip install opencv-python mediapipe python-osc  ```
#
# Files
# pose_to_wekinator.py   # Python script (MediaPipe + OSC)
# README.md              # This file
# Max MSP drum patch
# Wekinator trained model
#
# Run the script
# ``` python pose_to_wekinator.py```


