*** Settings ***
Library  SeleniumLibrary
Resource  ../VariablesScope.robot
Variables  ../WebElements.py

*** Keywords ***
Log in to the Odoo3 Demo
    Input Text    WebElements.LoginInputOdoo    ${login_odoo}
    Input Text    WebElements.PasswordInputOdoo    ${password_odoo}
    Click Button    WebElements.LogInButton 
