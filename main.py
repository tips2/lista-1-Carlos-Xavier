from engine.inference import Inference


knowledgeBaseFile = "./data/knowledge.json"

inference = Inference()
inference.start(knowledgeBaseFile)
