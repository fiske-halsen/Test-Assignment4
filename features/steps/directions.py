from behave import *

@given('the direction is up')
def step_iplm(context):
    context.key_pressed = 'key up'

@when('the direction up is choosen')
def step_impl(context):
    if context.key_pressed == 'key up':
        context.key = 'up'
        context.state = True

@then('the snake will move upwards infinite')
def step_implcontext(context):
    assert(context.state is True)

#-------------------------------------------

@given('the direction is down')
def step_iplm(context):
    context.key_pressed = 'key down'

@when('the direction down is choosen')
def step_impl(context):
    if context.key_pressed == 'key down':
        context.key = 'down'
        context.state = True

@then('the snake will move downwards infinite')
def step_implcontext(context):
    assert(context.state is True)

#-------------------------------------------

@given('the direction is left')
def step_iplm(context):
    context.key_pressed = 'key left'

@when('the direction left is choosen')
def step_impl(context):
    if context.key_pressed == 'key left':
        context.key = 'left'
        context.state = True

@then('the snake will move leftwards infinite')
def step_implcontext(context):
    assert(context.state is True)

#-------------------------------------------

@given('the direction is right')
def step_iplm(context):
    context.key_pressed = 'key right'

@when('the direction right is choosen')
def step_impl(context):
    if context.key_pressed == 'key right':
        context.key = 'right'
        context.state = True

@then('the snake will move rightwards infinite')
def step_implcontext(context):
    assert(context.state is True)