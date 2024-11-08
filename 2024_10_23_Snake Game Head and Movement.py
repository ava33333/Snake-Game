from graphics import *
import time

def snakeHead(win):
    # Define the coordinates for the pentagon
    snake_head = Polygon(Point(150, 120),  # Bottom-left
                    Point(250, 120),  # Bottom-right
                    Point(250, 200),  # Top-right
                    Point(200, 250),  # Apex
                    Point(150, 200))   # Top-left
    snake_head.setFill("green")
    snake_head.draw(win)

    snake_eye = Circle(Point(170, 170), 15)
    snake_eye.setFill("white")
    snake_eye.draw(win)

    snake_eye2 = snake_eye.clone()
    snake_eye2.move(60,0)
    snake_eye2.draw(win)

    snake_pupil = Circle(Point(170,176), 9)
    snake_pupil.setFill("black")
    snake_pupil.draw(win)

    snake_pupil2 = snake_pupil.clone()
    snake_pupil2.move(60,0)
    snake_pupil2.draw(win)
    
    snakeFeatures = [snake_head, snake_eye, snake_eye2, snake_pupil, snake_pupil2]

    return snakeFeatures

"""def snakeHeadMovement(snakeHead, win):
    snakeHead = snakeHead(win)
    # moves all snakeHead across screen
    key = win.getKey()

    if key == "Up":
        for features in snakeHead:
            features.move(0, 100)  # Move 1 pixel up
            time.sleep(0.01)
    elif key == "Down":
        for features in snakeHead:
            features.move(0, -100)  # Move 1 pixel down
            time.sleep(0.01)
    elif key == "Left":
        for features in snakeHead:
            features.move(-100, 0)  # Move 1 pixel to the left
            time.sleep(0.01)
    elif key == "Right":
        for features in snakeHead:
            features.move(100, 0)  # Move 1 pixel to the right
            time.sleep(0.01)

    win.getMouse()
    win.close()"""

def snakeHeadMovement(snakeHead, win):
    snakeHead = snakeHead(win)
    # moves all snakeHead across screen
    key = win.getKey()

    head = snakeHead[0]
    points = head.getPoints()

    points_list = []

    for point in points:
        x = point.getX()
        y = point.getY()
        points_list.append(x)
        points_list.append(y)
    
    for points in points_list:
        while (points != 0) and (points != 400):
            if key == "Up":
                for features in snakeHead:
                    features.move(0, 100)  # Move 1 pixel up
                    time.sleep(0.01)
            elif key == "Down":
                for features in snakeHead:
                    features.move(0, -100)  # Move 1 pixel down
                    time.sleep(0.01)
            elif key == "Left":
                for features in snakeHead:
                    features.move(-100, 0)  # Move 1 pixel to the left
                    time.sleep(0.01)
            elif key == "Right":
                for features in snakeHead:
                    features.move(100, 0)  # Move 1 pixel to the right
                    time.sleep(0.01)
            
            head = snakeHead[0]
            points = head.getPoints()

            points_list = []

            for point in points:
                x = point.getX()
                y = point.getY()
                points_list.append(x)
                points_list.append(y)

    win.getMouse()
    win.close()

"""def gamePlay(win):
    snakeHeadMovement(snakeHead, win)
    head = snakeHead(win)
    y_value = head.getY()
    x_value = head.getX()
    win_conditions = True
    while win_conditions == True:
        if (y_value == 0) or (y_value == 400) or (x_value == 0) or (x_value == 0):
            False
        else:
            snakeHeadMovement(snakeHead, win)
            y_value = head.getY()
            x_value = head.getX()"""
        
def main():
    win = GraphWin("Snake head", 700, 700)
    win.setCoords(0, 0 , 400, 400)

    snakeHeadMovement(snakeHead, win)


main()