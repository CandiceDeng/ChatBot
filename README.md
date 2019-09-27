# ChatterBot
Setup Instruction:
After downloading the file from Git branch, first install virtual environment in the terminal/bash by commands line by line : “
pip install virtualenv
virtualenv -p python3 .venv/
source .venv/bin/activate
cd ChatterBot/ChatBot
pip3 install -r requirements.txt
python manage.py runserver “ (without quotes)

Required packages:
ChatterBot==1.0.5
chatterbot-corpus==1.2.0
Django==2.2.5

Extra Information:
What went well:
Under Django framework, the MVC structure requires less consideration on how to distinguish and connect model, view, and controller of the application. And the usage of ChatterBot library gives the chatbot training data to make corresponding response to questions.
what was difficult
The handlebar to display each text input turns to have a conflict with django framework, which makes me stuck for a while
what you would improve if you had more time
Currently, the chatbot works on the basis of the ChatterBot package, rather than train its data based on user input. If more time provided, I tend to combine sklearn and nltk to gradually train the model from the backend.
