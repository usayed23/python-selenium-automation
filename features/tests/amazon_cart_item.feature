# Created by usyed at 10/17/2020
Feature: Test for Amazon Cart item
  # Enter feature description here

  Scenario: Amazon items is shown in cart

    Given Open Amazon page
     When Input ball into Amazon search field
     And Click on second search result item
     And Add the item to the cart
     Then Verify if item is in the cart
