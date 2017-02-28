

def average_score():
    """Вычисляет среднюю оценку за домашки по каждому студенту, добавляет в словарь этого студента, вычисляет
    среднюю оценку по всем студентам. Ничего не возвращает.
    Добавляет в словари среднюю оценку каждому студенту по формуле 0.6 + 0.4"""
    for i in range(len(students)):
        aver_rating_hw = (sum(students[i]['home_work_rating'])) / len(students[i]['home_work_rating'])
        average_all_score_for_one = 0.6 * aver_rating_hw + 0.4 * students[i]['exam_rating']
        students[i]['aver_rating'] = aver_rating_hw
        students[i]['average_total_score_one'] = average_all_score_for_one


def average_total_scores(key1, key2):
    """Вычисление средней оценки по всем студентам. На всякий случай возвращаем и средние оценки по
    домашним работам и по экзаменам по отдельности"""
    average_total_score_hw = 0
    average_total_score_exam = 0
    for i in range(len(students)):
        average_total_score_hw += students[i][key1] / len(students)
        average_total_score_exam += students[i][key2] / len(students)
    average_total_score = (average_total_score_hw + average_total_score_exam) / 2
    return average_total_score, average_total_score_hw, average_total_score_exam


def average_sex_scores(key, value):
    """Вычисление средней оценки в зависимости от ключа
    записи и варианта значения по этому ключу """
    n = 0
    av_rating_value = 0
    for i in range(len(students)):
        if students[i][key] == value:
            av_rating_value += (students[i]['aver_rating'] + students[i]['exam_rating']) / 2
            n += 1
    av_rating_values = av_rating_value / n
    return av_rating_values, n


def hi_score_student():
    """В отдельный список добавляем среднюю оценку каждого студента,
    находим индекс максимальной оценки. По индексу находим имя и фамилию студента"""
    interim = []
    for i in range(len(students)):
        interim.append(students[i]['average_total_score_one'])
    q_max = max(interim)
    e = interim.index(max(interim))
    name1 = students[e]['name'] + ' ' + students[e]['surname']
    if interim.count(max(interim)) == 1:
        print('У студента {} наибольший балл {}'.format(name1, q_max))
    else:
        for r in range(len(interim)):
            if interim[r] == q_max:
                name = students[r]['name'] + ' ' + students[r]['surname']
                print('Студент {} получил максимальный балл {}'.format(name, q_max))


students = [
    {'ID': '23456', 'name': 'Ivan', 'surname': 'Ivanov', 'sex': 'male',
    'prog_exp': 0, 'home_work_rating': [5, 10, 5, 2, 5], 'exam_rating': 2},
    {'ID': '23457', 'name': 'Andrew', 'surname': 'Gusev', 'sex': 'male',
    'prog_exp': 1, 'home_work_rating': [8, 7, 5, 3, 5], 'exam_rating': 3},
    {'ID': '23458', 'name': 'Sara', 'surname': 'Jonson', 'sex': 'female',
    'prog_exp': 1, 'home_work_rating': [5, 10, 5, 10, 5], 'exam_rating': 10},
    {'ID': '23459', 'name': 'Sergey', 'surname': 'Vasiliev', 'sex': 'male',
    'prog_exp': 1, 'home_work_rating': [5, 3, 5, 5, 5], 'exam_rating': 5},
    {'ID': '23460', 'name': 'Vadim', 'surname': 'Svetlov', 'sex': 'male',
    'prog_exp': 0, 'home_work_rating': [5, 10, 5, 10, 5], 'exam_rating': 10},
    {'ID': '23461', 'name': 'Sveta', 'surname': 'Ivanova', 'sex': 'female',
    'prog_exp': 1, 'home_work_rating': [5, 10, 5, 10, 5], 'exam_rating': 1}
]

average_score()

print("Введите число, чтобы получить информацию:")
print("1 - средняя оценка по всем студентам")
print("2 - средняя оценка в разрезе пола студентов")
print("3 - средняя оценка в разрезе опыта в программировании студентов")
print("4 - студент с лучшим средним баллом")
request = input()
if request == '1':
    print("Средняя оценка за домашние работы и экзамены по всем студентам:\n {:*^20.2f}".format(average_total_scores\
                                                                        ('aver_rating', 'exam_rating')[0]))
elif request == '2':
    print("Средняя оценка {:.2f} у {} мужчин-студентов".format(*average_sex_scores('sex', 'male')))
    print("Средняя оценка {:.2f} у {} девушек-студенток".format(*average_sex_scores('sex', 'female')))
elif request == '3':
    print("{:.2f} - Средняя оценка у {} студентов с опытом программирования".format(*average_sex_scores('prog_exp', 1)))
    print("{:.2f} - Средняя оценка у {} студентов без опыта программирования".format(*average_sex_scores('prog_exp', 0)))
elif request == '4':
    hi_score_student()
else:
    print("Неправильный ввод.")