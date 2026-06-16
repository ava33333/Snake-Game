import time
 
import pygame
 
import random
 
# initilizes pygame modules and fonts
 
pygame.init()
pygame.font.init()
 
# initilizes colors
white = (250, 250, 250)
red = (255, 102, 102)
orange = (255, 178, 102)
yellow = (255, 255, 102)
green = (178, 255, 102)
darkgreen = (0, 255, 0)
blue = (51, 153, 255)
purple = (153, 153, 255)
black = (0, 0, 0)
 
# colorList = [yellow, green, darkgreen, blue, purple, red, orange]
# purple color list: colorList = [(71, 50, 255), (85, 50, 230), (98, 50, 235), (112, 50, 240), (126, 50, 245), (139, 50, 250), (153, 50, 255)]

# blue color list: 
colorList = [(51, 153, 255), (51, 136, 230), (51, 119, 204), (51, 102, 179), (51, 85, 153), (51, 68, 128), (51, 51, 102)]
 
# makes screen (500x500)
display_surface = pygame.display.set_mode((500, 500))
 
# sets caption for screen
pygame.display.set_caption("Snake")
 
# font and size settings
font = pygame.font.Font(None, 32)
font2 = pygame.font.SysFont('comicsansms', 72)
font3 = pygame.font.SysFont('comicsansms', 48)
font4 = pygame.font.SysFont('comicsansms', 32)
 
# initilizes points to 0
points = 0
 
# creates text variable for points (needs to be written after points var initilized)
text = font.render(f"Points: {points}", True, white, black)
 
# creates text variables (to be called later)
# "text", True, color
intro_text = font.render('Select an Option to Begin', True, white)
snake_intro = font2.render('SNAKE', True, white)
outro_text = font.render('Press Space to Exit', True, white)
over_text = font3.render('GAME OVER', True, white)
points_text = font.render(f"You got {points} points.", True, white)

# speed option text
mode1 = font4.render('Slow', True, blue)
mode2 = font4.render('Medium', True, blue)
mode3 = font4.render('Fast', True, blue)
 
#initial apple positions
ax1 = 200
ax2 = 220
ay1 = 200
ay2 = 220
 
#body of snake
body = [[240, 240, 260, 260]]
 
#movements
movelist = [[-20, 0]]
 
movelist2 = [[220, 240, 240, 260]]
 
def intro_snake():
        # Define the coordinates for the pentagon, offset by (x, y)
        snake_head_points = [(220, 220),  # Bottom-left
                             (280, 220),  # Bottom right
                             (280, 280),  # Top-right
                             (250, 310),  # Apex
                             (220, 280)]  # Top-left
 
        # Draw the pentagon head 
        pygame.draw.polygon(display_surface, blue, snake_head_points)
 
        # Draw the snake's eyes (two white circles)
        pygame.draw.circle(display_surface, white, (238, 270), 10)
        pygame.draw.circle(display_surface, white, (262, 270), 10)
 
        # Draw the snake's pupils (two black circles)
        pygame.draw.circle(display_surface, black, (238, 276), 6)
        pygame.draw.circle(display_surface, black, (262, 276), 6)
 
#changes coords of the square
def movement():
        for i in range(len(body)):
                moveVar = int(i) * -1 #- 1
                if i == 0: #x1:0 y1:1 x2:2 y2:3
                        body[i][0] += movelist[-1][0]
                        body[i][1] += movelist[-1][1]
                        body[i][2] += movelist[-1][0]
                        body[i][3] += movelist[-1][1]
                        movelist2.append([body[i][0], body[i][1], body[i][2], body[i][3]])
                else:
                        body[i][0] = movelist2[moveVar][0]
                        body[i][1] = movelist2[moveVar][1]
                        body[i][2] = movelist2[moveVar][2]
                        body[i][3] = movelist2[moveVar][3]
 
                pygame.draw.polygon(display_surface, colorList[(i + 1) % 7], [(body[i][0], body[i][1]),
                                                                              (body[i][0], body[i][3]),
                                                                              (body[i][2], body[i][3]),
                                                                              (body[i][2], body[i][1])])
 
 
        #draws apple and snake and updates screen
 
        pygame.draw.polygon(display_surface, red, [(ax1, ay1), (ax1, ay2), (ax2, ay2), (ax2, ay1)])
 
        pygame.display.update()
 
#makes a new apple in a new spot
def newApple():
        # calls global variables
        global points, ax1, ax2, ay1, ay2, text, points_text
 
        # increments points each time function is called
        points += 1
 
        # updates points text each time function is called
        # so that every time the snake eats an apple, a point is added
        text = font.render(f"Points: {points}", True, white, black)
        
        # updates point count for game over screen
        points_text = font.render(f"You got {points} points", True, white, black)
 
        #so apple keeps moving to a new position until it is NOT the same as the snake
        randomVar = True
        while randomVar == True:
                randomAy = random.randint(10, 440)
                randomAx = random.randint(10, 440)
                if randomAy % 20 == 0 or randomAx % 20 == 0:
                        randomVar = False
 
        ax1 = randomAx
        ax2 = randomAx + 20
        ay1 = randomAy
        ay2 = randomAy + 20 
 
        movelistvar = (len(body) + 1) * -1
 
        #x1:0 y1:1 x2:2 y2:3
 
        #adding new segment to body
        new0 = body[-1][0] - movelist[movelistvar][0]
        new1 = body[-1][1] - movelist[movelistvar][1]
        new2 = body[-1][2] - movelist[movelistvar][0]
        new3 = body[-1][3] - movelist[movelistvar][1]
        body.append([new0, new1, new2, new3])
 
        #draws apple
        pygame.draw.polygon(display_surface, red, [(ax1, ay1), (ax1, ay2), (ax2, ay2), (ax2, ay1)])
 
        #draws text
        display_surface.blit(text, (0, 450))
 
def gameOver():
        global font, text, points
 
        # initilizes variable to true boolean
        gameOverActive = True
 
        # the loop is entered while var is true
        while gameOverActive == True:
                # makes the screen black
                display_surface.fill(black)
 
                # goes through pygame events
                for event in pygame.event.get():
                        # checks if the x is hit
                        # exits game if it is
                        if event.type == pygame.QUIT:
                                pygame.quit()
 
                        # checks if space is keydown is pressed
                        elif event.type == pygame.KEYDOWN:
                                # exits while loop
                                gameOverActive = False
 
                # displays our text (GAME OVER)
                display_surface.blit(over_text, (120, 140))
                # displays our text (You got X points.)
                display_surface.blit(points_text, (155, 400))
                # displays our text (Press Space to Exit the Game)
                display_surface.blit(outro_text, (150, 450))
 
                # puts our intro snake drawing on the screen
                intro_snake()
 
                # changes display
                pygame.display.flip()
                time.sleep(0.1)
 
        # exits once loop is also exited     
        pygame.quit()
 
 
#runs game
def snake():
    global gameActive, body, movelist, ax1, ay1, ax2, ay2
 
    # evalutes variable as false
    # stops the second loop from entering
    # until our intro screen is done
    gameActive = False 
 
    # Intro screen loop
    intro_screen = True
    while intro_screen:
        # goes through pygame events
        for event in pygame.event.get():
 
                # if red x is hit
                if event.type == pygame.QUIT:
                        # exits loop/closes game
                        pygame.quit()
                        return
 
                elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1: # left mouse button
                                x , y = pygame.mouse.get_pos()
                                print(f"mouse clicked at {x} , {y}")
                                if 50 <= x <= 150 and 300 < y < 400:
                                        sleepVar = 0.2
                                elif 160 <= x <= 275 and 300 < y < 400:
                                        sleepVar = 0.15
                                elif 300 <= x <= 450 and 300 < y < 400:
                                        sleepVar = 0.075
                                        
                                intro_screen = False
                                gameActive = True
 
                # Draw the intro screen
                display_surface.fill(black)
 
                # intro text (Press Space to Start the Game)
                display_surface.blit(intro_text, (135, 450))
                # intro text (SNAKE)
                display_surface.blit(snake_intro, (120, 100))
                
                # speed options text
                display_surface.blit(mode1, (100, 350))
                display_surface.blit(mode2, (200, 350))
                display_surface.blit(mode3, (350, 350))
 
                # Show snake drawing
                intro_snake()
 
                # changes display
                pygame.display.flip()
                time.sleep(0.1)  # Slow down the loop so it's not too fast
 
        # gameplay loop
        while gameActive == True:
 
                #makes screen black
                display_surface.fill(black)
                pygame.display.flip()
 
                #displays our points text
                display_surface.blit(text, (0, 450))
 
                #checks if snake coords is overlapping with apple
                for i in range(len(body)):
                        if 20 > abs((body[i][0] + body[i][2])/2 - (ax1 + ax2)/2) >= 0 and 20 > abs((body[i][1] + body[i][3])/2 - (ay1 + ay2)/2) >= 0 :
                                newApple() # runs new apple function if apple is "eaten"

                
                # increments speed by changning sleepVar (decreasing makes it faster)
                # goes by 10s, if not a value of 10 it stays the same
                if points == 10:
                        sleepVar -= 0.003
                elif points == 20:
                        sleepVar -= 0.003
                elif points == 30:
                        sleepVar -= 0.003
                elif points == 40:
                        sleepVar -= 0.003
                elif points == 50:
                        sleepVar -= 0.003
                else:
                        sleepVar = sleepVar
                        
                #checks if hitting border
                for i in range(len(body)):
                        if body[i][0] == 0 or body[i][2] == 500 or body[i][1] == 0 or body[i][3] == 500:
                                gameOver() # runs gameOver function if true
 
                for event in pygame.event.get():
                        #quits if red x button hit
                        if event.type == pygame.QUIT:
                                pygame.quit()
 
                        #changes xchange or ychange variables (which impact how the snake
                        #is moved each while loop
                        elif event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_UP: # up key
                                        movelist.append([0, -20])
 
                                elif event.key == pygame.K_DOWN: # down key
                                        movelist.append([0, 20])
 
                                elif event.key == pygame.K_RIGHT: # right key
                                        movelist.append([20, 0])
 
                                elif event.key == pygame.K_LEFT: # left key
                                        movelist.append([-20, 0])
 
                #changes coords of snake
                movement()
 
                #checks for collison between head and body
                for i in range(len(body) - 1):
                        if i != 0 and len(body) - 1 > 2:
                                if len(body) > 3 and body[0][0] == body[i+1][0] and body[0][1] == body[i+1][1] and body[0][2] == body[i+1][2] and body[0][3] == body[i+1][3]:
                                        gameOver() # runs game over function if true
 
                #waits before moving again
                # uses our sleepVar from above to control the speed
                time.sleep(sleepVar)
 
                # changes display
                pygame.display.flip()
 
 
 
def main():
        snake()
 
main()
