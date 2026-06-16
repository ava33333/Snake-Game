# Snake Game

A graphical Snake game built with Python and pygame. This was a group project for an introductory Computer Science course at the College of Charleston.

## About

The game runs in a 500x500 pygame window and features three speed modes (Slow, Medium, Fast) selectable from an intro screen. The snake is rendered as a chain of colored polygon segments that follow the head's movement history, and grows each time it eats an apple. The game ends when the snake collides with a wall or itself.

Key features:
- Animated snake with a custom pentagon-shaped head and color-gradient body
- - Random apple placement
  - - Score tracking
    - - Game over and restart screen
     
      - ## Files
     
      - | File | Description |
      - |------|-------------|
      - | `snake_game.py` | Final version — fully playable game with pygame |
      - | `snake_game_draft.py` | Early draft — initial snake head rendering and movement logic using the `graphics.py` library |
     
      - ## Dependencies
     
      - - Python 3
        - - pygame
         
          - Install pygame with:
          - ```
            pip install pygame
            ```

            ## How to Run

            ```
            python snake_game.py
            ```

            Use the arrow keys to control the snake. Select a speed mode from the intro screen to begin.

            ## Course

            Intro to Computer Science | College of Charleston
