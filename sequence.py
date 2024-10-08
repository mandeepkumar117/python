# sequence->to maintain order of sequence data type we use indexing.
# type->
# list->in python wen we want to store multiple element with the help single reference(variable) .then we have two option first list & tupple
#       list is a conatainer in which  we contain hytroginious data as well as homogenious to
# note-> array is not built in support in python


name="mandeep"
age=26
address="bihar"
st_details=[name, age, address]
print(type(name))
print(type(age))
print(type(address))
print(type(st_details))
print(st_details[2],st_details[-3])

# list manipulation->list is a mutable data type

st_details=[name, age, address]
st_details2=["ajay", 23, "ujjain"]
print(st_details2)
st_details2[2]="indore"
print(st_details2)
st_details2[1]=26
print(st_details2)