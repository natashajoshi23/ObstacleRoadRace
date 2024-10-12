import pygame, sys, time, random 


pygame.init()


screenW = 500
screenH = 700


screen = pygame.display.set_mode((screenW, screenH))
pygame.display.set_caption('Car Racers')


bg = pygame.image.load('road.png')
bg = pygame.transform.scale(bg, (500, 700))
xpos = 0
ypos = 0


start_line = pygame.image.load('finish line.png')
start_line = pygame.transform.scale(start_line, (330, 50))
startX = 85
startY = 80


car = pygame.image.load('car.png')
car = pygame.transform.scale(car, (55, 90))
sx = 260
sy = 580
direction = 1
speed = 0


tire = pygame.image.load('tire.png')
tire = pygame.transform.scale(tire, (30, 30))
ty = -300
tx = -600
tSpeed = .3


# Set initial background position
background_y = 0


# Set background speed
background_speed = 2


# set the start screen flag
start_screen = True
game_over = False


obstacle = pygame.image.load('obstacle.png')
obstacle_width = 50
obstacle_height = 70
obstacle = pygame.transform.scale(obstacle, (obstacle_width, obstacle_height))
obstacle_x = random.randint(83, 360)
obstacle_y = -obstacle_height
obstacle_speed = 4


obstacle2 = pygame.image.load('obstacle.png')
obstacle2_width = 50
obstacle2_height = 70
obstacle2 = pygame.transform.scale(obstacle2, (obstacle2_width, obstacle2_height))
obstacle2_x = random.randint(83, 360)
obstacle2_y = -obstacle_height
obstacle2_speed = 3


obstacle3 = pygame.image.load('obstacle.png')
obstacle3_width = 50
obstacle3_height = 70
obstacle3 = pygame.transform.scale(obstacle3, (obstacle3_width, obstacle3_height))
obstacle3_x = random.randint(83, 360)
obstacle3_y = -obstacle3_height
obstacle3_speed = 5


# sounds
obstacle_sound = pygame.mixer.Sound("obstacle sound.wav")
tires_sound = pygame.mixer.Sound("tire sound.wav")
countdown_sound = pygame.mixer.Sound("countdown sound.wav")
winning_sound = pygame.mixer.Sound("winning sound.wav")


# Function to check collision
def check_collision(car_x, car_y, car_width, car_height, obstacle_x, obstacle_y, obstacle_width, obstacle_height):
   if car_x < obstacle_x + obstacle_width and car_x + car_width > obstacle_x and car_y < obstacle_y + obstacle_height and car_y + car_height > obstacle_y:
       return True
   return False




# Function to check if the car reaches the finish line
def check_win(car_y, start_line_y):
   if car_y <= start_line_y:
       return True
   return False




# Start screen loop
while start_screen:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           start_screen = False
           game_over = True
       if event.type == pygame.KEYDOWN:
           start_screen = False


   # Draw the start screen
   screen.fill((0, 0, 0))
   font1 = pygame.font.SysFont('comic sans', size=45)
   font2 = pygame.font.SysFont('comic sans', size=30)
   font3 = pygame.font.SysFont('comic sans', size=15)
   title = font1.render("Obstacle Road Rush", True, (255, 255, 255))
   message = font2.render("Press Any Key To Start", True, (255, 255, 255))
   name = font3.render("Created By Natasha", True, (255, 255, 255))
   start_text_rect = title.get_rect(center=(screenW / 2, 295))
   screen.blit(title, start_text_rect)
   start_text_rect2 = message.get_rect(center=(screenW / 2, 365))
   screen.blit(message, start_text_rect2)
   start_text_rect3 = name.get_rect(center=(410, 680))
   screen.blit(name, start_text_rect3)
   pygame.display.update()


# Game loop
running = True
clock = pygame.time.Clock()




def show_game_over_screen():
   screen.fill((0, 0, 0))
   font4 = pygame.font.SysFont('comic sans', size=60)
   text3 = font4.render(f"GAME OVER!!", True, (255, 255, 255), None)
   text3_rect = text3.get_rect(center=(screenW / 2, 310))
   screen.blit(text3, text3_rect)
   font5 = pygame.font.SysFont('comic sans', 30)
   text4 = font5.render(f"You lost :(", True, (255, 255, 255), None)
   text4_rect = text4.get_rect(center=(screenW / 2, 400))
   screen.blit(text4, text4_rect)
   pygame.display.update()
   time.sleep(5)




def show_win_screen():
   pygame.mixer.Sound("winning sound.wav")
   screen.fill((0, 0, 0))
   font4 = pygame.font.SysFont('comic sans', size=60)
   text3 = font4.render(f"GAME OVER!!", True, (255, 255, 255), None)
   text3_rect = text3.get_rect(center=(screenW / 2, 310))
   screen.blit(text3, text3_rect)
   font5 = pygame.font.SysFont('comic sans', 30)
   text4 = font5.render(f"You win!", True, (255, 255, 255), None)
   text4_rect = text4.get_rect(center=(screenW / 2, 400))
   screen.blit(text4, text4_rect)
   pygame.display.update()
   time.sleep(5)



def countdown(n):
   while n > 0:
       pygame.mixer.Sound("countdown sound.wav")
       screen.fill((0, 0, 0))
       font = pygame.font.SysFont('comic sans', size=70)
       text = font.render(str(n), True, (255, 255, 255))
       text_rect = text.get_rect(center=(250, 350))
       screen.blit(text, text_rect)
       pygame.display.flip()


       time.sleep(1)  # Wait for 1 second
       n -= 1

   pygame.mixer.Sound("countdown sound.wav")
   screen.fill((0, 0, 0))
   font1 = pygame.font.SysFont('comic sans', size=70)
   text = font1.render("Go!", True, (255, 255, 255))
   text_rect = text.get_rect(center=(250, 350))
   screen.blit(text, text_rect)
   pygame.display.flip()
   time.sleep(1)  # Wait for 2 seconds before closing the window



countdown(3)


while running:
   # Handle events
   clock.tick(60)
   for e in pygame.event.get():
       if e.type == pygame.QUIT:
           running = False
       elif e.type == pygame.KEYDOWN:
           if e.key == pygame.K_RIGHT:
               speed += 4
           elif e.key == pygame.K_LEFT:
               speed -= 4
           elif e.key == pygame.K_UP:
               sy -= 5
           elif e.key == pygame.K_SPACE and ty < 0:
               tx = sx
               ty = sy
               tSpeed = -5
           elif e.key == pygame.K_DOWN:
               sy += 4
       elif e.type == pygame.KEYUP:
           if e.key == pygame.K_RIGHT:
               speed -= 4
           elif e.key == pygame.K_LEFT:
               speed += 4


   # Move the background
   background_y += background_speed


   # Reset the background position if it goes off the screen
   if background_y >= screenH:
       background_y = 0


   # Move the car
   sx += direction * speed
   if sx > 360:
       sx = 360
   if sx < 83:
       sx = 83
   if sy < 0:
       sy = 0
   ty += tSpeed




   # Move the obstacles
   obstacle_y += obstacle_speed
   if obstacle_y > screenH:
       obstacle_x = random.randint(100, 360)
       obstacle_y = -obstacle_height


   obstacle2_y += obstacle2_speed
   if obstacle2_y > screenH:
       obstacle2_x = random.randint(100, 360)
       obstacle2_y = -obstacle_height


   obstacle3_y += obstacle3_speed
   if obstacle3_y > screenH:
       obstacle3_x = random.randint(100, 360)
       obstacle3_y = -obstacle3_height


   # Check for collision
   if check_collision(sx, sy, car.get_width(), car.get_height(), obstacle_x, obstacle_y, obstacle.get_width(), obstacle.get_height()):
       pygame.mixer.Sound("obstacle sound.wav")
       game_over = True
       break


   if check_collision(sx, sy, car.get_width(), car.get_height(), obstacle2_x, obstacle2_y, obstacle2.get_width(), obstacle2.get_height()):
       pygame.mixer.Sound("obstacle sound.wav")
       game_over = True
       break


   if check_collision(sx, sy, car.get_width(), car.get_height(), obstacle3_x, obstacle3_y, obstacle3.get_width(), obstacle3.get_height()):
       pygame.mixer.Sound("obstacle sound.wav")
       game_over = True
       break


   # Check if the car reaches the finish line
   if check_win(sy, startY):
       running = False
       break


   # Check for collision with obstacles
   if check_collision(tx, ty, tire.get_width(), tire.get_height(), obstacle_x, obstacle_y, obstacle.get_width(), obstacle.get_height()):
       pygame.mixer.Sound("tire sound.wav")
       obstacle_x = random.randint(100, 360)
       obstacle_y = -obstacle_height


   if check_collision(tx, ty, tire.get_width(), tire.get_height(), obstacle2_x, obstacle2_y, obstacle2.get_width(), obstacle2.get_height()):
       pygame.mixer.Sound("tire sound.wav")
       obstacle2_x = random.randint(100, 360)
       obstacle2_y = -obstacle_height


   if check_collision(tx, ty, tire.get_width(), tire.get_height(), obstacle3_x, obstacle3_y, obstacle3.get_width(), obstacle3.get_height()):
       pygame.mixer.Sound("tire sound.wav")
       obstacle3_x = random.randint(100, 360)
       obstacle3_y = -obstacle3_height


   # Display
   screen.blit(bg, (0, background_y))
   screen.blit(bg, (0, background_y - screenH))
   screen.blit(start_line, (startX, startY))
   screen.blit(car, (sx, sy))
   screen.blit(tire, (tx, ty))
   screen.blit(obstacle, (obstacle_x, obstacle_y))
   screen.blit(obstacle2, (obstacle2_x, obstacle2_y))
   screen.blit(obstacle3, (obstacle3_x, obstacle3_y))
   pygame.display.update()


# Game over screen
if game_over:
   show_game_over_screen()


# Win screen
if not game_over:
   show_win_screen()


pygame.quit()
sys.exit()

