*** Settings ***
Resource    ../Resources/common.resource
Resource    ../Resources/login_page.resource

Suite Setup       Open Browser To Login Page
Suite Teardown    Close Browser Session

Test Template     Invalid Login Scenario

*** Test Cases ***
Invalid User
    invalid_user
    secret_sauce
    Epic sadface: Username and password do not match any user in this service

Locked User
    locked_out_user
    secret_sauce
    Epic sadface: Sorry, this user has been locked out.

Problem User
    problem_user
    wrong_password
    Epic sadface: Username and password do not match any user in this service

*** Keywords ***
Invalid Login Scenario
    [Arguments]    ${username}    ${password}    ${error_message}

    Login To Application    ${username}    ${password}

    Element Should Contain
    ...    xpath://h3[@data-test='error']
    ...    ${error_message}