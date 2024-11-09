from datetime import datetime
import time


class Quest:
    def __init__(self, name, goal, description):
        self.name = name
        self.goal = goal
        self.description = description
        self.start_time = None
        self.end_time = None

    def __str__(self):
        about_quest = 'Цель квеста ' + self.name + ' - ' + self.goal
        if self.end_time:
            return (f'{about_quest} Квест завершён.')
        if self.start_time:
            return (f'{about_quest} Квест выполняется.')
        return (about_quest)

    def accept_quest(self):
        if self.end_time:
            return ('С этим испытанием вы уже справились.')
        else:
            self.start_time = datetime.now()
            return (f'Вы взяли квест в {self.start_time}')

    def pass_quest(self):
        if not self.start_time:
            return ('Нельзя завершить то, что не имеет начала!')
        else:
            self.end_time = datetime.now()
            completion_time = self.end_time - self.start_time
            return (
                f'Квест "{self.name}" окончен.'
                f'Время выполнения квеста: {completion_time}')


# Объявите класс Quest с методами и свойствами.
# В этих переменных содержатся значения, которые нужно передать
# в качестве аргументов в экземпляр класса Quest.
quest_name = 'Сбор пиксельники'
quest_goal = 'Соберите 12 ягод пиксельники.'
quest_description = '''
В древнем лесу Кодоборье растёт ягода "пиксельника".
Она нужна для приготовления целебных снадобий.
Соберите 12 ягод пиксельники.'''
# Создайте экземпляр класса Quest.
new_quest = Quest(quest_name, quest_goal, quest_description)
print(new_quest.pass_quest())
print(new_quest.accept_quest())
time.sleep(3)
print(new_quest.pass_quest())
print(new_quest.accept_quest())


# Печатаем объекта класса Quest:
print(new_quest)
