Feature: Amazon Dropdown and Action Chains

  Scenario Outline: User can see department and value
    Given Open Amazon page
    When Select department by value <value>
    And Search for kitchen
    Then Verify <department> department is selected
    Examples:
      | value        | department |
      | pot          | appliances |
      | Harry Potter | books      |