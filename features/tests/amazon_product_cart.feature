
 Feature: Test for amazon search cart

  Scenario: User can search for Cart page
    Given Open Amazon Books page
    When Click preorder now
    Then Verify results has 1 are shown