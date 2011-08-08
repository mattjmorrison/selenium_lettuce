Feature: Google My Blog
	In order to find my blog
	As a Google fanboy
	I want to find see my Google juice

	Scenario: Find my agile blog with google instant search
		Given I am on "http://www.google.com"
		When I type "My Crusade for Agility" in the "q" field
		Then I should see a link that contains "mattjmorrison", "My Crusade for Agility" and "Part 1"
		
