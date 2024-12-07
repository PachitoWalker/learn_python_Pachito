from main import *



class SuperTank(Tank):
    def __init__(self, model, armor, min_damage, max_damage, health, doubleShotVar):
        super().__init__(model, armor, min_damage, max_damage, health)
        self.doubleShotVar = doubleShotVar

    def shot(self, enemy):
        if random.randint(1,100) <= self.doubleShotVar:
            print('\n Двойной выстрел !!!')
            super().shot(enemy)
            super().shot(enemy)
        else:
            super().shot(enemy)


tank1 = Tank("Pz.Kpfw. I", 10, 50, 75, 340)
tank1.info()

tank2 = SuperTank("T80", 15, 35, 55, 376, 15)
tank2.info()    



while True:
    if tank1.health <= 0 and tank2.health <= 0:
        print("\n Ничья!")
        break
    elif tank1.health <= 0:
        print(f"\n Победил {tank2.model}")
        break
    elif tank2.health <= 0:
        print(f"\n Победил {tank1.model}")
        break   
    tank1.shot(tank2)
    tank2.shot(tank1)

