# # Программа "Сотрудники и зарплаты"

# # Простая реализация работника
# name = 'Игорь'
# salary = 200_000    # 200000 и 200_000 равнозначны

# # Вывод информации на экран
# print(f'Имя работника: {name}, зарплата в месяц: {salary}')
# print(f'Зарплата в месяц: {salary *12}')

# # ==================================================================================================================================================================================================
# # Реализация работника через словарь

# employ = {
#     'name':'Игорь', 
#     'salary':200_000
# }


# # Список с работниками:
# employees = [
#     {'name': 'Игорь', 'salary': 200_000},
#     {'name': 'Вадим', 'salary': 150_000},
#     {'name': 'Антон', 'salary': 250_000}
#                     ]
# print(employees[0])


# # Увольняем Игоря
# for empl in employees:
#     if empl['name'] == 'Игорь':
#         employees.remove(empl)
#         break

# print(employees)


# # Нанимаем нового сотрудника
# new_employee = {
#     'name': 'Кирил', 'salary': 200_000
# }

# employees.append(new_employee)
# print(employees)


# # Узнаем кол-во сотрудников
# print(f'Количество сотрудников: {len(employees)}')


# =====================================================================================================================================================================================================
# Реализация сотрудника в виде Класса

class Employee:
    def __init__(self, name, salary):
        self.name = name 
        self.salary = salary 
        
        # Сотрудник в отпуске?
        self.on_vacation = False


    # метод получения текущей информации по сотруднику
    def get_info(self):
        return f'У сотрудника по имени {self.name} З/П в месяц: {self.salary}. Сотрудник в отпуске: {self.on_vacation}'
    



# Создаю список сотрудников:
employees = [Employee('Игорь', 200_000), Employee('Никита', 250_000), Employee('Роман', 300_000)]

# Вывожу информацию о всех сотрудниках 
for employee in employees: 
    print(employee.get_info())

# Добавляем нового сотрудника:
new_name = input('Введите имя сотрудника: ')
new_salary = int(input('Введите зарплату нового сотрудника: '))

employees.append(Employee(new_name, new_salary))

for employee in employees:
    print(employee.get_info())