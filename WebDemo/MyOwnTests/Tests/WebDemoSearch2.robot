*** Settings ***
Documentation  WebDemoTests
Resource  ../Resources/OpenCloseBrowser.robot
Resource  ../Resources/UserDefinedKeywords.robot

Test Setup  OpenCloseBrowser.Start TestCase        # will be always executed, regardless of test result
Test Teardown  OpenCloseBrowser.Finish TestCase     # will be always executed, regardless of test result

*** Variables ***


*** Test Cases ***
Valid username and password.
    [Documentation]  Valid username and password
    [Tags]  Functional

    UserDefinedKeywords.Enter valid username and password
    UserDefinedKeywords.Logout from welcome page

