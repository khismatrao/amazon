Feature: Check login is successful

  Scenario: Check login page open successfully
    Given  I launch browser is open
    When user is on login page url
    And user enter "ishwarikhismatrao31@gmail.com"
    And Click on the continue btn
    Then user enter "Sonali@123"
    And Click on the submit btn
    Then close chrome browser



  Scenario Outline: Check login  with multiple invalid credentials
    Given browser is open
    When user is on login page
    And user enter "<username>"
    And Click on the continue button
    Then user enter  "<password>"
    And Click on the submit button
    Then close browser
    Examples:
      | username                     | password  |
      | ishwari@gmail.com            |123344     |
      | ishwarikhismatrao31@gmail.com|So0nali@123|
      | ishwari12@gmail.com          |Sonali@123 |