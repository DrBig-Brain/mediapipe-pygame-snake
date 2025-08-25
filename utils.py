def get_direction_from_landmarks(landmarks):
    wrist = landmarks.landmark[0]
    index_tip = landmarks.landmark[8]

    dx = index_tip.x - wrist.x
    dy = index_tip.y - wrist.y

    if abs(dx) > abs(dy):
        return 'RIGHT' if dx > 0 else 'LEFT'
    else:
        return 'DOWN' if dy > 0 else 'UP'