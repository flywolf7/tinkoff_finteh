def is_int(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False
