import pygame
import random


class Colors:
    GREEN = (0, 150, 0)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)


class Game:
    def __init__(self):
        pygame.font.init()

        self.WIDTH, self.HEIGHT = 750, 750
        self.FPS = 60
        self.player_speed = 7
        self.enemy_speed = 5

        self.triesFont = pygame.font.SysFont("Courier", 26)

        self.WIN = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Meteorites")

        self.localP = pygame.rect.Rect(((self.WIDTH//2) - 10//2, self.HEIGHT-200), (25,25))

        self.enemy_list = []

        self.main()

    def main(self):
        run = True
        plays = 0
        clock = pygame.time.Clock()
        self.gen_enemies(3, 3, 3, 3)

        while run:
            clock.tick(self.FPS)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    run = False

            keys_pressed = pygame.key.get_pressed()

            self.player_movement(keys_pressed)
            self.enemy_movement()

            if self.enemy_collision():
                plays += 1
                self.reset()

            self.draw_window(plays)

    def reset(self): # reset localp and enemies position
        p = 0
        c=0
        for a, i in self.enemy_list:
            if i == "top":
                a.y = -50 * p
                p+=1
            elif i == 'bottom':
                a.y = self.HEIGHT + 50 * p
                c += 1
            if i == "left":
                a.x = (random.randint(30, self.HEIGHT-30))
            elif i == 'right':
                a.x = (random.randint(30, self.HEIGHT-30))
        self.localP.x = self.WIDTH//2 - 10/2
        self.localP.y = self.HEIGHT-200

    def draw_window(self, plays):
        self.WIN.fill(Colors.GREEN)

        pygame.draw.rect(self.WIN, Colors.BLACK, self.localP)

        for i,a in self.enemy_list:
            pygame.draw.rect(self.WIN, Colors.RED, i)

        tries_text = self.triesFont.render(f"Plays: {plays}", True, Colors.BLACK)
        self.WIN.blit(tries_text, (10,10))

        pygame.display.update()

    def player_movement(self, keys_pressed):
        if keys_pressed[pygame.K_w] and self.localP.y >= 0:
            self.localP.y -= self.player_speed
        if keys_pressed[pygame.K_s] and self.localP.y <= self.HEIGHT - self.localP.height:
            self.localP.y += self.player_speed
        if keys_pressed[pygame.K_a] and self.localP.x >= 0:
            self.localP.x -= self.player_speed
        if keys_pressed[pygame.K_d] and self.localP.x <= self.WIDTH - self.localP.width:
            self.localP.x += self.player_speed

    def enemy_movement(self):

        for i, a in self.enemy_list:
            if a == 'top':
                i.y += self.enemy_speed
                if i.y > self.HEIGHT + i.height:
                    i.y = -50
                    i.x = random.randint(30, self.WIDTH-30)
            elif a == 'bottom':
                i.y -= self.enemy_speed
                if i.y < - 50:
                    i.y = self.HEIGHT + 50
                    i.x = random.randint(30, self.WIDTH - 30)
            elif a == 'left':
                i.x += self.enemy_speed
                if i.x > self.WIDTH + 50:
                    i.x = -50
                    i.y = random.randint(30, self.HEIGHT - 30)
            elif a == 'right':
                i.x -= self.enemy_speed
                if i.x < - 50:
                    i.x = self.WIDTH + 50
                    i.y = random.randint(30, self.HEIGHT - 30)

    def enemy_collision(self) -> bool:
        for i, a in self.enemy_list:
            if self.localP.colliderect(i):
                return True
        return False

    def gen_enemies(self, top, bottom, left, right):
        for i in range(top):
            self.enemy_list.append([pygame.rect.Rect((random.randint(30, self.WIDTH-30), -50 * i), (30, 30)), 'top'])
        for i in range(bottom):
            self.enemy_list.append([pygame.rect.Rect((random.randint(30, self.WIDTH - 30), self.HEIGHT + 50 * i), (30, 30)), 'bottom'])
        for i in range(left):
            self.enemy_list.append([pygame.rect.Rect((-50 * i, (random.randint(30, self.HEIGHT-30))), (30, 30)), 'left'])
        for i in range(right):
            self.enemy_list.append([pygame.rect.Rect((self.WIDTH + 50*i, (random.randint(30, self.HEIGHT-30))), (30, 30)), 'right'])

game = Game()
