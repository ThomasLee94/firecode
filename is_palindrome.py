def is_palindrome_recursive(text: str, forward=None, backward=None) -> bool:
    
    # set forward and backward
    if forward == None and backward == None:
        forward = 0
        backward = len(text) - 1 

    # check if forward is less than backwards
    if forward >= backward:
        return True
    
    # skip over non letters
    if text[forward] not in string.ascii_letters:
        return is_palindrome_recursive(text, forward + 1, backward)
    if text[backward] not in string.ascii_letters:
        return is_palindrome_recursive(text, forward, backward - 1)

    # check if indecies match
    if text[forward].lower() != text[backward].lower():
        return False
    else:
        return is_palindrome_recursive(text, forward + 1, backward - 1)