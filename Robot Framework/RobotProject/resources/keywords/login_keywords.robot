*** Settings ***
Library     SeleniumLibrary
Library     ../pages/LoginPage.py

*** Keywords ***
Open Demoblaze Application
    Launch Demoblaze Application

Click Login Menu
    Click Login Link

Enter Login Username
    Enter Username

Enter Login Password
    Enter Password

Click Login Button
    Click Signin Button

Validate Successful Login
    Verify Successful Login

Close Application
    Close Browser

Enter Invalid Login Username
    Enter Invalid Login Username

Enter Invalid Login Password
    Enter Invalid Login Password

 Validate Invalid Login Alert
    Validate Invalid Login Alert


Launch Demoblaze Application
    # TODO: implement keyword "Launch Demoblaze Application".
    Fail    Not Implemented


Click Login Link
    # TODO: implement keyword "Click Login Link".
    Fail    Not Implemented


Enter Username
    # TODO: implement keyword "Enter Username".
    Fail    Not Implemented


Enter Password
    # TODO: implement keyword "Enter Password".
    Fail    Not Implemented


Verify Successful Login
    # TODO: implement keyword "Verify Successful Login".
    Fail    Not Implemented


Click Signin Button
    # TODO: implement keyword "Click Signin Button".
    Fail    Not Implemented

