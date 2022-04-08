Feature: Check login is successful with valid credentials

  Scenario: Check login page open successfully
    Given browser is open
    When user is on login page
    And user enter username
    And Click on the continue button
    Then user enter password
    And Click on the submit button
    And user navigated to home page
    Then close browser