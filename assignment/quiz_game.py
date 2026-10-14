#Creating tuples questions() and options() because there is no need to change them(meaning they are immutable)
questions = ("How many elements are in the periodic table?: ",
                       "Which animal lays the largest eggs?: ",
                       "What is the most abundant gas in Earth's atmosphere?: ",
                       "How many bones are in the human body?: ",
                       "Which planet in the solar system is the hottest?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
                   ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
                   ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
                   ("A. 206", "B. 207", "C. 208", "D. 209"),
                   ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

answers = ("C", "D", "A","A", "B") #stoting answers
guesses = [] #guesses is empty list; Score and the Order of the questions is zero for now
score = 0
question_num = 0
# Loop through each question, display options, and collect user input
for question in questions:
    print("-----")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    # Check if the guess matches the correct answer
    if guess == answers[question_num]:
        score+=1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"Correct answer is: {answers[question_num]}")
    question_num+=1
# Display final results summary
print("---------")
print("RESULTS")
print("---------")

print("Answers: ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end = " ")
for guess in guesses:
    print(guess, end=" ")
print()
# Calculate and display the final percentage score
score = int(score/len(answers)*100)
print(f"You got {score}% correct")