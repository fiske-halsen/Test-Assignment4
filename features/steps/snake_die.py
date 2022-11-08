from behave import *

@given('the game has walls')
def step_iplm(context):
    context.game = {'wall': {'width': 400, 'height': 600}}  
    context.snake = {'position': {'xWidth': 450 , 'yHeight': 550 }}

@when('the snakes head run into the wall')
def step_impl(context):
    isHit = False
    if context.snake['position']['xWidth'] >= context.game['wall']['width']:
        isHit = True
    elif context.snake['position']['yWidth'] >= context.game['wall']['height']:
        isHit = True
    context.isHit = isHit

@then('the snake dies')
def step_implcontext(context):
    assert(context.isHit is True)


@given('the game has no walls')
def step_iplm(context):
    context.snakeHead = {'position': {'xWidth': 450 , 'yHeight': 550 }}
    context.snakeTail = {'position': {'xWidth': 450 , 'yHeight': 550 }}

@when('the snakes head run into its own body')
def step_impl(context):
    isHit = False
    if context.snakeHead['position'] == context.snakeTail['position']:
        isHit = True
    context.isHit = isHit

@then('the snake diess')
def step_implcontext(context):
    assert(context.isHit is True)