def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    num = '0123456789'
    if len(zip_code) <= 5:
        for i in range(len(zip_code)):
            if not (zip_code[i] in num):
                return False
                break
        return True
    else:
        return False

is_valid_zip('1234x')