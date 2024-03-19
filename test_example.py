from pytest_bdd import scenario, given, when, then
import json
@scenario("example.feature", "Login page")
def test_scenario():
    pass

@given(u'User')
def test_step_impl():
    with open("resources/variables.json", "r") as f:
        data = json.load(f)
        user_name = "admin"
        user_password = data["users"][user_name]


    #raise NotImplementedError(u'STEP: Given User')

#
# @given(u'URL to Navigate')
# def step_impl():
#     pass
#     #raise NotImplementedError(u'STEP: Given URL to Navigate')
#
#
# @when(u'I open URL')
# def step_impl():
#     pass
#     #raise NotImplementedError(u'STEP: When I open URL')
#
#
# @when(u'I till <login>')
# def step_impl():
#     pass
#     #raise NotImplementedError(u'STEP: When I till <login>')
#
#
# @when(u'I till <password>')
# def step_impl():
#     pass
#     #raise NotImplementedError(u'STEP: When I till <password>')
#
#
# @when(u'I press the login button')
# def step_impl():
#     pass
#     #raise NotImplementedError(u'STEP: When I press the login button')
#
#
# @then(u'I check message on top of page')
# def step_impl():
#     pass
#     #raise NotImplementedError(u'STEP: Then I check message on top of page')
