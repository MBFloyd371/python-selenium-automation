Feature: Tests for product page

  Scenario: User can hover product features
    Given Open Amazon product B074TBCSC8 page
    When Hover on New Arrivals
    Then Verify deals exist