Feature: 
    You control the direction of a continuously moving snake
    going up, down, left or right - the snake cannot stop moving.

    Scenario: mooving up
        Given the direction is up
        When the direction up is choosen
        Then the snake will move upwards infinite

    Scenario: mooving down
        Given the direction is down
        When the direction down is choosen
        Then the snake will move downwards infinite

    Scenario: mooving left
        Given the direction is left
        When the direction left is choosen
        Then the snake will move leftwards infinite

    Scenario: mooving right
        Given the direction is right
        When the direction right is choosen
        Then the snake will move rightwards infinite


