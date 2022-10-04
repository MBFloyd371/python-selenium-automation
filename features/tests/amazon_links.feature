Feature: Test for amazon best sellers

  Scenario: Heads links has the right amount of links
    Given Open Amazon page
    Then Verify That Header has 5 links
