# Alien-Killer-Python-game
A retro-style 2D space shooter where you control a spaceship to fight off waves of descending aliens. Built from scratch using Python and Pygame. Features smooth movement, bullet mechanics, collision detection, a scoring system with high score tracking, multiple lives, and progressively harder levels.
# 👾 Alien Killer

A classic 2D space shooter game built with Python and Pygame. Defend Earth by shooting down waves of aliens before they reach the bottom of the screen!

## About

Alien Invasion is a retro-style arcade game where you control a spaceship at the bottom of the screen. Waves of aliens march across and down the screen — your job is to shoot them all before they reach you. Each wave you survive gets faster and harder, so stay sharp!

## Features

-  **Smooth ship movement** — Move left and right with arrow keys
-  **Shooting mechanics** — Fire bullets with the spacebar (up to 5 on screen)
-  **Alien fleet** — Rows of aliens that move across and drop down the screen
-  **Collision detection** — Bullets destroy aliens, aliens can hit your ship
-  **Lives system** — You get 3 lives per game
-  **Scoring** — Earn points for each alien destroyed
-  **High score** — Tracks your best score during the session
-  **Levels** — Difficulty increases with each wave you clear
-  **Play button** — Click to start or restart the game

## Prerequisites

- Python 3.12
- Pygame

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/MudassirAbbas/alien-invasion.git
   cd alien-invasion
   ```

2. **Install Pygame**
   ```bash
   pip install pygame
   ```

3. **Run the game**
   ```bash
   python alien_invasion.py
   ```

## How to Play

| Key | Action |
|-----|--------|
| `←` `→` | Move ship left / right |
| `Space` | Fire bullet |
| `Q` | Quit the game |
| `Mouse Click` | Click the Play button to start |

### Rules

- Shoot all the aliens to advance to the next level
- Each new level makes the aliens faster
- You lose a life if an alien hits your ship or reaches the bottom of the screen
- The game ends when you run out of lives
- Click "Play" to start a new game

## Project Structure

```
alien-invasion/
├── alien_invasion.py    # Main game loop and logic
├── settings.py          # Game configuration and difficulty scaling
├── ship.py              # Player ship class
├── alien.py             # Alien sprite class
├── bullet.py            # Bullet sprite class
├── game_stats.py        # Score, lives, and level tracking
├── scoreboard.py        # On-screen score display
├── button.py            # Play button UI
├── Ship.bmp             # Ship sprite image
└── README.md
```

## Built With

- [Python](https://www.python.org/) — Programming language
- [Pygame](https://www.pygame.org/) — Game development library

## License

This project is open source and available under the [MIT License](LICENSE).
