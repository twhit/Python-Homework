import pickle
import shelve

def readfile(op):
    if (op == "pickle"):
        f = open("pickle.txt", "br")
        pic = pickle.load(f)
        print("Name: " + pic["name"])
        print("Age: " + pic["age"])
        print("Country: " + pic["country"])
        f.close()
    if (op == "shelve"):
        s = shelve.open("shelve")
        print("Name: " + s["name"])
        print("Age: " + s["age"])
        print("Country: " + s["country"])
        s.close()
        
dict = {}

op = ""
while (op != "pickle") and (op != "shelve"):
    op = input("Enter pickle or shelve: ")
    
dict["name"] = input("Enter your name: ")
dict["age"] = input("Enter your age: ")
dict["country"] = input("Enter your country of origin: ")

if (op == "pickle"):
    f = open("pickle.txt", "bw")
    pickle.dump(dict, f)
    f.close()

if (op == "shelve"):
    s = shelve.open("shelve")
    s["name"] = dict["name"]
    s["age"] = dict["age"]
    s["country"] = dict["country"]
    s.close()
    
readfile(op)
    




