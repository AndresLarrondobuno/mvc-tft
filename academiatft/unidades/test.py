from ast import literal_eval

string = "{'pablo':10, 'juan':20.934754888888884}"
dict = literal_eval(string)
print(dict)