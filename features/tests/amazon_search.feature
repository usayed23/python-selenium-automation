# Created by usyed at 9/29/2020
Feature: Test for Amazon Search
  # Enter feature description here

  Scenario: Amazon search returns correct result
     Given Open Amazon page
     When Input Dress into Amazon search field
     And Click on Amazon search icon
     Then Search results for Dress is shown
