from loguru import logger


def evaluate_expression(expression):
    try:
        expression = expression.replace("\\", "/")

        return eval(expression)

    except ZeroDivisionError:
        logger.error("Division by zero.")
        return "Division by zero."

    except ValueError as e:
        logger.error(f"Value error: {e}")
        return str(e)

    except SyntaxError:
        logger.error("Syntax error in the expression.")
        return "Syntax error in the expression."

    except NameError:
        logger.error("Name error in the expression.")
        return "Name error in the expression."


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
    assert evaluate_expression("2 + abc") == "Name error in the expression."

    logger.success("All tests passed.")
