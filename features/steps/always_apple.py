from behave import *

@given('the game')
def step_iplm(context):
    context.game = {'is_apple': False, 'is_active': False}

@when('the game is active')
def step_impl(context):
    if context.game:
        context.game['is_active'] = True 
        context.game['is_apple'] = True 

@then('there will always be an apple in the game')
def step_implcontext(context):
    assert(context.game['is_active'] is True)
    assert(context.game['is_apple'] is True)