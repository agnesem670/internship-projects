*** Settings ***
Library  SeleniumLibrary

*** Variables ***
#${search_result}  "Wyniki Twojego wyszukiwania:"
#&{dict1}  a=books b=travel c=cars

*** Keywords ***
Verify Search results
    [Arguments]  ${search_result}  ${search_text}
    Page Should Contain  ${search_result}  ${search_text}

Filter results by name A-Z
    Click Element  //*[@id="selectProductSort"]
    Click Element  //select[@id='selectProductSort']//descendant::option[@value='name:asc']