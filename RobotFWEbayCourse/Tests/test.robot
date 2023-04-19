*** Settings ***
Documentation  DrogeriaKosmetycznaTests
Resource  ../Resources/OpenCloseBrowser.robot
Resource  ../Resources/BasicSearchFunctionality.robot
Resource  ../Resources/PageObject/HeaderPage.robot
Resource  ../Resources/PageObject/SearchResultPage.robot

Test Setup  OpenCloseBrowser.Start Browser
Test Teardown  OpenCloseBrowser.Finish Browser

*** Variables ***

*** Test Cases ***
Verify basic search funcionality
    HeaderPage.Input text in the search box and click search  krem
    SearchResultPage.Verify Search results  Wyniki  krem






