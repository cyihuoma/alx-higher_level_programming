#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if 'result' in locals():
            print("Inside result: {}".format(result))
    return result
