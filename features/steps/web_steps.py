import time
from lettuce import step, before, after, world
from selenium import webdriver

@before.all
def setup_environ():
	profile = webdriver.FirefoxProfile()
	world.browser = webdriver.Firefox(firefox_profile=profile)

@after.all
def teardown_environ(arg):
	world.browser.close()

@step(u'Given I am on "(.+)"')
def given_i_am_on_google_s_home_page(step, url):
	world.browser.get(url)

@step(u'When I type "(.*)" in the "(.*)" field')
def when_i_type_text_in_field(step, text, field):
	input_field = world.browser.find_element_by_css_selector('[name=%s]' % field)
	input_field.send_keys(text)

@step(u'Then I should see a link that contains "(.+)", "(.+)" and "(.+)"')
def then_i_see_group1_in_the_results(step, result_one, result_two, result_three):
	time.sleep(5) # wait for search to complete
	matches = world.browser.find_elements_by_partial_link_text(result_one)

	assert len(matches) > 0, "No matching elements"

	for match in matches:
		if result_one in match.text and result_two in match.text and result_three in match.text:
			break
	else:
		message = "%s and %s" % (result_one, result_two) + " not found in " + ', '.join(match.text for match in matches)
		assert False, message
