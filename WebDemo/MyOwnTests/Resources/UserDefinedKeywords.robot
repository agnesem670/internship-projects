*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
Enter valid username and password
    Input Text    //*[@id="username_field"]    demo
    Input Text    //*[@id="password_field"]    mode
    Press Keys    //*[@id="login_button"]    return
    Page Should Contain    Welcome Page

Logout from welcome page
    Press Keys  //*[@id="container"]/p/a  return
    Page Should Contain    Login Page
