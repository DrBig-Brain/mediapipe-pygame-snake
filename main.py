import pygame
import cv2
from snake import SnakeGame
from hand_tracker import HandTracker

def main():
    cap = cv2.VideoCapture(0)
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    game = SnakeGame(screen)
    tracker = HandTracker()

    running = True
    while running:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        hand_landmarks = tracker.get_hand_position(frame)

        if hand_landmarks:
            direction = tracker.get_direction(hand_landmarks)
            game.change_direction(direction)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.update()
        game.draw()
        pygame.display.flip()
        clock.tick(5)

        if not game.is_alive():
            game.screen.fill((0, 0, 0))
            font = pygame.font.SysFont(None, 48)
            text = font.render("Game Over", True, (255, 0, 0))
            game.screen.blit(text, (200, 280))
            pygame.display.flip()
            pygame.time.wait(1500)
            running = False

        cv2.imshow("Hand Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    pygame.quit()

if __name__ == "__main__":
    main()