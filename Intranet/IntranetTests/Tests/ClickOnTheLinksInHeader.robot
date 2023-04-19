*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/StartAndFinishTestCase.robot
Resource  ../Resources/OdooReaderPageObjects/Header.robot
Resource  ../Resources/VariablesScope.robot

Suite Setup  StartAndFinishTestCase.Start Test Case  http:/localhost:8080/
Suite Teardown  StartAndFinishTestCase.Finish Test Case

*** Test Cases ***
Click on the link and verifies the basic content
    [Documentation]  Click on the links located in header and verifies the basic (constant) content.
    Header.Click on the link 'Get Active Projects!' and varifies the content
    Header.Click on the link 'Get Favorite Projects!' and varifies the content