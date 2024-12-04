
# Cyber Dash  
#### Video Demo:  [URL HERE]  
#### Description:

Cyber Dash is a 2D side-scrolling pixel game built using Python and the PyGame library. The player controls a character in a futuristic cyberpunk world, where the goal is to dash through obstacles while accumulating points. The game combines traditional platformer mechanics with pixel art to create an engaging, nostalgic gameplay experience that requires reflexes and strategy to achieve a high score.

The project includes several core components:
- **Player Character:** An animated player sprite with realistic jumping mechanics.
- **Obstacles:** Multiple obstacle types (drones and dragons), each with animations and unique movement patterns.
- **Pillars and Ads:** Stationary and moving pillars and ad elements to enhance the cyberpunk setting and add complexity.
- **Scoring System:** Tracks survival time and displays the score dynamically.
- **Sound Effects and Background Music:** Immersive audio to add atmosphere to the cyberpunk theme.
- **User Interface (UI):** A start screen, game-over screen, and in-game instructions for ease of play.

This README provides a thorough breakdown of each file, as well as design decisions that contributed to the final project.

---

### File Descriptions

1. **main.py**
   - The main entry point for the game, containing initialization, event handling, game loop, and rendering functions.
   - Handles player controls, scoring logic, and conditions for resetting the game.
   - Imports other components and ensures smooth transitions between game states (start, active play, and game-over screens).

2. **Player Class (player.py)**
   - The `Player` class defines player behavior, including input handling, gravity, and animation.
   - Provides realistic movement by adjusting gravity in real time, allowing the player to jump and land fluidly.
   - Utilizes an animation sequence for the player’s running and jumping states, giving life to the character and enhancing visual appeal.

3. **Obstacle Classes (obstacle.py)**
   - Drones and dragons add challenge and excitement to the gameplay. Each type has its own speed, animation, and movement pattern.
   - Designed to respawn randomly off-screen, creating a seamless experience where new obstacles appear at intervals.
   - Uses PyGame’s sprite functionality for efficient collision detection and movement.

4. **Pillar Classes (pillar.py)**
   - `MovingPillar` and `MovingPillarAd` add depth to the visual environment. These stationary and moving obstacles don’t affect the player directly but enhance the overall game aesthetic.
   - Ads are used to reinforce the cyberpunk theme with commercial visuals, simulating a bustling urban setting.

5. **assets**
   - `graphics/`: Contains pixel art assets for characters, obstacles, backgrounds, and UI elements.
   - `audio/`: Provides background music and sound effects, with files in `.mp3` format. Background music is looped, and a jump sound effect is triggered when the player jumps.
   - Organizing assets into separate folders ensures modularity, making it easier to update or replace specific assets without affecting the rest of the project.

6. **README.md**
   - This file serves as documentation for the project, explaining its structure and guiding users on how to play the game.

---

### Design Choices

#### Character Animation
Animating the character frame-by-frame allows for smooth transitions between different states. For example, the player’s walking and jumping actions each have distinct animations, lending a polished and dynamic feel. This design choice reinforces the pixel art aesthetic while providing visual feedback that enhances player control.

#### Obstacle Design
To keep the game engaging, obstacles vary in type and behavior. Drones and dragons spawn at random intervals, forcing players to stay alert and react quickly. Dragons move closer to the ground, while drones fly higher, requiring different jumping strategies to avoid each type. The respawning logic ensures a steady stream of obstacles, with gaps that give players opportunities to gather points.

#### Gravity and Jumping Mechanics
Gravity plays an essential role in creating a realistic platforming experience. The `Player` class updates the Y-axis position of the character incrementally, simulating a smooth falling effect. When the player jumps, gravity is momentarily reduced, allowing the character to ascend. This functionality, combined with collision detection, results in a responsive and engaging control scheme.

#### Scoring and Progression
The score increases based on the duration of time survived. This choice encourages players to focus on survival rather than specific goals, such as defeating enemies. By tracking score through time, the game provides an implicit difficulty progression, with longer survival times requiring more skill and attention.

#### Visual and Audio Design
A pixel-art cyberpunk theme was chosen to appeal to fans of retro-style games. The color palette and detailed backgrounds evoke a futuristic city, while background music and sound effects enhance immersion. The jump sound effect reinforces the player’s actions and provides additional feedback. Pillars and ads reinforce the cyberpunk aesthetic and offer an authentic in-game environment.

---

### How to Run the Game

1. **Install PyGame**  
   Run the following command to install PyGame:
   ```bash
   pip install pygame
   ```

2. **Download the Project Files**  
   Clone or download the repository. Ensure all asset folders are in place (e.g., `graphics/`, `audio/`).

3. **Run main.py**  
   In your terminal, navigate to the project folder and execute:
   ```bash
   python main.py
   ```

The game will open in a new window, and you can start playing by following the on-screen instructions.

---

### Known Issues

- **Scaling on Large Displays:** The game is optimized for 800x400 resolution. On larger displays, pixelation may occur, and performance may vary.
- **Collision Detection:** Some collisions may not feel precise due to bounding box detection. Future versions could benefit from pixel-perfect collision handling for a smoother experience.

### Future Enhancements

1. **Difficulty Levels**  
   - Adding selectable difficulty levels would allow players to choose a pace that suits their skill level.

2. **Power-Ups and Collectibles**  
   - Implementing collectibles, such as shields or speed boosts, would provide additional goals and rewards.

3. **Extended Scoring System**  
   - Reward players with bonuses for close calls or perfect jumps to add depth to the scoring system.

4. **Mobile Porting**  
   - With touch-based controls, the game could be adapted for mobile platforms, expanding its accessibility.

---

### Sum up

Cyber Dash encapsulates elements from classic platformers, such as intuitive controls, pixel art, and simple yet challenging mechanics. By focusing on player control, visual appeal, and procedural obstacle generation, the game offers a satisfying experience that grows more challenging over time. This project was a comprehensive exercise in game development fundamentals, including physics, sprite management, and object-oriented programming. Through Cyber Dash, I gained valuable insights into the game development process and applied skills acquired from the CS50x course, setting a foundation for future projects.
