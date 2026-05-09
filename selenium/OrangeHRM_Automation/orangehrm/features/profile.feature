@Smoke @Regression @Profile
Feature: Update Profile

Background:
  Given user is logged in

Scenario: Update nickname
  When user goes to My Info page
  And user updates nickname "Shreya"
  Then profile should be updated