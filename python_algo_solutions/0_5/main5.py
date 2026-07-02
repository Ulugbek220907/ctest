def reverse(num:int) -> int:
    """
    Reverses the digits of an integer.

    Args:
        num (int): The integer to be reversed.

    Returns:
        int: The reversed integer.
    """
    INT_MAX = 2**31 - 1
    INT_MIN = -2**31
    # Convert the integer to a string, reverse it, and convert back to int
    
    if num < 0:
        # Handle negative numbers
        reversed_num = -int(str(-num)[::-1])
    else:
        reversed_num = int(str(num)[::-1])
    
    if reversed_num < INT_MIN or reversed_num > INT_MAX:
        return 0
    else:
        return reversed_num

print(reverse(153423649))  # Output: 0
