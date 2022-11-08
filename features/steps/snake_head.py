from behave import *

@given('the snake')
def step_iplm(context):
    context.snake = {'length': 1, 'position': {'y': 2, 'x':1}}
    context.apple = {'position': {'y': 2, 'x':1}}

@when('the snakes head run into the apple')
def step_impl(context):
    if context.snake['position'] == context.apple['position']:
        tmp_len = context.snake['length']
        context.snake['length'] = tmp_len+1

@then('then the snake will get longer')
def step_implcontext(context):
    assert(context.snake['length'] == 2)
    