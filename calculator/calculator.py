import random

# this is my "calculator base" - it does the
# real math so we can check the user answers
def my_calculator(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return round(a / b, 2)
    return none

#this function makes a list of questions
# depending on what grade the user typed in
# each question is stored as [question_text, correct_answer]:

def make_questions(grade):
    questions = []
 
    if grade <= 2:
        # little kids - simple adding and subtracting, small numbers
        for i in range(5):
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            op = random.choice(["+", "-"])
            if op == "-" and b > a:
                a, b = b, a  # swap so we dont get negative answers
            text = str(a) + " " + op + " " + str(b)
            answer = my_calculator(a, b, op)
            questions.append([text, answer])

#Questions for grade 3,4 
    elif grade <= 4:
        # bigger adding/subtracting, plus start of times tables
        for i in range(5):
            choice = random.randint(1, 3)
            if choice == 1:
                a = random.randint(10, 99)
                b = random.randint(10, 99)
                op = random.choice(["+", "-"])
                if op == "-" and b > a:
                    a, b = b, a
                text = str(a) + " " + op + " " + str(b)
                answer = my_calculator(a, b, op)
            else:
                a = random.randint(1, 10)
                b = random.randint(1, 10)
                text = str(a) + " x " + str(b)
                answer = my_calculator(a, b, "*")
            questions.append([text, answer])
 
 #Questions for grade 5,6  
    elif grade <= 6:
        # times tables, division that comes out even, bigger numbers
        for i in range(5):
            choice = random.randint(1, 3)
            if choice == 1:
                a = random.randint(2, 12)
                b = random.randint(2, 12)
                text = str(a) + " x " + str(b)
                answer = my_calculator(a, b, "*")
            elif choice == 2:
                b = random.randint(2, 12)
                ans = random.randint(2, 12)
                a = b * ans  # so it divides evenly, nice and clean
                text = str(a) + " / " + str(b)
                answer = my_calculator(a, b, "/")
            else:
                a = random.randint(50, 500)
                b = random.randint(10, 200)
                op = random.choice(["+", "-"])
                if op == "-" and b > a:
                    a, b = b, a
                text = str(a) + " " + op + " " + str(b)
                answer = my_calculator(a, b, op)
            questions.append([text, answer])
#Questions for grade 7,8
 
    elif grade <= 8:
        # percentages, and small algebra
        for i in range(5):
            choice = random.randint(1, 3)
            if choice == 1:
                percent_options = [10, 20, 25, 50, 75]
                p = random.choice(percent_options)
                num = random.randint(4, 40) * 5  # keeps it a friendly number
                answer = round((p / 100) * num, 2)
                text = "What is " + str(p) + "% of " + str(num) + "?"
            elif choice == 2:
                a = random.randint(2, 20)
                x = random.randint(1, 20)
                b = a + x
                text = "If x + " + str(a) + " = " + str(b) + ", what is x?"
                answer = x
            else:
                a = random.randint(2, 12)
                b = random.randint(2, 12)
                c = random.randint(2, 12)
                # order of operations, kept small so it's not scary
                answer = a + b * c
                text = str(a) + " + " + str(b) + " x " + str(c)
            questions.append([text, answer])
 #Questions for grade 9,10, also any class above them
    else:
        # grade 9 and up - a bit of everything, slightly harder algebra
        for i in range(5):
            choice = random.randint(1, 3)
            if choice == 1:
                coeff = random.randint(2, 5)
                x = random.randint(1, 15)
                a = random.randint(1, 20)
                b = coeff * x + a
                text = str(coeff) + "x + " + str(a) + " = " + str(b) + ",  what is x?"
                answer = x
            elif choice == 2:
                base = random.randint(2, 6)
                exp = random.randint(2, 3)
                answer = base ** exp
                text = str(base) + " ^ " + str(exp)
            else:
                a = random.randint(10, 50)
                b = random.randint(2, 9)
                c = random.randint(2, 9)
                answer = (a - b) * c
                text = "(" + str(a) + " - " + str(b) + ") x " + str(c)
            questions.append([text, answer])
 
    return questions
 
 
# this function asks the user their age and grade
# and makes sure they typed real numbers
def get_age_and_grade():
    while True:
        age_text = input("How old are you? ")
        grade_text = input("What grade are you in? (1 to 12) ")
 
        if age_text.isdigit() and grade_text.isdigit():
            age = int(age_text)
            grade = int(grade_text)
            if 1 <= grade <= 12:
                return age, grade
            else:
                print("Hmm, grade should be between 1 and 12. try again!")
        else:
            print("Oops! please type numbers only. try again!")
 
  
# this function shows the questions, gets the
# user's answers, and checks them against my
# calculator base
def run_quiz(questions):
    num_right = 0
 
    for i in range(len(questions)):
        question_text = questions[i][0]
        correct_answer = questions[i][1]
 
        print("")
        print("Question " + str(i + 1) + ":  " + question_text + " = ?")
        user_answer = input("Your answer: ")
 
        try:
            user_number = float(user_answer)
        except ValueError:
            user_number = None
 
        if user_number is not None and abs(user_number - correct_answer) < 0.01:
            print("Correct! Nice job!")
            num_right += 1
        else:
            print("Not quite. The right answer was " + str(correct_answer))
 
    return num_right
 
 
# this is where the program actually starts
def main():
    print("==================================================")
    print("   MY COOL MATH CALCULATOR QUIZ!!")
    print("==================================================")
    print("Hi! Answer a couple questions and I'll make a quiz just for you!")
    print("")
 
    age, grade = get_age_and_grade()
 
    print("")
    print("Okay age " + str(age) + ", grade " + str(grade) + " -- here are your questions!")
 
    questions = make_questions(grade)
    num_right = run_quiz(questions)
 
    print("")
    print("==================================================")
    print("You got " + str(num_right) + " out of " + str(len(questions)) + " right!!")
 
    if num_right == len(questions):
        print("PERFECT SCORE!! :D")
    else:
        print("Good try, keep practicing!")
    print("==================================================")
 
 
# this makes sure the quiz only runs when you
# actually run this file (not if it gets imported)
if __name__ == "__main__":
    main()
