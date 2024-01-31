#ABSTRACTION  in which a class hides its properties only working is known
class ANIMAL:
    def ATTACK(self):
        pass
class DOG(ANIMAL):
    def ATTACK(self):
        print("I can bow bow")
class CAT(ANIMAL):
    def ATTACK(self):
        print("I  can meow meow")
D = DOG()
C = CAT()
D.ATTACK()
C.ATTACK()