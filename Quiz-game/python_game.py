from questions import quiz

def Check_ans(question,ans,attempts, score):

    if quiz[question]['answer'].lower() == ans.lower():
        print(f"correct Answer! \n Your score is {score+1}!")
        return True
    else:
        print(f"Wrong Answer :( \n You have {attempts-1} left! \n Try again...")
        return False

def print_dictionary():
    for question_id, ques_answer in quiz.item():
        for key in ques_answer:
            print(key + ':', ques_answer[key])

def intro_message():
    print("Welcome to this python quiz! \nAre you ready to test your knowledge in python?")
    print("There are a total of 8 questions, you can skip a question anytime by typing 'skip' ")
    input("Press any key to start the fun ;)")
    return True

    intro = intro_message()
    while True:
        score = 0
        for question in quiz:
            attempts = 3
            while attempts > 0:
                print(quiz[question]['qustion'])
                answer = input("Enter Answer (to move to the next qustion, type 'skip') :")
                if answer == "skip":
                    break
                check = Check_ans(qustion,answer, attempts,score)
                if check:
                    score +=1
                    break
                    attempts -=1
                    break
    print(f"Your final score is {score} !\n")
    print("Want to know the correct answer? Please see them below! ;)\n")
    print_dictionary()
    print("Thanks for playing the Python game! ")