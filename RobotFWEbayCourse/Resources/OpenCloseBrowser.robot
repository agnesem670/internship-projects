*** Settings ***
Documentation  DrogeriaEkologicznaTests
Library  SeleniumLibrary

*** Variables ***


*** Keywords ***
Start Browser
    Open Browser  https://www.drogeria-ekologiczna.pl/  chrome
    Maximize Browser Window
   

Finish Browser
    Close Browser

