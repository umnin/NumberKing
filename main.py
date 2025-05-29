import random, time

class MathKing_:
    def __init__(self):
        mk = random.randint(5,10)
        self.setM(mk)
        self.round = 0  # 初始化属性
    
    def getName(self):
        return "数字之王"

    def setM(self, m):
        self.M = m
        
    def getM(self):
        return self.M
    
    def RAdd(self):
        mAdd = self.M + random.randint(0,3)
        self.setM(mAdd)
    
    def setRound(self):
        r = random.random()
        if r <= 0.5:
            self.round = random.randint(3,7)
        elif r < 0.65:
            self.round = 10
        else:
            self.round = random.randint(2,4)
        print("回合已更新")
    
    def getRound(self):
        return self.round

    class Magic:
        @staticmethod
        def TheEnd():
            pass

class Player_:
    def __init__(self):
        pl = random.randint(1,5)
        self.setM(pl)
    
    def setName(self, name):
        self.n = name

    def getName(self):
        return self.n
    
    def setM(self, p):
        self.P = p
        
    def getM(self):
        return self.P
    
    def RAdd(self):
        pAdd = self.P + random.randint(1,2)
        self.setM(pAdd)
    
    class Power:
        @staticmethod
        def Life():
            pass

class Rule:
    def __init__(self):
        pass

def gameStart():
    mk = MathKing_()
    pl = Player_()
    pl.setName("umnin")
    
    print(mk.getName())
    print("VS")
    print(pl.getName())

    time.sleep(1)
    print("一切才刚刚开始")
    time.sleep(1)
    print(f"{mk.getName()}:点数:{mk.getM()}")
    print(f"{pl.getName()}:点数:{pl.getM()}")
    time.sleep(1)
    mk.setRound()
    round = mk.getRound()
    print(f"{mk.getName()}给出的回合数是 {round}")
    print("活下去！！！")

    while(round != 0):
        mk.RAdd()
        pl.RAdd()
        print(f"{mk.getName()}:点数:{mk.getM()}")
        print(f"{pl.getName()}:点数:{pl.getM()}")
        time.sleep(1)
        
        round = round - 1
        print(round)
    

gameStart()