# features/leave.feature

Feature: Leave Workflow

  Scenario: Apply Leave

    When user stores initial leave balance
    And user applies for one day leave
    Then success toast message should be displayed
    And leave balance should reduce by one