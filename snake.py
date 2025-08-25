import pygame
import random

class SnakeGame:
    def __init__(self, screen):
        self.screen = screen
        self.block_size = 20
        self.direction = 'RIGHT'
        self.snake = [(100, 100)]
        self.food = self.spawn_food()
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)
        self.alive = True

    def spawn_food(self):
        x = random.randint(0, 29) * self.block_size
        y = random.randint(0, 29) * self.block_size
        return (x, y)

    def change_direction(self, new_direction):
        opposites = {'UP': 'DOWN', 'DOWN': 'UP', 'LEFT': 'RIGHT', 'RIGHT': 'LEFT'}
        if new_direction and new_direction != opposites.get(self.direction):
            self.direction = new_direction

    def update(self):
        if not self.alive:
            return

        x, y = self.snake[0]
        if self.direction == 'UP':
            y -= self.block_size
        elif self.direction == 'DOWN':
            y += self.block_size
        elif self.direction == 'LEFT':
            x -= self.block_size
        elif self.direction == 'RIGHT':
            x += self.block_size

        new_head = (x, y)
        self.snake.insert(0, new_head)

        if new_head == self.food:
            self.food = self.spawn_food()
            self.score += 1
        else:
            self.snake.pop()

        if (
            x < 0 or x >= 600 or
            y < 0 or y >= 600 or
            new_head in self.snake[1:]
        ):
            self.alive = False

    def is_alive(self):
        return self.alive

    def draw(self):
        self.screen.fill((0, 0, 0))
        for block in self.snake:
            pygame.draw.rect(self.screen, (0, 255, 0), (*block, self.block_size, self.block_size))
        pygame.draw.rect(self.screen, (255, 0, 0), (*self.food, self.block_size, self.block_size))

        score_text = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))