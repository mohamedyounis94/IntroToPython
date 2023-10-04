import random

def computer_assest():
    num1 = random.randrange(1,10)
    num2 = random.randrange(1,10)
    result = num1 * num2
    correct_answer = ['Very good!','Nice work!','Keep up the good work!']
    wrong_answer = ['No. Please try again.','Wrong. Try once more.','No. Keep trying.']
    type_problem = int(input('Select Operator 1- Addition, 2- Sub, 3- Multipli, 4- Divid, 5- Random Operator'))
    rand_type = random.randrange(1,5)
    rand_operator = ['+','-','*','/']
    # print = rand_operator[0]

    if type_problem == 1:
        result = num1 + num2
    elif type_problem == 2:
        result = num1 - num2
    elif type_problem == 3:
        result = num1 * num2
    elif type_problem == 4:
        result = num1 / num2
    else:
        random_mixture()
    
    
    
    
    print(result)
    


    while True:
        rand_response = random.randrange(0,3)
        print(f'How much is {num1} times {num2}?')
        stu_input = int(input())

        if stu_input == result:
            print(correct_answer[rand_response])
            break
        else:
            print(wrong_answer[rand_response])
            

def random_mixture():
    num1 = random.randrange(1,10)
    num2 = random.randrange(1,10)
    
    correct_answer = ['Very good!','Nice work!','Keep up the good work!']
    wrong_answer = ['No. Please try again.','Wrong. Try once more.','No. Keep trying.']
    rand_type = random.randrange(1,5)
    rand_operator = ['+','-','*','/']

    

    if rand_type == 1:
        result = num1 + num2
    elif rand_type == 2:
        result = num1 - num2
    elif rand_type == 3:
        result = num1 * num2
    elif rand_type == 4:
        result = num1 / num2
    

    print(result)
    


    while True:
        rand_response = random.randrange(0,3)
        print(f'How much is {num1} times {num2}?')
        stu_input = int(input())

        if stu_input == result:
            print(correct_answer[rand_response])
            break
        else:
            print(wrong_answer[rand_response])



computer_assest()
