## CS 110 Final Project
Summer, 2020
### [Assignment Description](https://drive.google.com/open?id=1HLIk-539N9KiAAG1224NWpFyEl4RsPVBwtBZ9KbjicE)

https://github.com/bucs110/final-project-summer20-ballmer-s-peak

https://docs.google.com/presentation/d/1k_T_v0HsIlZApdHQ84gtgVn8qB7TyKfM4W5yUh323kk/edit?usp=sharing

### Team: Ballmer's Peak
#### David Esses, Matthew Sadowski, Ron Laniado

***

## Project Description
This game is space invaders-inspired, designed to have quickly increasing difficulty while still remaining fun

***    

## User Interface Design
* << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. >>
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
![class diagram](assets/class_diagram.jpg)

***        

## Program Design
* Non-Standard libraries
   We have not used non standard libraries for this game.
* Class Interface Design
    * Diagram shows the class design in our game
        * ![class diagram](assets/class_diagram.jpg)
* Classes
    - Player Class: the player that can move around the screen and shoot projectiles
    - Enemy Class: the enemy that tries to kill the enemy by moving towards the player and shooting projectiles back
    - Projectile Class: a class that is used by other classes to shoot bullets towards the other side of the screen
    - Controller Class: creates groups of sprites and controls the logic between them

***

## Tasks and Responsibilities
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Ron Laniado

Worked as integration specialist by making sure that each feature was integrated without breaking the rest of the game, creating the ATP, and assisting both the front end and back end specialists

### Front End Specialist - Matthew Sadowski

Front-end lead conducted significant research on implementing the nice visual effects, infinite background, and other important GUI details. 


### Back End Specialist - David Esses

The backend specialist was responsible for creating many classes and implementing the data logic in the controller


## Testing
Our testing strategy was to create features in small chunks and test them manually to make sure they don't break the rest of the game
    * When creating the collision events with the enemy and projectiles, we needed to ensure that the projectiles didn't have side effects against the player or not working as intended

| Step | Procedure                                                          | Expected Results                                                                                                                                                                                                                                                                                                 | Comments |
|------|--------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| 1    | Open terminal, navigate to folder, and type "python3 main.py"      | a. Pygame window opens and the game begins b. Player is displayed on the screen with a score of 0 and 5 lives c. Enemies are displayed on the screen, move towards the player and shoot randomly. If they hit the player, player loses a life                                                                    |          |
| 2    | Press or hold SPACE BAR                                            | Launches bullets towards the enemy. If bullet collide with the enemy, they kill the enemy                                                                                                                                                                                                                        |          |
| 3    | Press or hold RIGHT ARROW/D KEY                                    | Moves the player to the right and changes the sprite to the "ship moving right" image                                                                                                                                                                                                                            |          |
| 4    | Press or hold LEFT ARROW/A KEY                                     | Moves the player to the left and changes the sprite to the "ship moving left" image                                                                                                                                                                                                                              |          |
| 5    | Press or hold UP ARROW/W KEY                                       | Moves the player up                                                                                                                                                                                                                                                                                              |          |
| 6    | Press or hold DOWN ARROW/S KEY                                     | Moves the player down                                                                                                                                                                                                                                                                                            |          |
| 7    | Player pressed the x button on the window or loses all their lives | The game ends and the Pygame window closes                                                                                                                                                                                                                                                                       |          |
| 8    | General Playtesting                                                | a. Bullet go in the correct direction and kill enemies on impact. When they leave the screen, the bullets are destroyed b. When a bullet kills an enemy, the score is increased by 1 b. Player is able to move around easily, and can press multiple keys at the same time (shoot while moving leftwards and up) |          |
