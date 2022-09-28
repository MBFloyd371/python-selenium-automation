
Feature: Test for amazon search cart

  Scenario: User can search for Cart page
    Given Open Amazon page
    When Click cart
    Then Verify Sign in label visible and email input field present