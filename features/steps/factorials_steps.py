from lettuce import step, world

@step(u'Given I have the number (.+)')
def given_i_have_the_number(step, number):
	world.number = int(number)

@step(u'When I compute this factorial')
def when_i_compute_this_factorial(step):
	world.number = factorial(world.number)

@step(u'Then I see the number (.+)')
def then_i_see_the_number(step, number):
	expected = int(number)
	assert world.number == expected, "Got %d" % world.number 



def factorial(number):
	if number in (0, 1):
		return 1
	return number * factorial(number - 1)
