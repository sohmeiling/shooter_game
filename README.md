## Edit the readme file
📦 Project Title
Space Shooter Game (Pygame)

🧾 Description
A simple 2D shooter game built using Python and Pygame. Players control a rocket ship to shoot down invading UFOs. The game tracks score, missed enemies, and remaining lives, with clear win/lose conditions and a restart/exit menu after game over.

Designed for learning and practice with sprite-based game logic, event handling, collision detection, and basic UI interaction in Pygame.

🎮 Gameplay Mechanics
Use Left / Right arrow keys to move the rocket.

Press Spacebar to shoot bullets upward.

Destroy 10 UFOs to win.

Lose a life when:

A UFO passes the bottom (missed).

The rocket collides with a UFO.

You get 3 lives per game.

After losing all lives or winning, a menu screen appears to restart or exit.

📂 Project Structure
Copy
Edit
shooter_game/
├── rocket.png
├── ufo.png
├── bullet.png
├── heart.png
├── galaxy.jpg
├── space.ogg
├── fire.ogg
├── shooter_game.py
└── README.md
All image and sound assets should be placed in the same directory as shooter_game.py.

▶️ How to Run
Requirements
Python 3.x

Pygame

Installation
bash
Copy
Edit
pip install pygame
Run the game
bash
Copy
Edit
python shooter_game.py
📌 Features
Sprite-based game with player, enemy, and bullet mechanics.

Health/lives indicator using heart icons.

Multiple-hit enemies (each UFO takes 2 hits).

Win/loss detection and scoring system.

Restart/exit menu after game ends.

Background music and shooting sound effects.

🛠️ To-Do / Possible Enhancements
Add difficulty levels (enemy speed increases over time).

Add more enemy types with different behaviours.

Add sound toggle / volume control.

Animate sprites (explosions, ship motion).

Store high scores between sessions.

🧑‍💻 Author
Developed by: Mei Ling Soh

📄 License
This project is for educational use. Please replace or verify usage rights for external assets (e.g., images, sounds) before public distribution.
