*** Settings ***
Documentation  WebDemo - click all locators
Resource  ../Resources/OpenCloseBrowser.robot

Test Setup  OpenCloseBrowser.Start TestCase     
# Test Teardown  OpenCloseBrowser.Finish TestCase

*** Variables ***

*** Keywords ***

*** Test Cases ***
Click locators
    Click Element  id:container
    Click Element  tag:h1
    Click Element  tag:p
    Click Element  tag:label
    Click Element  //*[@id="container"]/form/table/tbody/tr[2]/td[1]/label 

    
