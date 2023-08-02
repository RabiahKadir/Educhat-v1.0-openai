import spacy as sp
import nltk

NER = sp.load('en_core_web_sm')

# #FB: salam cikgu saya nak tanya.. pasword nur alma Batrisya macam mana ya. boleh tak cikgu bagi semula
# query1 = "Greetings teacher, I want to ask .. what kind of password is Nur Alma Batrisya? Can you please share again"
# #FB: kenapa saya tak boleh buka
# query2 = "why can't I open it"
# #WhatApp: general learning tu dekat mana ye tak jumpa pun
# query3 = "General learning is close to where you can't find it"
# #whatApp: assalamualaikum cikgu, macam mana saya nak register email wife saya sekali untuk received info
# query4 = "assalamualaikum teacher, how do I register my wife's email once to receive info"
# #excel - 13: tunjukkan jalan kerja
# query5 = "show me the way it works"
# #excel -19: minta penerangan
# query6 = "ask for an explanation"
# #excel - 43: "Apa maksud iri hati
# query7 = "What does envy mean"
# #excel  49:- "Saya tak faham
# query8 = "I do not understand"
# #excel - 53 : Parent Code : QUPSRBM104837, sudah jatuh ditimpa tangga
# query9 = "Parent Code: QUPSRBM104837, has fallen on the stairs"
# #excel - 56: Parent Code : QLPRIMTE126118, jalan kerja dalam answer scheme salah
# query10 = "Parent Code: QLPRIMTE126118, the working path in the answer scheme is incorrect"

# queries = [query1,query2,query3,query4,query4,query6,query7,query8,query9,query10]

def cleanParentCode(query):
    if query.startswith('Parent Code:'): 
        commaIndexLoc = query.find(',')
        query = query[commaIndexLoc+1:]
    return query

def getTag(i):
    i = cleanParentCode(i) 
    
    tag = nltk.pos_tag(nltk.word_tokenize(i))
    # print("Tag: ",tag)
    print(tag)
    
    
    nouns = [token for token, 
             pos in tag 
             if pos.startswith('N')]
    verbs = [token for token, 
             pos in tag
             if pos.startswith('V')]
    adjectives = [token for token, 
             pos in tag 
             if pos.startswith('J')]
    adverbs = [token for token, 
             pos in tag 
             if pos.startswith('RB')]
    return (nouns,verbs,adverbs,adjectives)

def analyseSenTag(i):
    print("Sentence:",i)
    (nouns, verbs, adverbs, adjectives) = getTag(i)
    if len(nouns)>0:     
        print("nouns:",nouns)
    if len(verbs)>0: 
        print("verbs:",verbs)
    if len(adverbs)>0: 
        print("adverbs:",adverbs)
    if len(adjectives)>0: 
        print("adjectives:",adjectives)

def PrintTag(nouns,verbs,adverbs,adjectives):
    if len(nouns)>0:     
        print("nouns:",nouns)
    if len(verbs)>0: 
        print("verbs:",verbs)
    if len(adverbs)>0: 
        print("adverbs:",adverbs)
    if len(adjectives)>0: 
        print("adjectives:",adjectives)
     

'''
for i in queries:
    print(i)
    (nouns, verbs, adverbs, adjectives) = getTag(i)
    if len(nouns)>0:     
        print("nouns:",nouns)
    if len(verbs)>0: 
        print("verbs:",verbs)
    if len(adverbs)>0: 
        print("adverbs:",adverbs)
    if len(adjectives)>0: 
        print("adjectives:",adjectives)
   '''     
 
 
'''
CC	coordinating conjunction
CD	cardinal digit
DT	determiner
EX	existential there
FW	foreign word
IN	preposition/subordinating conjunction
JJ	This NLTK POS Tag is an adjective (large)
JJR	adjective, comparative (larger)
JJS	adjective, superlative (largest)
LS	list market
MD	modal (could, will)
NN	noun, singular (cat, tree)
NNS	noun plural (desks)
NNP	proper noun, singular (sarah)
NNPS	proper noun, plural (indians or americans)
PDT	predeterminer (all, both, half)
POS	possessive ending (parent\ ‘s)
PRP	personal pronoun (hers, herself, him, himself)
PRP$	possessive pronoun (her, his, mine, my, our )
RB	adverb (occasionally, swiftly)
RBR	adverb, comparative (greater)
RBS	adverb, superlative (biggest)
RP	particle (about)
TO	infinite marker (to)
UH	interjection (goodbye)
VB	verb (ask)
VBG	verb gerund (judging)
VBD	verb past tense (pleaded)
VBN	verb past participle (reunified)
VBP	verb, present tense not 3rd person singular(wrap)
VBZ	verb, present tense with 3rd person singular (bases)
WDT	wh-determiner (that, what)
WP	wh- pronoun (who)
WRB	wh- adverb (how)
'''