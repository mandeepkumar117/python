# method of dictionary

d={1:"mon",2:"tues",3:"wed"}
# 1)keys()
keys=d.keys()
print(type(keys),keys)

# 2)value()
vaule=d.values()
print(type(vaule),vaule)

# 3)items()
item=d.items()
print(type(item),item)

keys=sorted(d.keys())
print(keys)
vaule=sorted(d.values())
print(d)
item=sorted(d.items())
print(d)