*** Settings ***
Documentation  WebDemoTests
Resource  ../Resources/OpenCloseBrowser.robot
Resource  ../Resources/UserDefinedKeywords.robot

Test Setup  Start TestCase        # will be always executed, regardless of test result
Test Teardown  Finish TestCase     # will be always executed, regardless of test result

*** Variables ***


*** Test Cases ***
Valid username and password.
    [Documentation]  Valid username and password
    [Tags]  Functional

    Enter valid username and password
    Logout from welcome page

