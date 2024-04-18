from pytest_bdd import scenario, scenarios, given, when, then


@scenario('initial.feature', 'Login Verification')
def test_def_init():
    pass

@given('As User')
def as_user():
    assert 3 == 3


@given('using Client')
def using_client():
    assert 2 == 2