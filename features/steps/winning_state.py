from behave import *

@given('the snake2')
def step_iplm(context):
    context.snake = {'squaremeter': 2, 'position': {'y': 2, 'x':1}}
    context.game = {'squaremeter': 1}

@when('the snake runs out of space')
def step_impl(context):
    context.isOutOfSpace = False
    if context.snake['squaremeter'] >= context.game['squaremeter']:
        context.isOutOfSpace = True

@then('then the game is won')
def step_implcontext(context):
    assert(context.isOutOfSpace is True)
    