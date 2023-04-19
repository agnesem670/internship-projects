*** Settings ***
Library  SeleniumLibrary
Resource  ./VariablesScope.robot

*** Keywords ***
Start Test Case
    [Arguments]  ${host_or_url}
    Open Browser  ${host_or_url}  ${BROWSER}
    Maximize Browser Window
    Sleep    1s

Finish Test Case
    Close Browser