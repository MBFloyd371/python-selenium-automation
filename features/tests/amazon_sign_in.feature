
Feature: Test for amazon search

  Scenario: User can search for Sign in page
    Given Open Amazon page
    When Click orders
    Then Verify Sign in label visible and email input field present
