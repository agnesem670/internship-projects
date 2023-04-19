*** Settings ***
Library  SeleniumLibrary
Variables  ../Resources/WebElements.py

*** Keywords ***
Get favorite project names from the table
    [Documentation]  Gets favorite projects names from the table
    
    @{fav_proj_names}=  Get WebElements    ${FavoriteTable}
    
    FOR    ${element}    IN    @{fav_proj_names}
        ${fav_proj_txt}=  Get Text    ${element}
        
    END


