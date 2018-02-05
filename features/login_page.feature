# language: en
Feature: Login Page
  To be successfully logged in to the website, a user fill in Email and Password
  fields with correct values. If email and/or password values are incorrect,
  the website will display an appropriate message.

  Actors: A user

  Triggers: when a user clicks "Login" button

  Flow of events:
    1 - If Email and/or Password fields are not filled in with any values, the
    website make empty fields borders red color
    2 - When a user enters a incorrect email or password, then the website will
    display an appropriate error message
    Validations when a user clicks "Forgot your password? Recover password" link
    1 - A user will see Reset Password page with Email field and "Send" button

  Precondition: A user navigates to Login Page of the website

  Post Conditions:
    1 - A user successfully logs in to the website with valid credentials
    2 - After the authentication, a user is redirected to the Main page of the
    website which is Library page. There is mandatory section called
    “Upcoming Product” on it.
    3 - The Main Menu of the website is displayed.

  Background: User must be in the Login Page
    Given the user is on the login page

  Scenario: User does not fill in any field
    Given the user does not fill any field
    When the user clicks on login button
    Then the user should stay in the same page
    And should see the email field with red borders
    And should see the password field with red borders

  Scenario: User fill in only email field
    Given the user fill in only email field
    When the user clicks on login button
    Then the user should stay in the same page
    And should see the password field with red borders

  Scenario: User fill in only password field
    Given the user fill in only password field
    When the user clicks on login button
    Then the user should stay in the same page
    And should see the email field with red borders

  Scenario Outline: Successfull login
    Given the user inform the email "<email>"
    And the user inform the password "<password>"
    When the user clicks on login button
    Then the user should be redirected to the Library page
    And should see the main menu
    And should see the section Upcomming Product

    Examples: Valid Users
      | email                     | password             |
      | valid_user@domain.com     | thisisavalidpassword |
      | valid_user@mindvalley.com | validpassword        |

  Scenario Outline: Unsuccessful login
    Given the email "<email>"
    And the password "<password>"
    When the user clicks on login button
    Then the user should see the error message "<message>"

    Examples: Invalid Users
      | email           | password          | message                  |
      | user@domain.com | invalid_password  | Wrong email or password. |
      | user@domain.com | existing_password | Wrong email or password. |

  Scenario: User clicks on "Forgot your password? Recover password"
    Given the user access the login page
    When the user clicks on "Forgot your password? Recover password" link
    Then the user should be redirected to "Reset Password" page
    And should see the email field
    And should see the send button
