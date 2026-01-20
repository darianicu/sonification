import cv2
import mediapipe as mp
from pythonosc import udp_client

# -------------------
# Wekinator OSC setup
# -------------------
# Wekinator listens on localhost:6448 for inputs
client = udp_client.SimpleUDPClient("127.0.0.1", 6448)

# -------------------
# MediaPipe Hands setup
# -------------------
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,               # only one hand
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils

# -------------------
# Helper function
# -------------------
def get_hand_data(hand_landmarks):
    """
    Flatten 21 landmarks (x,y,z) to a list of 63 floats
    """
    data = []
    for lm in hand_landmarks.landmark:
        data.extend([lm.x, lm.y, lm.z])
    return data

# -------------------
# Open webcam
# -------------------
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot read from webcam")
        break

    frame = cv2.flip(frame, 1)  # mirror view
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            # Draw landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Get flat hand data for OSC
            hand_data = get_hand_data(hand_landmarks)
            
            # Send to Wekinator
            client.send_message("/wek/inputs", hand_data)
    else:
        # Send zeros if no hand is detected (optional)
        client.send_message("/wek/inputs", [0]*63)

    cv2.imshow("Hand to Wekinator", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
