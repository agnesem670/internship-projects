*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/StartAndFinishTestCase.robot
Resource  ../Resources/OdooReaderPageObjects/GetFavoritePage.robot
Resource  ../Resources/OdooReaderPageObjects/GetActivePage.robot
Resource  ../Resources/OdooReaderPageObjects/Header.robot
Resource  ../Resources/VariablesScope.robot

Suite Setup  StartAndFinishTestCase.Start Test Case  ${HOST_READER}
Suite Teardown  StartAndFinishTestCase.Finish Test Case

*** Test Cases ***
Get active project names from the table
    Header.Click on the link 'Get Active Projects!'
    GetActivePage.Get active project names from the table

Get favorite project names from the table
    Header.Click on the link 'Get Favorite Projects!'
    GetFavoritePage.Get favorite project names from the table
