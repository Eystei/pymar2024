*** Settings ***
Library           library_keywords.py
Library           BuiltIn

*** Variables ***
${BOOK_NAME}      Harry Potter and the Goblet Fire
${AUTHOR}         J. K. Rowling
${NUM_PAGES}      636
${ISBN}           0747550794

*** Test Cases ***
Multiple Reservation Flow
    [Documentation]    Test 1: Multiple reservation flow
    ${book}=    Create Book    ${BOOK_NAME}    ${AUTHOR}    ${NUM_PAGES}    ${ISBN}
    ${pika}=    Create Reader    Pikachu
    ${ash}=    Create Reader    Ash
    Log Message    Test 1: Multiple reservation flow
    ${result}=    Reserve Book    ${pika}    ${book}
    Should Be True    ${result}
    ${result}=    Reserve Book    ${ash}    ${book}
    Should Be True    ${result} == False
    ${result}=    Cancel Reserve    ${pika}    ${book}
    Should Be True    ${result}
    ${result}=    Reserve Book    ${ash}    ${book}
    Should Be True    ${result}

Get Book Flow
    [Documentation]    Test 2: Get book flow
    ${book}=    Create Book    ${BOOK_NAME}    ${AUTHOR}    ${NUM_PAGES}    ${ISBN}
    ${pika}=    Create Reader    Pikachu
    ${ash}=    Create Reader    Ash
    Log Message    Test 2: Get book flow
    ${result}=    Reserve Book    ${pika}    ${book}
    Should Be True    ${result}
    ${result}=    Get Book    ${pika}    ${book}
    Should Be True    ${result}
    ${result}=    Get Book    ${ash}    ${book}
    Should Be True    ${result} == False
    ${result}=    Return Book    ${pika}    ${book}
    Should Be True    ${result}
    ${result}=    Reserve Book    ${ash}    ${book}
    Should Be True    ${result}
    ${result}=    Get Book    ${ash}    ${book}
    Should Be True    ${result}

Invalid Return Attempt
    [Documentation]    Test 3: Invalid return attempt
    ${book}=    Create Book    ${BOOK_NAME}    ${AUTHOR}    ${NUM_PAGES}    ${ISBN}
    ${pika}=    Create Reader    Pikachu
    ${ash}=    Create Reader    Ash
    Log Message    Test 3: Invalid return attempt
    ${result}=    Reserve Book    ${pika}    ${book}
    Should Be True    ${result}
    ${result}=    Get Book    ${pika}    ${book}
    Should Be True    ${result}
    ${result}=    Return Book    ${ash}    ${book}
    Should Be True    ${result} == False
