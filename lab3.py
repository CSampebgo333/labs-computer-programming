"""Exercise 5.1"""
import time

total_time = time.time()
second_to_minute = 60
minutes_to_hours = 60
hours_to_days = 24
hours_to_second = second_to_minute * minutes_to_hours
days_to_seconds = second_to_minute * minutes_to_hours * hours_to_days

days_spent = int(total_time // days_to_seconds)
remaining = total_time % days_to_seconds
hours_spend = int(remaining // hours_to_second)
remaining = remaining % hours_to_second
minutes_spent = int(remaining // minutes_to_hours)
second_spent = int(remaining % minutes_to_hours)

print(f"{days_spent} days, {hours_spend} hours, {minutes_spent} minutes, {second_spent} seconds")



"""Exercise 5.2"""
# Question 1
def check_fermat(a, b, c, n):
    if n > 2:
        if (a**n + b**n == c**n):
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn’t work.")
            
# Question 2            
def get_user_numbers():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    n = int(input("Enter n: "))
    return (a, b, c, n)
    
numbers = get_user_numbers()
check_fermat(numbers[0], numbers[1], numbers[2], numbers[3])



"""Exercise 5.3"""
#Question 1
def is_triangle(s1, s2, s3):
    if s2 > s1:
        longer_size = s2
        sum_others_size = s1 + s3
        if s3 > s2:
            longer_size = s3
            sum_others_size = s1 + s2
    elif s3 > s1:
        longer_size = s3
        sum_others_size = s1 + s2
    else:
        longer_size = s1
        sum_others_size = s2 + s3
        
    if longer_size > sum_others_size:
        print("No")
    else:
        print("Yes")

# Question 2
def get_sizes():
    s1 = int(input("Enter size 1: "))
    s2 = int(input("Enter size 2: "))
    s3 = int(input("Enter size 3: "))
    return (s1, s2, s3)

sizes = get_sizes()
is_triangle(sizes[0], sizes[1], sizes[2])
 
 
 
"""Exercise 5.4"""
def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)

recurse(3, 0)

#Question 1
"""
If we call the function like recurse(-1, 0), the function will keep running indefinitely
since -1 is already less than 0 and will keep decreasing, the base case
condition will never be reached.
"""

#Question 2
"""
@Function name: recurse
@Function role: recursive() decrements a number "n" recursively and accumulates the sum of n and s.
@Parameters: n: The starting integer, which is decremented in each recursive call
             s: The accumulated sum, which is incremented by the current value of n.
    
@Returns:
    None: The function does not return anything since it prints the final value of s when n reaches 0.
    
@Raises:
    RecursionError: If called with a negative value for n, recurse() will run indefinitely.
    
@Example:
    recurse(3, 0) will print 6.
"""
 
 
 
"""Exercise 5.4""" 
def fibonaci(n):
    if n == 0:
        return 0;
    elif n == 1:
        return 1;
    else:
        return fibonaci(n - 1) + fibonaci(n - 2)
 

print(fibonaci(7))