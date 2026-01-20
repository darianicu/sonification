# \# MediaPipe Hand Gestures → Wekinator → Max (Drum Control)

# 

# This project uses \*\*MediaPipe hand tracking in Python\*\* to capture \*\*one-hand gestures\*\*, sends the data to \*\*Wekinator\*\* via \*\*OSC\*\*, and maps \*\*five learned gesture classes\*\* to \*\*drum sounds in Max\*\* (kick, snare, hi-hat, all, silence).

# 

# The system is designed for \*\*real-time performance, installation, and interactive music projects\*\*.

# 

# ---

# 

# \## Overview

# 

# \*\*Pipeline:\*\*

# 

# ```

# Webcam

# &nbsp; ↓

# Python (MediaPipe Hands)

# &nbsp; ↓  OSC (/wek/inputs)

# Wekinator (5 gesture classes)

# &nbsp; ↓  OSC

# Max/MSP (Drum control)

# ```

# 

# ---

# 

# \## Gesture Mapping

# 

# | Gesture Class | Function in Max |

# | ------------- | --------------- |

# | Class 0       | Kick only       |

# | Class 1       | Snare only      |

# | Class 2       | Hi-hat only     |

# | Class 3       | All drums       |

# | Class 4       | Silence         |

# 

# All gestures are \*\*trained by the user\*\* in Wekinator.

# 

# ---

# 

# \## Requirements

# 

# \### Software

# 

# \* Python 3.9 or higher

# \* Webcam

# \* Wekinator

# \* Max/MSP

# 

# \### Python Libraries

# 

# Install required libraries with:

# 

# ```bash

# pip install opencv-python mediapipe python-osc

# ```

# 

# ---

# 

# \## Files

# 

# ```

# .

# ├── hand\_to\_wekinator.py   # Python script (MediaPipe + OSC)

# ├── README.md              # This file

# ```

# 

# ---

# 

# \## Python: Hand Tracking → Wekinator

# 

# The Python script:

# 

# \* Tracks \*\*one hand\*\* using MediaPipe

# \* Extracts \*\*21 landmarks (x, y, z)\*\* → 63 values

# \* Sends landmark data via OSC to Wekinator at `/wek/inputs`

# 

# \### Run the script

# 

# ```bash

# python hand\_to\_wekinator.py

# ```

# 

# \* Press \*\*Q\*\* to quit.

# \* A webcam window will appear showing tracked hand landmarks.

# 

# ---

# 

# \## Wekinator Setup

# 

# 1\. Open \*\*Wekinator\*\*

# 2\. Create a \*\*New Project\*\*

# 

# &nbsp;  \* Input type: \*\*OSC\*\*

# &nbsp;  \* Input size: \*\*63\*\*

# &nbsp;  \* Output type: \*\*Class\*\*

# &nbsp;  \* Output size: \*\*1\*\*

# 3\. Make sure Wekinator is listening on:

# 

# &nbsp;  \* \*\*Port:\*\* `6448`

# 4\. Click \*\*Start Running\*\*

# 5\. Record training examples for \*\*5 gestures\*\*

# 

# &nbsp;  \* Gesture 1 → Class 0 (Kick)

# &nbsp;  \* Gesture 2 → Class 1 (Snare)

# &nbsp;  \* Gesture 3 → Class 2 (Hi-hat)

# &nbsp;  \* Gesture 4 → Class 3 (All)

# &nbsp;  \* Gesture 5 → Class 4 (Silence)

# 6\. Train and enable \*\*Run\*\* mode

# 

# ---

# 

# \## Max/MSP Setup

# 

# Wekinator sends gesture classifications via OSC to Max.

# 

# \### Basic Max logic

# 

# ```max

# \[udpreceive 12000]

# |

# \[int]

# |

# \[select 0 1 2 3 4]

# ```

# 

# Connect each outlet to:

# 

# \* Kick

# \* Snare

# \* Hi-hat

# \* All drums

# \* Silence / mute

# 

# You can expand this to control:

# 

# \* Drum machines

# \* Samplers

# \* MIDI

# \* Audio effects

# 

# ---

# 

# \## Notes \& Tips

# 

# \* Keep your hand \*\*clearly visible and centered\*\* during training

# \* Train gestures with \*\*consistent posture\*\*

# \* Use \*\*silence gesture\*\* as a resting state to avoid accidental triggers

# \* For live performance, gesture smoothing is recommended

# 

# ---

# 

# \## Possible Extensions

# 

# \* Gesture smoothing / debounce

# \* Two-hand support

# \* Continuous control (velocity, filter, tempo)

# \* TouchDesigner or Unity integration

# \* MIDI output instead of OSC

# 

# ---

# 

# \## License

# 

# This project is provided for \*\*educational and artistic use\*\*.

# Feel free to modify and adapt for your own performances and installations.

# 

# ---

# 

# \## Credits

# 

# Built with:

# 

# \* MediaPipe

# \* Wekinator

# \* Max/MSP

# \* Open Sound Control (OSC)

# 

# ---

# 

# If you want, I can also:

# 

# \* Add \*\*installation screenshots\*\*

# \* Write a \*\*short artist statement\*\*

# \* Create a \*\*Max patch example\*\*

# \* Add \*\*gesture diagrams\*\* for training

# 

# Just tell me.



