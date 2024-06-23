from loguru import logger

ALLOWED_CHARS = '0123456789+-*/()%'


def simple_validator(expression):
    for char in expression:
        if char not in ALLOWED_CHARS:
            return False, char
    return True, None


def evaluate_expression(expression):
    expression = expression.replace(' ', '')
    valid, invalid_char = simple_validator(expression)
    if not valid:
        logger.error(f"Invalid char --> {invalid_char}")
        return f"Invalid char --> {invalid_char}"

    try:
        return eval(expression)
    except ZeroDivisionError:
        logger.error("Division by zero.")
        return "Division by zero."
    except SyntaxError:
        logger.error("Syntax error in the expression.")
        return "Syntax error in the expression."


def run():
    print('Input: "exit" if you want to close calculator')
    while True:
        exp = input("~ ").replace(' ', '')

        if exp.lower() == 'exit':
            print("Have a nice day. Bye.")
            break

        print(evaluate_expression(exp))


if __name__ == "__main__":
    assert evaluate_expression("2+3") == 5
    assert evaluate_expression("10-2") == 8
    assert evaluate_expression("2*3") == 6
    assert evaluate_expression("8/4") == 2
    assert evaluate_expression("10//3") == 3
    assert evaluate_expression("10%3") == 1
    assert evaluate_expression("2**3") == 8
    assert evaluate_expression("2+3*4") == 14
    assert evaluate_expression("2*3+4") == 10
    assert evaluate_expression("2+(3*4)-2") == 12
    assert evaluate_expression("(2+3)*4") == 20
    assert evaluate_expression("1/0") == "Division by zero."
    assert evaluate_expression("2+*3") == "Syntax error in the expression."
    assert evaluate_expression("2 + abc") == "Invalid char --> a"

    logger.success("All tests passed.")
