#QuizGenerator - создает экзаменационные билелы с вопросами и ответами, расположенными в случайном порядке
import random
capitals = { 'Alabama': 'Montgomery','Alaska': 'Juneau','Arizona':'Phoenix','Arkansas':'Little Rock','California': 'Sacramento',
    'Colorado':'Denver', 'Connecticut':'Hartford', 'Delaware':'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta','Hawaii': 'Honolulu','Idaho': 'Boise',
    'Illinios': 'Springfield','Indiana': 'Indianapolis','Iowa': 'Des Monies','Kansas': 'Topeka','Kentucky': 'Frankfort','Louisiana': 'Baton Rouge',
    'Maine': 'Augusta','Maryland': 'Annapolis','Massachusetts': 'Boston','Michigan': 'Lansing','Minnesota': 'St. Paul',
    'Mississippi': 'Jackson','Missouri': 'Jefferson City','Montana': 'Helena','Nebraska': 'Lincoln','Neveda': 'Carson City','New Hampshire': 'Concord',
    'New Jersey': 'Trenton','New Mexico': 'Santa Fe','New York': 'Albany','North Carolina': 'Raleigh',
    'North Dakota': 'Bismarck','Ohio': 'Columbus','Oklahoma': 'Oklahoma City','Oregon': 'Salem','Pennsylvania': 'Harrisburg',
    'Rhoda Island': 'Providence','South Carolina': 'Columbia','South Dakoda': 'Pierre','Tennessee': 'Nashville','Texas': 'Austin',
    'Utah': 'Salt Lake City','Vermont': 'Montpelier','Virginia': 'Richmond','Washington': 'Olympia','West Virginia': 'Charleston','Wisconsin': 'Madison','Wyoming': 'Cheyenne' }
for quizNum in range(35):
    #Создание файлов билетов и ответовs
    quizFile = open('capitalsquiz%s.txt' % (quizNum + 1), 'w')
    answerKeyFile = open('capitalsquiz_answers%s.txt'  % (quizNum + 1), 'w')
    #Запись заголовка
    quizFile.write('Имя:\n\nДата:\n\nКурс:\n\n')
    quizFile.write((' ' * 15) + 'Проверка знания столиц штатов (Билет %s)' % (quizNum +1))
    quizFile.write('\n\n')
    #Случайный порядок
    states = list(capitals.keys())
    random.shuffle(states)
    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers, 3)
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)
        #Запись вопросов и ответов в файл
        quizFile.write('%s. Выберите столицу штата %s.\n' % (questionNum + 1, states[questionNum]))
        for i in range(4):
            quizFile.write(' %s. %s\n' % ('ABCD' [i], answerOptions[i]))
        quizFile.write('\n')
        answerKeyFile.write('%s. %s\n' % (questionNum +1, 'ABCD' [answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerKeyFile.close()
