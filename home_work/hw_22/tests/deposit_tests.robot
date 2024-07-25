*** Settings ***
Library           ../resources/deposit_keywords.py
Library           BuiltIn

*** Variables ***
${INITIAL_INVESTMENT}    1000
${YEARS}                 1
${DEFAULT_INTEREST_RATE}    0.10
${CUSTOM_INTEREST_RATE}     0.05

*** Test Cases ***
Validate Initial Investment
    [Documentation]    Test 1: Validate initial investment is stored correctly
    ${deposit}=    Create Deposit    ${INITIAL_INVESTMENT}    ${YEARS}
    ${initial_investment}=    Get Initial Investment    ${deposit}
    Should Be Equal As Numbers    ${initial_investment}    ${INITIAL_INVESTMENT}

Validate Investment Length
    [Documentation]    Test 2: Validate investment length is stored correctly
    ${deposit}=    Create Deposit    ${INITIAL_INVESTMENT}    ${YEARS}
    ${investment_length}=    Get Investment Length    ${deposit}
    Should Be Equal As Numbers    ${investment_length}    ${YEARS}

Ensure Default Interest Rate
    [Documentation]    Test 3: Ensure default interest rate is used when not specified
    ${deposit}=    Create Deposit    ${INITIAL_INVESTMENT}    ${YEARS}
    ${interest_rate}=    Get Interest Rate    ${deposit}
    Should Be Equal As Numbers    ${interest_rate}    ${DEFAULT_INTEREST_RATE}

Validate Custom Interest Rate
    [Documentation]    Test 4: Validate that a custom interest rate is stored correctly
    ${deposit}=    Create Deposit    ${INITIAL_INVESTMENT}    ${YEARS}    ${CUSTOM_INTEREST_RATE}
    ${interest_rate}=    Get Interest Rate    ${deposit}
    Should Be Equal As Numbers    ${interest_rate}    ${CUSTOM_INTEREST_RATE}

Test With Zero Years Of Investment
    [Documentation]    Test 5: Test with zero years of investment
    ${deposit}=    Create Deposit    ${INITIAL_INVESTMENT}    0
    ${final_amount}=    Calculate Final Amount    ${deposit}
    Should Be Equal As Numbers    ${final_amount}    ${INITIAL_INVESTMENT}
