# 🐍 Gesture-Controlled Snake Game

A modern take on the classic Snake game where you control the snake using hand gestures captured through your webcam!

## 🎮 How to Play

1. Run the game using `python main.py`
2. Use your hand gestures to control the snake:
   - Point up to move UP
   - Point down to move DOWN
   - Point left to move LEFT
   - Point right to move RIGHT
3. Collect the red food blocks to grow the snake and increase your score
4. Avoid hitting the walls or the snake's own body

## 📦 Requirements

- Python 3.8+
- OpenCV
- Pygame
- MediaPipe

Install the required dependencies:

```bash
pip install opencv-python pygame mediapipe
```

## 🔧 Project Structure

- `main.py` - The main game loop and initialization
- `snake.py` - Snake game logic implementation
- `hand_tracker.py` - Hand gesture detection using MediaPipe
- `utils.py` - Utility functions for gesture processing

## 🎯 Features

- Real-time hand gesture recognition
- Classic snake gameplay mechanics
- Score tracking
- Game over detection
- Smooth controls using hand movements

## ⌨️ Controls

- Show your palm to the webcam
- Point your index finger in the direction you want the snake to move
- Press 'Q' to quit the game

## 🚀 Getting Started

1. Clone the repository
2. Install the dependencies
3. Run the game:
   ```bash
   python main.py
   ```
4. Position yourself in front of the webcam
5. Start playing!

## 📝 Note

Make sure you have good lighting conditions for optimal hand tracking