import mediapipe as mp
import cv2
from utils import get_direction_from_landmarks
from snake import SnakeGame


class HandTracker:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(max_num_hands=1)
        self.mp_draw = mp.solutions.drawing_utils

    def get_hand_position(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(rgb)
        if results.multi_hand_landmarks:
            return results.multi_hand_landmarks[0]
        return None

    def get_direction(self, landmarks):
        return get_direction_from_landmarks(landmarks)