*** Settings ***
Documentation  WebDemoTests
Library  SeleniumLibrary

 
*** Keywords ***
Start browser
    Open Browser  http://localhost:7272/  chrome
    Maximize Browser Window

Close browser
    Close Browser
