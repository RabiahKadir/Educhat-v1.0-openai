
def sub_DIObject(text):   
    import spacy
    nlp = spacy.load('en_core_web_sm')
    parsed_text = nlp(text)
    subject = ""
    direct_object = ""
    indirect_object = ""
#get token dependencies
    for text in parsed_text:
    #print(text)
    #subject would be
        if text.dep_ == "nsubj":
            subject = text.orth_
    #iobj for indirect object
        if text.dep_ == "iobj":
            indirect_object = text.orth_
    #dobj for direct object
        if text.dep_ == "dobj":
            direct_object = text.orth_

    return (subject, direct_object, indirect_object)
###
###
###
###delete this funtion
