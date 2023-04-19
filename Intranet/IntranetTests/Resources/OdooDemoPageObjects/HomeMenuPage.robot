*** Settings ***
Library  SeleniumLibrary
Variables  ../WebElements.py

*** Keywords ***
Click on the Project icon
    Click Element    ${ProjectIcon}  return