from chatterbot import ChatBot
import time
time.clock = time.time

bot = ChatBot('Buddy',
            logic_adapters=[{
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }],
            read_only = True,
            preprocessors=['chatterbot.preprocessors.clean_whitespace',
                        'chatterbot.preprocessors.unescape_html',
                        'chatterbot.preprocessors.convert_to_ascii']
                        )



file = open('c:/xampp/htdocs/ChatBot/chatbot-main/db_main.txt', 'r')
text = file.read()
file.close()
request = text
response=bot.get_response(request)
print(response)
