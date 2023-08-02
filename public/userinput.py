from bmtoEngtranslator import convertToEnglish
from nlpTagging import getTag, analyseSenTag
from sparqlQuery import findObject
from checkClass import findSentenceType
import rdflib
from generateTriple import createTriple
from googletrans import Translator
import warnings
warnings.filterwarnings('ignore')

#buat objek Translator
penterjemah = Translator()



def userqueries (query):
        
    graph = rdflib.Graph()
#edit path20221107T145819Z
#C:\Users\Aimi\Desktop\Python engine Educhat\resources-20221107T145819Z-001\resources
    graph.parse("resources/educhatModel.rdf") ##
    #print(len(graph))
    #visualizeRDFTriple("./Final/educhatModel.rdf", 'xml')
        
    #print("Enter Question")
    #query = input("Enter Query:")   
    #query = "Good morning, how to login into the system"

    # membuka file dengan mode read ('r')
    file = open('db.txt', 'r')

    # membaca isi file dan menyimpannya ke dalam variabel text
    text = file.read()

    # menutup file setelah selesai digunakan
    file.close()

    ###// insert from laravel
    #query = "what are the subjects available?"
    #query = 'Bagaimana cara pembelajaran mengunakan HomeTutor dan bagaimana Hometutor dapat membantu pelajar.'
   #lakukan penterjemahan menggunakan fungsi translate(['teks asal 1,'teks asal 2',...],src=kode_bahasa_sumber, dest=kode_bahasa_tujuan)
    query = penterjemah.translate(text, dest='en')

    #query = 'Adakah Hometutor menyediakan bahan pembelajaran atau guru yang akan mengajar ?'
    query = (query.text)
    # print("result:",query)
    print(query)
    sentences, types = findSentenceType(query)
    # print("sentences:",sentences)
    # print("sentences Type:",types)
    print(sentences)
    print(types)
    
    currSen = 0
    possible_solutionS = []
    possible_solutionP = []
    possible_solutionO = []
    for sen in sentences:
        if(types[currSen] != "gr"):
            # print("current sentence: ",sen)
            # print("result:",query,"sentences:",sentences,"type:",types,"current sentence:",sen)
            (nouns, verbs, adverbs, adjectives) = getTag(sen)
            #print("Noun Tag:", nouns)
            if len(nouns)>0: 
                for nn in nouns:
                    tempResult = findObject(graph,nn)
                    if(len(tempResult)>0):
                        possible_solutionS.append(tempResult)
            if len(verbs)>0: 
                for vb in verbs:
                    tempResult = findObject(graph,vb)
                    if(len(tempResult)>0):
                        possible_solutionP.append(tempResult)
            if len(adverbs)>0: 
                for ad in adverbs:
                    tempResult = findObject(graph,ad)
                    if(len(tempResult)>0):
                        possible_solutionO.append(tempResult)
            if len(adjectives)>0: 
                for adj in adjectives:
                    tempResult = findObject(graph,adj)
                    if(len(tempResult)>0):
                        possible_solutionO.append(tempResult)

        # (s,p,o) = defineSPO(sen)
        # analyseSenTag(sen)
        # if s != "":
        #     tempResult = findObject(graph,s)
        #    # print(tempResult)
        #     if(len(tempResult)>0):
        #         possible_solutionS.append(tempResult)
        # if p !="":
        #     tempResult = findObject(graph,p)
        #    # print(tempResult)
        #     if(len(tempResult)>0):
        #         possible_solutionP.append(tempResult)
        # if o !="":
        #     possible_solutionO.append(findObject(graph,o)) 
            
    tripleQuery = createTriple(sen)
    # print(tripleQuery.serialize())


    print("Recommended Solution:")
    if len(possible_solutionS)>0:
        for sol in possible_solutionS:
            if(sol !=""):
                print("subject:", str(sol))
        if len(possible_solutionP)>0:
            for sol in possible_solutionP:
                if(sol !=""):
                    print("Predicate:", str(sol))
            if len(possible_solutionO)>0:
                for sol in possible_solutionO:
                    if(sol !=""):
                        print("Object:", str(sol))

##recall this function
##print('Enter you text')
##userqueries = input('halo apa kabar ?')

# membuka file dengan mode read ('r')
file = open('db.txt', 'r')

# membaca isi file dan menyimpannya ke dalam variabel text
text = file.read()

# menutup file setelah selesai digunakan
file.close()

# memanggil fungsi userqueries dengan mengirimkan isi file sebagai argumen
##userqueries = input('halo apa kabar ?')
userqueries(text)