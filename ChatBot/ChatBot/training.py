from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os

def Training():
    chatbot = ChatBot('Bot')
    chatbot.set_trainer(ListTrainer)

    for files in os.listdir('data/english/'):
        data = open('data/english/'+files, 'r').readlines()
        chatbot.train(data)


Training()