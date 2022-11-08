Feature: 
    The winning state is to run out of space

    Scenario: Snake runs of out space
        Given the snake2
        When the snake runs out of space
        Then then the game is won