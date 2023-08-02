import rdflib

#attribute 1/2/3 (s,p,o)
def getValue(graph,_query,attribute):
    results = graph.query(_query)
    print(len(results))
    _list=set()
    for row in results:
        if(attribute==1):
            _list.add(row.subject)
        elif (attribute == 2):
            _list.add(row.predicate)
        else:
            _list.add(row.object)
    return _list
                
# Query4 = "select * where { ?subject ?predicate ?object .}"
# listall = getValue(graph,Query4,3)
# print(listall)
# for result in listall:
#     print("result:",str(result)) 

def findObject(graph, keyword):      
    _possibleSubjs = []
    _possiblePreds = []
    _possibleObjs = []
    sparql_query = " SELECT * WHERE { ?s ?p ?o.} "
    results = graph.query(sparql_query)
    for result in results:
        if (str(result.s).lower().find(keyword.lower()) !=-1 or 
            str(result.p).lower().find(keyword.lower()) !=-1 or
            str(result.o).lower().find(keyword.lower()) !=-1):
            #    print("record",str(result)) 
                # print("subject:", str(result.s))
                # print("Predicate:", str(result.p))
                # print("Object:", str(result.o))
                if(str(result.s) != ""):
                    _possibleSubjs.append(str(result.s))
                if(str(result.p) != ""):
                    _possiblePreds.append(str(result.p))
                if(str(result.o) != ""):
                    _possibleObjs.append(str(result.o))
    return (_possibleSubjs,_possiblePreds,_possibleObjs)

def getSubjects(graph):
    _query = """ SELECT DISTINCT ?s WHERE { ?s ?p ?o .} """
    _distinctList = graph.query(_query)
    print("Total Subject: ",len(_distinctList))
    for result in _distinctList:
        print("subject:",str(result)) 
    return _distinctList

def getPredicates(graph):
    _query = """ SELECT DISTINCT ?p WHERE { ?s ?p ?o .} """
    _distinctList = graph.query(_query)
    print("Total Predicates: ",len(_distinctList))
    for result in _distinctList:
        print("Predicate:",str(result)) 
    return _distinctList

def getObjects(graph):
    _query = """ SELECT DISTINCT ?o WHERE { ?s ?p ?o .} """
    _distinctList = graph.query(_query)
    print("Total Objects: ",len(_distinctList))
    for result in _distinctList:
        print("object:",str(result)) 
    return _distinctList

def testQuery():
    graph = rdflib.Graph()
    #graph.parse("./testing/animals.rdf")
    graph.parse("resources//educhatModel.rdf")
    print(len(graph))
    (s,p,o) = findObject(graph,"subject")
    # print("subject:",s)
    # print("Predicate:", p)
    # print("Objects:", o)
    print(s)
    print(p)
    print(o)
    
    
        