# # class People:
# #     def __init__(self, name, age) :
# #         self.name = name
# #         self.age = age
# #         print('Я родился')

# #     def info(self):
# #         print(f'{self.name} {self.age}')

# # people1 = People('Pavel', 21)


# # # 2 строчки равнозначны
# # people1.info()
# # People.info(people1)


# # Родительский класс
# class A:
#     def __init__(self, q,w,e,r,t):
#         self.q = q  
#         self.w = w 
#         self.e = e  
#         self.r = r 
#         self.t = t

#     def one(self):
#         print('one is A')

#     def two(self):
#         print('two is A')

# # class C:
# #     # def onec(self):
# #     #     print('onec is C')
# #     def one(self):
# #         print('one is C')
# #     def twoc(self):
# #         print('twoc is C')


# # Дочерний класс, наследует A и C
# class B(A):   # Если сначала наследуется one из A, а потом из C, то b.one ==> one is A. Если сначала C, затем A, то one is C
#     # # плохой способ (если надо скопировать аргументы родителя и добавить новый)
#     # def __init__(self, q,w,e,r,t, new):    
#     #     self.q = q  
#     #     self.w = w 
#     #     self.e = e  
#     #     self.r = r 
#     #     self.t = t
#     #     self.new = new


#     # Хороший способ
#     def __init__(self, q,w,e,r,t, new):
#         super().__init__(q,w,e,r,t) #вызов родительского метода
#         self.new = new

#     def one(self):
#         return super().one()
#     # one is A

#     def three(self):
#         print('three is B')


# a = A(1,2,3,4,5)
# a.one()
# a.two()
# print("-"*50)
# b = B(1,2,3,4,5, 'xz')    # если в родительском классе есть атрибуты, они должны быть и в дочернем
# b.one()
# b.two()
# b.three()
# # b.onec()


# ============================================================================================================================================================
import random


class Tank:
    def __init__(self, model, armor, min_damage, max_damage, health):
        self.model = model
        self.armor = armor 
        self.damage = random.randint(min_damage, max_damage)
        self.health = health

    def info(self):
        print(f'Model: {self.model}, броня: {self.armor}, урон: {self.damage}, здоровье: {self.health}')

    def shot(self, enemy):
        damageDrop = self.damage * enemy.armor / 100
        finalDamage = self.damage - damageDrop
        enemy.health -= round(finalDamage, 2)
        print(f"Выстрел {self.model}")
        print(f"Точно в цель, у противника {enemy.model} осталось {round(enemy.health, 2)} единиц здоровья")



   