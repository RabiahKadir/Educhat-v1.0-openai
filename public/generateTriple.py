from nlpTagging import getTag
#from generategraph import visualizeRDFTriple
import rdflib
from rdflib import URIRef, BNode, Literal
import re 
import nltk
from nltk.stem import PorterStemmer
from objectsIdentifier import sub_DIObject

ps = PorterStemmer()

def defineTriple(s,p,o):
    return (s, p, o)

def createURIRef(namespace,entity):
    reference = "http://www."+namespace+".com/rdf#"+entity.replace(" ", "");
    return URIRef(reference);

def CreateblankNode():
    return BNode()

def createLiteral(value): #object only
    return Literal(value)

def getPhrase(query):
    sens = []
    print(query)
    phrase = re.split(r'[,.!\n]',query)
   # phrase = re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)(\s|[A-Z].,*)',query)
   # phrase = query.split('[.,!]')
    for ph in phrase:
        if(ph.strip() != ""):
            #print("line:"+ph);
            sens.append(ph.strip())
    return sens
        
def defineSPO(sen):
    (nouns, verbs, adverbs, adjectives) = getTag(sen)
    for nn in nouns: 
        tSub = nn
        tPredicate = ""
        for vb in verbs: 
            if vb != "are" and vb !="is":
                tPredicate = tPredicate + " "+ vb            
        tObj = ""
        for adv in adverbs: 
            tObj = tObj + " "+ adv      
        for adj in adjectives: 
            tObj = tObj + " "+ adj

    return defineTriple(tSub, tPredicate, tObj)
    
def createTriple(query):
    sentences = getPhrase(query)
    #empty graph
    graph = rdflib.Graph()
    print(len(graph))
    node = CreateblankNode()
    tripleMainSubject = URIRef("urn:educate:query")  #object
    tripleMainObject = URIRef("urn:educhat:data")
    tripleMainPredicate = URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#_4") #predicate
    graph.add((tripleMainSubject, tripleMainPredicate, tripleMainObject))

    for sen in sentences:
        print(sen)
        (s,d,i)=sub_DIObject(sen) 
        if (s and d or i !=""):   
            if (s != ""):
                print('subject:', s)
            if d != "":
                print('object:', d)
            if i != "":
                print('object:', i)

            (nouns, verbs, adverbs, adjectives) = getTag(sen)

            continue
       
        (nouns, verbs, adverbs, adjectives) = getTag(sen)
        # if len(nouns) > 0:
        #     print("nouns:",nouns)
        # if len(verbs) > 0:
        #     print("verbs:", verbs)
        # if len(adverbs) > 0:
        #     print("adverbs:", adverbs)
        # if len(adjectives) > 0:
        #     print("adjectives:", adjectives)
        count = -1
        for nn in nouns: 
            # snn = ps.stem(nn)
            # print(snn)
            # nounTag = nltk.pos_tag([snn])
            # print(nounTag)
            count+=1
            if nn == "Does":
                continue
            tSub = nn
            tPredicate = ""
            predictCount = 0
            for vb in verbs: 
                if predictCount < 2:
                    if vb != "are" and vb !="is":
                        tPredicate = tPredicate + " "+ vb   
                        predictCount +=1
                if predictCount==3:
                    tPredicate = ""
                if predictCount>=3:
                    if vb != "are" and vb !="is":
                        tPredicate = tPredicate + " "+ vb   
                        predictCount +=1        
            tObj = ""
            for adv in adverbs: 
                tObj = tObj + " "+ adv      
            for adj in adjectives: 
                tObj = tObj + " "+ adj
            if tObj == "":
                if count<len(nouns)-1:
                    tObj = nouns[count+1]
                    nouns.remove(tObj)
                
            (s,p,o) = defineTriple(tSub, tPredicate, tObj)
            print("Subject:"+s)
            print("Predicate:"+p)
            print("Object:"+o)     
            
            if(s != ""):
                triRefToSubject = tripleMainObject  
                triRefToSubjData= createURIRef("educhat","class")
                tripleSubData= Literal(s)
                graph.add((triRefToSubject, triRefToSubjData, tripleSubData))
            if(p != ""):
                triRefToPredData = createURIRef("educhat",p)
                triplePredData = Literal(p)           
                graph.add((tripleSubData, triRefToPredData, triplePredData))
            if(o != ""):    
                triRefToObjData= createURIRef("educhat",o)
                tripleObjectData = Literal(o)           
                graph.add((tripleSubData, triRefToObjData, tripleObjectData))
    return graph

# #query = "The children are still not good at starting ... there are guidelines"
# query = "How to login into the system"
# tripleQuery = createTriple(query)
# print(len(tripleQuery))
# print(tripleQuery.serialize())
# tripleQuery.serialize(format="xml",destination="query.rdf")
# visualizeRDFTriple("query.rdf", 'xml')