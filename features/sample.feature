# language: en

Feature: User open URL
  As a user
  I want to be able to open URL


  Scenario: Successful open URL
    Given URL "https://example.com/6666" is opened
    And wait "2" sec

  Scenario: 1111Successful open URL
    Given URL "https://example.com/6666" is opened
    And wait "2" sec
    And user clicked on "Menu icon"

    

    


    