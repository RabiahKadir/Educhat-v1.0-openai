from generateTriple import getPhrase


def TextClass(filename):
    file = open(filename, 'r')
    Lines = file.readlines()
    file.close()
    return Lines


def GenericCatCheck(phrase, ClassL):
    count = 0
    for line in ClassL:
        count += 1
        words = line.split(",")
        if (phrase.lower().find(words[0].lower().strip()) != -1):
            return words[1].strip()
    return "u"


def getCat(key):
    # edit path for resoruce
    # C:\Users\Aimi\Desktop\Python engine Educhat\resources-20221107T145819Z-001\resources
    Lines = TextClass(
        'resources/category.csv')
    count = 0
    for line in Lines:
        count += 1
        words = line.split(",")
#        print("word: {} -> cat:{}".format(words[0].strip(), words[1].strip()))
        if (key.find(words[0].strip()) != -1):
            return words[1].strip()
    return "u"


def getSynonym(word):
    from nltk.corpus import wordnet
    synonyms = []
    for syn in wordnet.synsets(word):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return synonyms


def analysePhrase(phrase):
    from nltk.tokenize import word_tokenize
    tokens = word_tokenize(phrase)
    for token in tokens:
        synons = set(getSynonym(token))
        for syn in synons:
            finalCat = getCat(syn)
            if (finalCat != "u"):
                return finalCat
    return "u"


def findSentenceType(input):
    results = []
    phrases = getPhrase(input)
   # print("phrases:",phrases)
   # edit path for resoruce
   # C:\Users\Aimi\Desktop\Python engine Educhat\resources-20221107T145819Z-001\resources
    classData = TextClass(
        'resources/phaseClass.csv')
    for phrase in phrases:
        results.append(GenericCatCheck(phrase, classData))
#    print("Length", len(results), ":",results)
    count = 0
    for res in results:
        if (res == "u"):
            # print("checking:", phrases[count])
            results[count] = getCat(phrases[count])
        # print("proposed=>",results)
            if (results[count] == "u"):
                results[count] = analysePhrase(phrases[count])
        count += 1
    return (phrases, results)
