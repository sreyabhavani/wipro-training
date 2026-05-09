# features/login.feature

Feature: Login Feature

  Scenario: Valid Login

    Given user launches OrangeHRM application
    When user enters username "Admin" and password "admin123"
    Then user should navigate to dashboard page