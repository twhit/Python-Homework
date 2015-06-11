from datetime import datetime
import shelve

d = {"a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7}

s = shelve.open("sfile")
s["a"] = 1
s["b"] = 2
s["c"] = 3
s["d"] = 4
s["e"] = 5
s["f"] = 6
s["g"] = 7

dt1 = datetime.now()
print(d["a"])
print(d["b"])
d["b"] = d["b"] + 10
print(d["b"])
print(d["c"])
print(d["d"])
print(d["e"])
d["e"] = d["e"] * 10
print(d["e"])
dt2 = datetime.now()
dict_time = dt2-dt1
print("Dictionary time: " + str(dict_time))

dt3 = datetime.now()
print(s["a"])
print(s["b"])
s["b"] = s["b"] + 10
print(s["b"])
print(s["c"])
print(s["d"])
print(s["e"])
s["e"] = s["e"] * 10
print(s["e"])
dt4 = datetime.now()
shelve_time = dt4-dt3
print("Shelve time: " + str(shelve_time))
s.close()

if(dict_time < shelve_time):
    print("Dictionary is faster.")
elif(dict_time > shelve_time):
    print("Shelve is faster.")
else:
    print("Both times were equal.")
    
    
