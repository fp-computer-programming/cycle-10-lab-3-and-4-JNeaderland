#Author: Jacob Neaderland
list = [] #Makes a blank list
listd = [] #Makes another blank list
ph = int(0) #Sets the placeholder to 0
def double_stuff(list):
    ph = 0
    while len(listd) != len(list): #When it hasnt done every value
        doubv = list[ph] #Sets what value to double
        listd.append(2*doubv) #Adds the doubled value to a new list
        ph = ph + 1 #Moves over one space
    print (listd)
double_stuff([1, 2, 3, 4, 5, 6, "s"])


list = [] #Makes a blank list
indname = [] #Makes a blank list
def indexed_names(list):
    ph = 0 #Sets the placeholder to 0
    while len(indname) != len(list): #Makes sure they are the same length
        name = list[ph] #Which word
        rep = [ph, ": ", name] #What to add
        indname.append(rep) #Adds it
        ph = ph + 1 #Moves over one space
    print(indname)
names = ["john", "todd", "tim"]
indexed_names(names)