# language: en
Feature: Cancel subscription
  A user owns subscription and he/she wants to cancel it.

  Actors: A user

  Triggers: A user clicks “Cancel Subscription” link placed in a product
    description section on Subscription Details page.

  Flow of Events:
    1 - A user clicks “Cancel Subscription” link placed in a product
      description section on Subscription Details page.
    2 - A user sees a list of reasons for cancelling subscription and they have to
      pick one
    3 - Once he/she selects a reason, he/she clicks “Continue” button
    4 - A user is taken to a page which offers a 50% discount for the next 3 months
      for that subscription. A user can choose between "Keep Subscription" or
      "Cancel Subscription"
    5 - A user has to click one of the buttons mentioned above depending on what
    he/she wishes to do
    6 - If he/she clicks "Cancel Subscription" button, his/her subscription gets
      cancelled. A user will be redirected to Product subscription page where
      he/she can see an appropriate message about cancelling subscription.
    7 - If he/she clicks "Keep Subscription" button, then a discount of 50% is
      applied to that subscription for 3 months.

  Precondition: A user navigates to Subscription Details page of the website.

  Post Conditions:
    1 - If a user cancels a product subscription, then the status of  the product
    subscription will be changed to “Cancelled”.
    2 - If a user decided to keep subscription, then a discount of 50% is applied
    to that subscription for 3 months.
      1 - On 4th month they get charged the full amount again.
      2 - The 50% discount can only be applied once to every subscription. If a user
      tries to apply the 50% discount more than once, he/she will see an
      appropriate error message.

  Background: User start cancelling a subscription
    Given the user is logged in
    And the user is in the Subscription Details page
    Then the user clicks on Cancel subscription

  Scenario Outline: User cancel subscription
    Given the user selects the reason <reason>
    And the user clicks on Confirm button
    When the user confirm subscription cancelation
    Then the user sees his subscription status as canceled

    Examples: Cancelation reasons
      | reason  |
      | reason1 |
      | reason2 |
      | reason3 |
      | reason4 |
      | reasonN |

  Scenario Outline: User keep subscription for the discount
    Given the user has a subscription of the product
    And the user clicks on Cancel subscription
    And the user select the reason <reason>
    When the user clicks on Keep subscription
    Then the user see his subscription value with 50% of discount

    Examples: Cancelation reasons
      | reason  |
      | reason1 |
      | reason2 |
      | reason3 |
      | reason4 |
      | reasonN |
