a = "hello" + " " + "world" + "!"
b = 1 + 2 + 3 + 4 + 5

print(type(a), type(b), id(a), id(b))
print(type(id), id(id))
print(type(type), id(type))

class A:
    def public(self):
        return 42
    def _private(self):
        return "privat"
    def __protect(self):
        return True
    
a = A()
print(a.public())
print(a._private()) # В принципе, так можно сделать. Но тк перед private идет _ , то становится ясно: разработчик НЕ ПРЕДУСМАТРИВАЛ возможности его вызова, и делать этого не стоит
print(a.__protect())    # А вот этот метод не получится вызвать впринципе, единственный в Python пример правильной работы инкапсуляции.
#                                   УТОЧНЕНИЕ: ЭТИ МЕТОДЫ С _ СОЗДАНЫ ДЛЯ РАБОТЫ С НИМИ ВНУТРИ ИХ/ДОЧЕРНЕГО КЛАССА


