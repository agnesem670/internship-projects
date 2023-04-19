*** Settings ***
Library  SeleniumLibrary
Variables  ../WebElements.py

*** Variables ***

*** Keywords ***
Input text in the search box and click search
    [Arguments]  ${search_text}
    Input Text    ${HomePageSearchTextBox}    ${search_text}
    Press Keys    ${HomePageSearchButtom}   [return]

Click the bottom 'Kontakt'
    Press Key    HomePageKontaktBottom    [return]


