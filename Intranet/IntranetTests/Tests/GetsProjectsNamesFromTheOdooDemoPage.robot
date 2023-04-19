*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/OdooDemoPageObjects/LoginPage.robot
Resource  ../Resources/OdooDemoPageObjects/HomeMenuPage.robot
Resource  ../Resources/OdooDemoPageObjects/ProjectsKanbanDasboard.robot
Resource  ../Resources/StartAndFinishTestCase.robot
Variables  ../Resources/WebElements.py

Suite Setup  StartAndFinishTestCase.Start Test Case  ${URL_ODOO}
Suite Teardown  StartAndFinishTestCase.Finish Test Case

*** Test Cases ***
Log in to Odoo Demo, click on the project button and get active projects names from kanban dashboard
    Sleep    20s
    #Wait Until Element Is Visible    ${ProjectIcon}
    # THE SITE LOGS IN AUTOMATICALLY
    #LoginPage.Log in to the Odoo Demo
    HomeMenuPage.Click on the Project icon
    Sleep    3s
    ProjectsKanbanDasboard.Get active Projects names
    Sleep    5s
 
