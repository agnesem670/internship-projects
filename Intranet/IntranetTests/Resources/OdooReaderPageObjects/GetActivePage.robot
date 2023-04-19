*** Settings ***
Library  SeleniumLibrary
Variables  ../Resources/WebElements.py

*** Keywords ***
Get active project names from the table
    [Documentation]  Gets active projects names from the table
   
    @{act_proj_names}=  Get WebElements  ${ActiveTable}
    
    FOR    ${element}    IN    @{act_proj_names}
        ${act_proj_txt}=  Get Text    ${element}
        
    END