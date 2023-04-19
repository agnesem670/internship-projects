*** Settings ***
Library  SeleniumLibrary
Resource  ../VariablesScope.robot
Variables  ../WebElements.py

*** Keywords ***
# -----------CLICK----------------------

Click on the link 'Get Active Projects!'
    Click Link  ${GetActiveLink}  return

Click on the link 'Get Favorite Projects!'
    Click Link    ${GetFavoriteLink}  return

# -----------CLICK AND VERIFY-----------

Click on the link 'Get Active Projects!' and varifies the content
    Click Link  ${GetActiveLink}  return
    Sleep    1s
    Page Should Contain    ${verifying_text_active}

Click on the link 'Get Favorite Projects!' and varifies the content
    Click Link    ${GetFavoriteLink}  return
    Sleep    1s
    Page Should Contain    ${verifying_text_favorite}