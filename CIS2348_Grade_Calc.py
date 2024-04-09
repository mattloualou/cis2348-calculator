# CIS 2348 Grade Calculator

def participation():
    running = 1
    grades = []
    while running == 1:
        score = int(input("Your participation score (input 'n' when you're done): "))
        if score >= 0 and score <= 100:
            grades.append(score)
        if type(score) != int:
            print('\n-------\nTry Again\n-------\n')
        if score == 'n':
            running == 2
    full_score = sum(grades)
    score_avg = full_score/(len(grades))
    pre_grade = score_avg * .10
    return pre_grade

def challenge():
    running = 1
    grades = []
    while running == 1:
        score = int(input("Your challenge score (input 'n' when you're done): "))
        if score >= 0 and score <= 100:
            grades.append(score)
        if type(score) != int:
            print('\n-------\nTry Again\n-------\n')
        if score == 'n':
            running == 2
    full_score = sum(grades)
    score_avg = full_score/(len(grades))
    pre_grade = score_avg * .15
    return pre_grade

def homework():
    running = 1
    grades = []
    while running == 1:
        score = int(input("Your homework score (input 'n' when you're done): "))
        if score >= 0 and score <= 100:
            grades.append(score)
        if type(score) != int:
            print('\n-------\nTry Again\n-------\n')
        if score == 'n':
            running == 2
    full_score = sum(grades)
    score_avg = full_score/(len(grades))
    pre_grade = score_avg * .30
    return pre_grade

def project():
    running = 1
    score1 = 0
    score2 = 0
    while running == 1:
        score1 = int(input("Input grade for project part 1: "))
        if type(score1) != int:
            print('\n-------\nTry Again\n-------\n')
        if score1 == 'n':
            running == 2
    score1 = score1 * .1

    while running == 2:
        score2 = int(input("Input grade for project part 2: "))
        if type(score2) != int:
            print('\n-------\nTry Again\n-------\n')
        if score2 == 'n':
            running == 3
    score2 = score2 * .15

    pre_score = score1 + score2
    return pre_score

def midterms():
    running = 1
    grades = []
    while running == 1:
        score = int(input("Your midterm score (input 'n' when you're done): "))
        if score >= 0 and score <= 100:
            grades.append(score)
        if type(score) != int:
            print('\n-------\nTry Again\n-------\n')
        if score == 'n':
            running == 2
    full_score = sum(grades)
    score_avg = full_score/(len(grades))
    pre_grade = score_avg * .10
    return pre_grade

def extra_credit():
    running = 1
    grades = []
    while running == 1:
        score = int(input("Your score (input 'n' when you're done): "))
        if score >= 0 and score <= 100:
            grades.append(score)
        if type(score) != int:
            print('\n-------\nTry Again\n-------\n')
        if score == 'n':
            running == 2
    full_score = sum(grades)
    score_avg = full_score/(len(grades))
    pre_grade = score_avg * .05
    return pre_grade


participation_grade = participation()
challenge_grade = challenge()
homework_grade = homework()
project_grade = project()
midterms_grade = midterms()

final_grade = participation_grade + challenge_grade + homework_grade + project_grade + midterms_grade

print(final_grade)
