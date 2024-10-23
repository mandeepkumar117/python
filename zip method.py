#method of dict
#zip method->we have to pass keys and value .zip(key,value)

# key=["ajay", "mandeep", "jay", "vikas", "sonam", "naman"]
# value=[23, 34, 45, 26]
# result=dict(zip(key,value))
# print(result)
# result=tuple(zip(key,value))
# print(result)


# data={"ajay":23, "vikash":45, "sonam":34}
# a=data["vikash"]
# print(a)
# a=data["tarun"]
# print(a)
# a=data.get('ashish')
# print(a)



# setdefault()
# 1)key available-->return existing value
# 2)key not available-->key value pair add,return added value

# data={"ajay":23, "vikash":45, "sonam":34}
# value=data.setdefault("vikash",343)
# print(data,value)

#pop(), popitem()-->these are return value
#  clear()

data={"ajay":23, "vikash":45, "sonam":34, "sonali":67, "rahul":40, "mandeep":{'11':"rahul", '23':"suresh", '12':"kavya"}}
# value=data.pop("sonam")
# print(data)
# print(value)

# value=data["mandeep"].popitem()
value=data["mandeep"]
print(data)
# print(value)
# value=data.popitem()
# print(data)
# print(value)



