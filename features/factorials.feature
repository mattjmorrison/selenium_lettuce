Feature: Compute factorial
	In order to play with lettuce
	As beginners
	We'll implement factorial

	Scenario: Factorial Calculations
		Given I have the number <number>
		When I compute this factorial
		Then I see the number <factorial>
	
	Examples:
		| number	| factorial	|
		| 0		| 1		|
		| 1		| 1		|
		| 2		| 2		|
		| 3		| 6		|
		| 4		| 24		|

