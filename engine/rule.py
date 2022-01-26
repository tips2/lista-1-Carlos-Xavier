import json
from engine.method import Backward, Forward


class KnowledgeBase:
    def __init__(self):
        self.knowledgeBase = None

    def getKnowledgeBase(self, inputFile):
        with open(inputFile, "r") as file:
            file = json.load(file)

            if file["method"] == 'forward':
                knowledgeBase = Forward(file['initialData'], file['goal'])
                start = 'initialData'
            else:
                knowledgeBase = Backward(file['initialData'], file['goal'])
                start = 'goal'

            for item in file[start]:
                knowledgeBase.addMT(item)
            
            for rule in file['rules']:
                knowledgeBase.addRule(IF=rule[0], THEN=rule[1])

            knowledgeBase.method = file["method"]
            self.knowledgeBase = knowledgeBase

        return self.knowledgeBase