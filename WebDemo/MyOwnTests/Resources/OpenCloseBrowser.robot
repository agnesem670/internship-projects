*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Start TestCase
    Open Browser  http://localhost:7272/  chrome
    Maximize Browser Window

Finish TestCase
    Close Browser  