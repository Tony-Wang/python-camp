# -*- coding:utf-8 -*-
import random
import time


def detect_junior(first_num, operator, second_num):
    detected_result = False
    if operator == 'add':
        detected_result = (first_num+second_num)
    elif operator == 'minus':
        detected_result = (first_num-second_num)
    elif operator == 'multi':
        detected_result = (first_num*second_num)
    elif operator == 'divide':
        detected_result = (first_num/second_num)

    int_result = int(detected_result)
    if int_result == detected_result and 100 > detected_result > 0:
        return True
    else: return False


def detect_characters(char):
    numbers = ['0','1','2','3','4','5','6','7','8','9']
    char1 = str(char)
    for i in char1:
        if i in numbers:
            return True
        else: return False


def write_results(questions, correct):
    c = correct - 1
    correct_rate = c / questions
    file = open ("results.txt", 'a')
    file.write("time: " + time.strftime('%Y-%m-%d %H:%M:%S') +'\n')
    file.write("In a total of %d questions, you answered %d correctly. \n" % (questions,correct-1) )
    file.write("Correct Rate: " + str(int(correct_rate*100)) + "%  \n \n")


def print_results(questions, correct):
    c = correct - 1
    correct_rate = c / questions
    print("time: " + time.strftime('%Y-%m-%d %H:%M:%S') )
    print("In a total of %d questions, you answered %d correctly. " % (questions,correct-1) )
    print("Correct Rate: " + str(int(correct_rate*100)) + "%  \n")


def give_question(cycle_count):

    true_result = 0
    question_count = 1
    possible_operators = ['add', 'minus', 'multi', 'divide']
    user_win_count = 1

    current_cycle =0

    while current_cycle < cycle_count:
        operator = random.choice(possible_operators)
        a = random.randint(1, 100)
        b = random.randint(1, 100)

        #判断题目难度
        if detect_junior(a, operator, b) is True:
            if operator == 'add':
                true_result = int(a+b)
                print("Question%d : %d  + %d = ?" % (question_count, a, b))
            elif operator == 'minus':
                true_result = int(a-b)
                print("Question%d : %d  - %d = ?" % (question_count, a, b))
            elif operator == 'multi':
                true_result = int(a*b)
                print("Question%d : %d  * %d = ?" % (question_count, a, b))
            elif operator == 'divide':
                true_result = int(a/b)
                print("Question%d : %d  / %d = ?" % (question_count, a, b))

            #检查输入答案是否是数字
            legal_input = False
            while legal_input is not True:
                user_result = int(input("Please input your answer: \n "))
                legal_input = detect_characters(user_result)

            #判断结果
            if user_result == true_result:
                user_win_count +=1
                print("Answer correct!")
            else:
                print("Incorrect! The answer is %d" % true_result)

            current_cycle +=1

        else: pass

    write_results(cycle_count,user_win_count)
    print_results(cycle_count,user_win_count)


def main():
    cycles = int(input("How many rounds to play? \n"))
    give_question(cycles)
    continue_game = str(input("Have another round? (Y/N) \n"))

    while continue_game != 'N' or 'n':
        if continue_game == 'Y' or 'y':
            cycles = int(input("How many rounds to play? \n"))
            give_question(cycles)
            continue_game = input("Have another round? (Y/N) ")

main()