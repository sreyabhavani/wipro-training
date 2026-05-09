# features/pim.feature

Feature: PIM Employee Creation

  Scenario Outline: Add Employee

    When I enter "<FirstName>" and "<LastName>"

    Examples:
      | FirstName | LastName |
      | John      | David    |
      | Ram       | Kumar    |