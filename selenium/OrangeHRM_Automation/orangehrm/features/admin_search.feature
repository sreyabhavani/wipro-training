# features/admin_search.feature

Feature: Admin Search

  Scenario: Search User

    When I enter the following search criteria

      | Username | User Role | Status  |
      | Admin    | Admin     | Enabled |