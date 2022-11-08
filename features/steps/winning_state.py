from behave import *

@given('the snakess')
def step_iplm(context):
    context.snake = {'length': 2, 'position': {'y': 2, 'x':1}}
    context.game = {'length': 1}

@when('the snake runs out of space')
def step_impl(context):
    context.isOutOfSpace = False
    if context.snake['length'] >= 1: #Context did not work here for some reason
        context.isOutOfSpace = True

@then('then the game is won')
def step_implcontext(context):
    assert(context.isOutOfSpace is True)
    