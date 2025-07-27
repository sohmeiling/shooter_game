'''
1. A menu screen for game over
2. Enable to restart the game with mouse input

'''
import pygame
from pygame import *
from random import randint

# Window settings
width = 700
height = 500
window = display.set_mode((width, height))
display.set_caption("Shooter Game!")

# image
heart = transform.scale(image.load("heart.png"), (30, 30))

# Background
background = transform.scale(image.load("galaxy.jpg"), (width, height))

# Set music
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()

# Sound effects
fire_sound = mixer.Sound("fire.ogg")

# Set colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)

# Set fonts
## Option 1

font.init()
font_name = font.Font(None, 36)

font_msg = font.Font(None, 80)  # This is for win message
win_text = font_msg.render("YOU WIN!", True, GREEN)
lose_text = font_msg.render("YOU LOSE!", True, RED)
game_over_text = font_msg.render("GAME OVER!", True, RED)

# Parent class
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# Player class
class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet("bullet.png", self.rect.centerx, self.rect.top, 15, 20, 10)
        bullets.add(bullet)

# Enemy class
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
        self.health = 2 #2hits to die

    def update(self):
        self.rect.y += self.speed
        global missed
        if self.rect.y > height:
            self.rect.y = 0
            self.rect.x = randint(80, width - 80)
            missed += 1

# Bullet class
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

# Functions to restart the game
def restart_game(full_restart=False):
    global score, missed, finish, ufos, bullets, lives
    score = 0
    missed = 0
    finish = False
    ufos.empty()
    bullets.empty()
    for i in range(1, 6):
        ufo = Enemy("ufo.png", randint(80, width - 80), -40, 80, 50, randint(1, 2))
        ufos.add(ufo)
    if full_restart:
        lives = 3

def game_over_menu():
    window.blit(background, (0, 0))
    window.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, 100))

    restart_button = Rect(width // 2 - 100, 250, 200, 50)
    exit_button = Rect(width // 2 - 100, 320, 200, 50)

    draw.rect(window, RED, restart_button)
    draw.rect(window, RED, exit_button)

    restart_text = font_name.render("Restart Game", True, WHITE)
    exit_text = font_name.render("Exit", True, WHITE)

    window.blit(restart_text, (restart_button.x + 25, restart_button.y + 10))
    window.blit(exit_text, (exit_button.x + 70, exit_button.y + 10))

    display.update()

    waiting = True
    while waiting:
        for e in event.get():
            if e.type == QUIT:
                quit()
            elif e.type == MOUSEBUTTONDOWN:
                mouse_pos = mouse.get_pos()
                if restart_button.collidepoint(mouse_pos):
                    restart_game(full_restart=True)
                    return
                elif exit_button.collidepoint(mouse_pos):
                    global run
                    run = False
                    waiting = False



# Create variables
score = 0
missed = 0
goal = 10 # Number of enemies to destroy to win
lives = 3

# Create sprites
rocket = Player("rocket.png", 5, height - 100, 80, 100, 10)

ufos = sprite.Group()
for i in range(1, 6):
    ufo = Enemy("ufo.png", randint(80, width - 80), -40, 80, 50, randint(1, 2))
    ufos.add(ufo)

# Unlimited bullets
bullets = sprite.Group()


# Set game loop
run = True
finish = False
clock = time.Clock()
FPS = 60
show_game_over_menu = False

while run:
    # Events
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                fire_sound.play()
                rocket.fire()

    
    if not finish:
        window.blit(background, (0, 0))

        # Create heart sprites for lives
        for i in range(lives):
            window.blit(heart, (width - (i + 1) * 35, 10))

        # Draw sprites
        rocket.reset()
        ufos.draw(window)
        bullets.draw(window)

        # Counter score
        score_counter = font_name.render("Score: " + str(score), True, WHITE)
        window.blit(score_counter, (10, 10))

        missed_counter = font_name.render("Missed: " + str(missed), True, WHITE)
        window.blit(missed_counter, (10, 35))

        # Move sprites
        rocket.update()
        ufos.update()
        bullets.update()

        # Check collision
        hits = sprite.groupcollide(ufos, bullets, False, True) # True means to remove the bullet and the ufo
        for ufo in hits:
            ufo.health -= 1
            if ufo.health <= 0:
                ufo.kill()
                score += 1
                ufo = Enemy("ufo.png", randint(80, width - 80), -40, 80, 50, randint(1, 2))
                ufos.add(ufo)

        # Wining condition
        if score >= goal:
            finish = True
            window.blit(win_text, (width // 2 - win_text.get_width() // 2, height // 2 - win_text.get_height() // 2))
            display.update()
            time.delay(2000) # Pause for 2 seconds before restarting
            show_game_over_menu = True


        # Losing condition (missed > 3 or player collides with an enemy)
        if missed > 3 or sprite.spritecollide(rocket, ufos, False):
            lives -= 1
            if lives <= 0:
                finish = True
                show_game_over_menu = True
            else:
                finish = True
                window.blit(lose_text, (width // 2 - lose_text.get_width() // 2, height // 2 - lose_text.get_height() // 2))
                display.update()
                time.delay(2000)
                restart_game()
    
    if show_game_over_menu:
        show_game_over_menu = False
        game_over_menu()  # safe now, called before quitting
        restart_game(full_restart=True)
        finish = False

    # Update
    display.update()
    clock.tick(FPS)

pygame.quit()
