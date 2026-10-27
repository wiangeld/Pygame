import pygame
import random

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)


MAX_ALLOWED_ENEMIES = 10;
ENEMY_HEALTH = 100;

Enemies = [];

def SpawnEnemy():
    screen_width = screen.get_width()
    screen_height = screen.get_height()

    attacker_pos = pygame.Vector2(
        random.randint(0, screen_width),
        random.randint(0, screen_height)
    );

    Enemies.append({
        'position': attacker_pos,
        'health': ENEMY_HEALTH
    });
    
 
for i in range(10):
    SpawnEnemy()


def checkCircleCollision(c1, c2):
    dx = c1.x - c2.x;
    dy = c1.y - c2.y;
    distanceSquared = dx * dx + dy * dy;
    radiusSum = 40 + 40;
    return distanceSquared <= radiusSum * radiusSum;


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")


    player_avatar = pygame.draw.circle(screen,"Red", player_pos, 40)
    keys = pygame.key.get_pressed()

    if (keys[pygame.K_w]):
        player_pos.y -= 300 * dt
    elif (keys[pygame.K_s]):
        player_pos.y += 300 * dt
    elif (keys[pygame.K_d]):
        player_pos.x += 300 * dt
    elif (keys[pygame.K_a]):
        player_pos.x -= 300 * dt

    for i in range(len(Enemies) - 1, -1, -1):
        enemy = Enemies[i];
        position = enemy['position']
        
        attacker_avatar = pygame.draw.circle(screen, "Blue", position, 40);
        position.move_towards_ip(player_pos, 4.0)
        
        if (enemy['health'] <= 0):
            Enemies.pop(i);
            SpawnEnemy();
    
    if (keys[pygame.K_SPACE]):
        for enemy in Enemies:
                        
            enemyPosition = enemy['position'];

            isColliding = checkCircleCollision(enemyPosition, player_pos);
            if (isColliding):
                enemy['health'] -= 10
  
    pygame.display.flip()
    dt = clock.tick(60) / 1000
    clock.tick(60)  # limits FPS to 60

pygame.quit()
