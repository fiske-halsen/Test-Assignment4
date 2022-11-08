Feature: 
    The snake dies if its runs into its own body, or a wall (if your game has walls).
    If the game dosent have walls, the snake should wrap around (like in Pacman)

    Scenario: snake hits itself
        Given the snake
        When the snakes head run into the apple
        Then then the snake will get longer