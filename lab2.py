"""                                Lab 2: Submit by Thursday 23rd May 2024
                                        Functions and Interface Design
"""


"""
Exercise 3.0
"""
# In class activity
def getQuizScore():
    """Prompt the user to enter their quiz score and return it as an integer."""
    score = int(input("Please, enter your quiz score: "))   # Take the score from the user and then convert it to an integer.
    return score

# In class activity
def getLabScore():
    """Prompt the user to enter their lab score and return it as an integer."""
    score = int(input("Please, enter your labs score: "))   # Take the score from the user and then convert it to an integer.
    return score

# In class activity
def getExamScore():
    """Prompt the user to enter their exam score and return it as an integer."""
    score = int(input("Please, enter your exam score: "))   # Take the score from the user and then convert it to an integer.
    return score

# Question: 1
def getParticipationScore():
    """Prompt the user to enter their participation score and return it as an integer."""                                       
    score = int(input("Please, enter your participation score: "))  # Take the score from the user and then convert it to an integer.
    return score
   
# Question: 2
def gradingWeights():
    """
    Prompt the user to enter the weights for quiz, lab, participation, and exam scores.

    Returns:
        A tuple containing the weights for quiz, lab, participation, and exam scores.
    """
    quiz_weight = int(input("\nEnter your quiz weight: %"))                     # Take the weight and convert it to an integer.
    lab_weight = int(input("Enter your lab weight: %"))                         # Take the weight and convert it to an integer.
    participation_weight = int(input("Enter your participation weight: %"))     # Take the weight and convert it to an integer.
    exam_weight = int(input("Enter your exam weight: %"))                       # Take the weight and convert it to an integer.
    return (quiz_weight, lab_weight, participation_weight, exam_weight)

# Function that computes the final grade of the student
def computeGrade():
    """
    Compute the final grade based on scores and weights provided by the user.

    Returns:
        The final grade if weights sum to 100%, otherwise a message to correct the weights.
    """
    # Assign each score from the user to a variable.
    quiz_score = getQuizScore()                         
    lab_score = getLabScore()                           
    participation_score = getParticipationScore()       
    exam_score = getExamScore()                         
    
    # Assign each score weight from the user to a variable.
    weights = gradingWeights()
    quiz_weight = weights[0]
    lab_weight = weights[1]
    participation_weight = weights[2]
    exam_weight = weights[3]
    message = "\nPlease, ensure that the weight is exactly equal to 100% !!!"
    
    # Check that the total weight equals 100%. 
    if quiz_weight + lab_weight + participation_weight + exam_weight == 100:
        # If true, then calculate and assign score contribution to a variable.
        quiz_contribution = (quiz_score * quiz_weight) / 100
        lab_contribution = (lab_score * lab_weight) / 100
        participation_contribution = (participation_score * participation_weight) / 100
        exam_contribution = (exam_score * exam_weight) / 100
        # Calculate final grade
        final_grade = quiz_contribution + lab_contribution + participation_contribution + exam_contribution
        return final_grade
    # If not, prompt the user to correct that and quit the program. 
    else:
        return message
  
#   TEST computeGrade       
# student_1_grade = computeGrade()
# print(student_1_grade)
  

"""
Exercise 3.1
"""
def right_justify(s):
    """
    Print the string s with enough leading spaces so that the last letter of the string is in column 70.

    Args:
        s: The string to justify.
    """
    s_len = len(s)
    space_len = 70 - s_len
    tab = " " * space_len
    print(f"{tab}{s}")
 
#   TEST right_justify    
# right_justify("monty")
    

"""
Exercise 3.2
"""
# Question: 1
def do_twice(f):
    """
    Call the function f twice.

    Args:
        f: The function to call.
    """
    f()
    f()
    
def print_spam():
    """Print the word 'spam'."""
    print("spam")

#   TEST do_twice
# do_twice(print_spam)

# Question: 2, 3 & 4
def do_twice_modified(f, v):                 
    """
    Call the function f twice, passing v as an argument each time.

    Args:
        f: The function to call.
        v: The argument to pass to the function.
    """
    f(v)
    f(v)
    
def print_spam_modified(n):
    """Print the argument n.

    Args:
        n: The value to print.
    """
    print(n)

#   TEST do_twice_modified
# do_twice_modified(print_spam_modified, "spam")

# Question 5
def do_four(f, v):
    """
    Call the function f four times, passing v as an argument each time.

    Args:
        f: The function to call.
        v: The argument to pass to the function.
    """
    do_twice_modified(f, v)
    do_twice_modified(f, v)
 
#   TEST do_four
do_four(print_spam_modified, "spam") 

"""
Exercise 3.3
"""
def print_grid():
    """Print a 2x2 grid."""
    horizontal = "+ - - - - + - - - - +"                    # Variable containing the "+-" that will be printed to avoid repetition.
    vertical = "|         |         |"                      # Variable containing the "|" that will be printed to avoid repetition.
    
    print(horizontal)                                       # Start by printing the plus and minus signs.
    print((vertical + "\n") * 4, end="")                    # Then print the vertical bars on four different lines without spacing them.
    print(horizontal)                                       # Then, repeat the plus and minus horizontally.
    print((vertical + "\n") * 4, end="")                    # Then, repeat the vertical bars again.
    print(horizontal)                                       # Finally, close the grid with the plus and minus signs.

#   TEST print_grid
# print_grid()
