*** Settings ***
Documentation  DrogeriaEkologicznaTests
Library  SeleniumLibrary

*** Variables ***

*** Keywords ***
Verify basic search funcionality
    Input Text    xpath://input[@id="search_query_top"]    krem
    Press Keys    xpath//*[@id="submit_searchbox"]/span   [return]
    Page Should Contain    Wyniki Twojego wyszukiwania:

Filter results by name A-Z
    Click Element    xpath://*[@id="selectProductSort"]
    Click Element  xpath://select[@id='selectProductSort']//descendant::option[@value='name:asc']
    Sleep    3s

Verify filter results
    Element Should Contain    xpath://*[@id="center_column"]/div[2]/div[1]/div[2]    Wyświetlono

