# Exercise 6.1:
print("Exercise 6.1:\nThe program prints:")
print("9 90")
print("8100\n\n")


# Exercise 6.2: The Ackermann function, ack(m, n).
print("Exercise 6.2:")

def ack(m, n):
    """
    Compute the Ackermann function A(m, n).

    Args:
        m: non-negative integer
        n: non-negative integer

    Returns:
        The value of the Ackermann function for the given m and n.
    """
    # Base case for when m is 0
    if m == 0:
        return n + 1
    # Recursive case for when m > 0 and n is 0
    elif m > 0 and n == 0:
        return ack(m - 1, 1)
    # Recursive case for when m > 0 and n > 0
    elif m > 0 and n > 0:
        return ack(m - 1, ack(m, n - 1))
    # No need for else case here, as all possible cases are covered

print(f"eg: ack(3, 4) = {ack(3, 4)}")
# Note: For larger values of m and n, a RecursionError can occur due to deep recursion.
print("For larger values of m and n it occurs a RecursionError.\n\n")


# Exercise 6.3: Check if a word is a palindrome.
print("Exercise 6.3:")

def first(word):
    """
    Returns the first character of a string.
    
    Args:
        word: A string.
        
    Returns:
        The first character of the string.
    """
    return word[0]

def last(word):
    """
    Returns the last character of a string.
    
    Args:
        word: A string.
        
    Returns:
        The last character of the string.
    """
    return word[-1]

def middle(word):
    """
    Returns the middle characters of a string.
    
    Args:
        word: A string.
        
    Returns:
        All characters of the string except the first and last.
    """
    return word[1:-1]

print("1. If we call middle with a string that has:")
print("\t-Two letters: It returns an empty string")
print("\t-One letter: It returns an empty string")
print("\t-Empty string: It returns an empty string\n")

def is_palindrome(myString):
    """
    Check if a string is a palindrome.
    
    Args:
        myString: A string.
        
    Returns:
        True if the string is a palindrome, False otherwise.
    """
    # Base case: an empty string is a palindrome
    if len(myString) == 0:
        return True
    else:
        # Check if the first and last characters are the same
        if first(myString) == last(myString):
            # Recursively check the middle part of the string
            myString = middle(myString)
            return is_palindrome(myString)
        else:
            # If the first and last characters don't match, it's not a palindrome
            return False

print(f"2.\teg 1: is_palindrome('redivider'): {is_palindrome('redivider')}")
print(f"\teg 2: is_palindrome('school'): {is_palindrome('school')}")
print(f"\teg 3: is_palindrome('noon'): {is_palindrome('noon')}\n\n")


# Exercise 6.4: Check if a number is a power of another number.
print("Exercise 6.4:")

def is_power(a, b):
    """
    Check if a is a power of b.
    
    Args:
        a: An integer.
        b: An integer.
        
    Returns:
        True if a is a power of b, False otherwise.
    """
    # Base case: 1 is a power of any number
    if a == 1:
        return True
    # If b is 1, only 1 can be a power of 1
    if b == 1:
        return False
    else:
        # Check if a is divisible by b and recursively check the quotient
        if a % b == 0:
            return is_power(a // b, b)
        else:
            return False

print(f"eg 1: is_power(27, 3): {is_power(27, 3)}")
print(f"eg 2: is_power(40, 4): {is_power(40, 4)}")
print(f"eg 3: is_power(1, 2024): {is_power(1, 2024)}\n\n")


# Exercise 6.5: Compute the greatest common divisor of two numbers.
print("Exercise 6.5:")

def gcd(a, b):
    """
    Compute the greatest common divisor (GCD) of a and b.
    
    Args:
        a: An integer.
        b: An integer.
        
    Returns:
        The GCD of a and b.
    """
    # Base case: when b is 0, gcd is a
    if b == 0:
        return a
    else:
        # Recursively compute the gcd of b and the remainder of a divided by b
        r = a % b
        return gcd(b, r)

print(f"eg 1: gcd(2002, 2024) = {gcd(2002, 2024)}")
print(f"eg 2: gcd(81, 9) = {gcd(81, 9)}")
print(f"eg 3: gcd(144, 12) = {gcd(144, 12)}\n")
print("End !!!")