class Rule:
    def __init__(self, IF, THEN):
        if IF.split("&"):
            self.IF = IF.split("&")
            self.IF = [x.strip(' ') for x in self.IF]
        else:
            self.IF = IF
        self.THEN = THEN.split("=")[0].strip()
        self.action = self.getAction(THEN.split("="))

    def getAction(self, THEN):
        if THEN[1]:
            return True
        return False


class Inference:
    def __init__(self, initialData, goal):
        self.goal = goal
        self.initialData = initialData
        self.MT = list()
        self.rules = list()
        self.auxMT = list()
        self.method = None
        self.answer = True
    
    def setAnswer(self, flag):
        self.answer = flag

    def addRule(self, IF, THEN):
        self.rules.append(Rule(IF, THEN))
    
    def addMT(self, value):
        self.MT.extend(value)
        self.auxMT.append(value)

    def __str__(self):
        data = list()
        data.append("MT : ")
        data.append(self.MT)
        data.append("\n\n")
        for rule in self.rules:
            data.append("".join(rule.IF))
            data.append("  =>  ")
            data.append(rule.THEN[0])
            data.append("\n")
        return "".join(data)


class Backward(Inference):
    def __init__(self, initialData, goal):
        super().__init__(initialData, goal)
    
    def remove(self, value):
        for item in value:
            list_remove = []
            for index, rule in enumerate(self.MT):
                if rule == item:
                    list_remove.append(index)
            
            if len(list_remove) > 1:
                list_remove.pop(0)

            for i in list_remove:
                self.MT.pop(i)

        self.auxMT.remove(value)


class Forward(Inference):
    def __init__(self, initialData, goal):
        super().__init__(initialData, goal)
        self.goalIF = dict()
        self.goalArr = []
        self.goalIndex = None

    def setGoalIF(self, values, flag):
        for item in values:
            self.goalIF[item] = flag
    
    def setGoalArr(self, arr, index):
        self.goalArr = arr
        self.goalIndex = index+1
