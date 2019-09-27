from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings

from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
import os



chatbot = ChatBot(**settings.CHATTERBOT)

trainer = ListTrainer(chatbot)

for files in os.listdir(os.getcwd() + '/ChatBot/' + 'data/english/'):
    data = open(os.getcwd() + '/ChatBot/' + 'data/english/'+files, 'r').readlines()
    trainer.train(data)


def GetResponse(userInput):
    if userInput != 'Bye':
        reply = chatbot.get_response(userInput)
        response = str(reply)
        return response
    else:
        return 'Bye'
        

    
