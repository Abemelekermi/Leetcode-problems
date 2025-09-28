#i want to check if a number is same as with it's reverse

def is_palindrome(x):
    # Convert integer to string
    str_x = str(x)
    
    # Check if the string is equal to its reverse
    return str_x == str_x[::-1]

# Example usage:
num = 121
result = is_palindrome(num)
print(result)  # Output: True
