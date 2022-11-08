Feature: 
    The snake dies if its runs into its own body, or a wall (if your game has walls).
    If the game dosent have walls, the snake should wrap around (like in Pacman)

    Scenario: snake hits itself
        Given the game has walls
        When the snakes head run into the wall
        Then the snake dies

    Scenario: snake hits itself
        Given the game has no walls
        When the snakes head run into its own body
        Then the snake diess