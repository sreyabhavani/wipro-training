*** Settings ***
Resource    ../Resources/common.resource
Resource    ../Resources/login_page.resource
Resource    ../Resources/cart_page.resource
Library     ../Libraries/InternalCalculations.py

Suite Setup       Open Browser To Login Page
Suite Teardown    Close Browser Session

*** Test Cases ***
Valid Login Test

    Login To Application    standard_user    secret_sauce

    Element Should Be Visible    ${PRODUCT_TITLE}


Verify Product Prices

    Login To Application    standard_user    secret_sauce

    ${price1}=    Get Product Price By Name    Sauce Labs Backpack
    ${price2}=    Get Product Price By Name    Sauce Labs Bike Light

    ${total}=    Evaluate    float(${price1}) + float(${price2})

    Should Be Equal As Numbers    ${total}    39.98