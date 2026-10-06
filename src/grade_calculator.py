import math
# create a variable called points_possible and set it equal to user input
points_possible = input("How many points was the assignment worth?")

# Error handling for points_possible
if points_possible < 0:
    print("The assignment cannot be less than 0. Please try again.")
    points_possible = input("How many points was the assignment worth?")


# create a variable called points_earned and set it equal to user input
points_earned = input("How many points did the student earn?")

# cast points_possible to a float
points_possible = float(points_possible)

# cast total_points to a float
total_points = float(points_earned)

# do the math
score = (total_points / points_possible) * 100 
rounded_score = round(score, 2)

# print the answer out
print(f'Your grade: {rounded_score}')

if rounded_score >= 90.0:
    letter_grade = 'A'
elif rounded_score >= 80.0:
    letter_grade = 'B'
elif rounded_score >= 70.0:
    letter_grade = 'C'
elif rounded_score >= 60.0:
    letter_grade = 'D'
else:
    letter_grade = 'F'

print(f'Your letter grade: {letter_grade}')