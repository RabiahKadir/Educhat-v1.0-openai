from googletrans import Translator

def convertToEnglish(text):
    translator = Translator()
    type = translator.detect(text)
    
    if (str(type.lang) == "ms"):
        res = (translator.translate(text, dest='en')).text
    elif str(type.lang) == "en":
        res = text
    else: 
        res = "unknown language";
    return res 
