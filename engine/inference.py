from engine.rule import KnowledgeBase

class Inference:
    def __init__(self):
        self.goal = None
        self.knowledge = KnowledgeBase()

    def start(self, knowledge):
        self.knowledge = self.knowledge.getKnowledgeBase(knowledge)

        if self.knowledge.method == "forward":
            self.getGoalIF()
            self.runForward(self.knowledge.MT[0])
            self.knowledge.setAnswer(self.checkForwardGoal())
        elif self.knowledge.method == "backward":
            self.runBackward()

        self.print()

    def runForward(self, next):
        for index, rule in enumerate(self.knowledge.rules):
            if (next == rule.IF) or (next in rule.IF):
                if next in self.knowledge.goalArr:
                    self.knowledge.setGoalIF(next, True)
                
                if self.knowledge.goal == rule.THEN:
                    if self.checkForwardGoal():
                        self.knowledge.addMT(rule.THEN)
                else:
                    self.knowledge.addMT(rule.THEN)
                for item in rule.THEN:
                    self.runForward(item)

    def checkForwardGoal(self):
        count = 0
        for key, value in self.knowledge.goalIF.items():
            if value:
                count += 1
        if len(self.knowledge.goalIF) != count:
            return False 
        return True
    
    def getGoalIF(self):
        for index, rule in enumerate(self.knowledge.rules):
            if rule.THEN == self.knowledge.goal:
                self.knowledge.setGoalIF(rule.IF, False)
                self.knowledge.setGoalArr(rule.IF, index)

    def check(self, ruleActivated, i, stop):
        if i >= stop:   return -1

        points = 0
        for item in ruleActivated[i]:
            for rule in self.knowledge.rules:
                if rule.THEN == item or item in self.knowledge.initialData:
                    points += 1
                    break

        if points >= len(ruleActivated[i]):
            return i
    
        return self.check(ruleActivated, i+1, stop)
            
    def runBackward(self):
        for mt in self.knowledge.MT:
            ways = 0
            rules = []
            for rule in self.knowledge.rules:
                if mt == rule.THEN:
                    ways += 1
                    if not self.checkForward(rule.IF):
                        self.knowledge.addMT(rule.IF)
                        rules.append(rule.IF)

            if len(rules) > 0:
                id_save = self.check(rules, 0, ways)
                if id_save != -1:
                    self.remove(rules[id_save], rules)
                else:
                    self.remove(rules, rules, id_save)
                    self.knowledge.setAnswer(False)
                    break

    def print(self):
        print(f"\n### Método: {self.knowledge.method} ###\n")
        for mt in self.knowledge.auxMT:
            for index, rule in enumerate(self.knowledge.rules):
                if mt == rule.IF or mt in rule.IF and rule.IF != self.knowledge.goalArr:
                    print(f"Regra {index + 1} ativada : {self.knowledge.rules[index].IF} => {self.knowledge.rules[index].THEN}")
                

        if self.knowledge.answer:
            if self.knowledge.method == "forward":
                print(f"Regra {self.knowledge.goalIndex} ativada : {self.knowledge.goalArr} => {self.knowledge.goal}")
            print(f"\n\n** Objetivo encontrado: {self.knowledge.goal} **\n")
        else:
            print("\n\n** Não foi possível achar o objetivo! **\n\n")

        print(f"MT: {self.knowledge.MT}")

    def remove(self, save, arrUpdate, id_save=0):
        if id_save != -1:
            arr = []
            for item in arrUpdate:
                if item != save:
                    arr.append(item)
        else:
            arr = arrUpdate

        for item in arr:
            self.knowledge.remove(item)

    def checkForward(self, rule):
        return True if set(rule).issubset(set(self.knowledge.MT)) else False

