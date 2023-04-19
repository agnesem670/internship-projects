*** Settings ***
Library  SeleniumLibrary
Library  Collections
Variables  ../WebElements.py

*** Variables ***



*** Keywords ***
Get active Projects names 
       
    ${number}  Get Element Count    xpath://span[@class='o_text_overflow']
    ${number}  Evaluate    ${number} +1
    @{projects_names}  Create List
    # Log    @{list_name}[0]
    
    FOR    ${counter}    IN RANGE    1    ${number}    1
        ${title}  Get Element Attribute    xpath:(//span[@class='o_text_overflow'])[${counter}]    title 
        Append To List    ${projects_names}  ${title}
            
    END
    
    Log List    ${projects_names}
    

 