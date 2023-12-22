#!/usr/bin/python3
def safe_print_integer_err(value):
    if value is not None:
        import sys
        try:
            print('{:d}'.format(value))
            return True
        except ValueError:
            sys.stderr.write(
                "Exception: Unknown format code 'd' for object of type 'str'\n"
            )
            return False
