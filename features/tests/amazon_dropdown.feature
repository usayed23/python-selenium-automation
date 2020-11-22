# Created by usyed at 11/21/2020
Feature: Test for DropDown menu

  Scenario: User search for PS5 in Electronic department
    Given Open Amazon page
    When User selects the video games department
    When User searches for PS5 in chosen department
    Then User Verifies that chosen department is searched in


  Scenario: User verifies new arrival clothing
    Given Product clothing product page
    When User Hover over New Arrivals
    Then verify Hover Pop up

