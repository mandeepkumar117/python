import json
py_data={'name':"mandeep",'age':None,'active':True}
js_data=json.dumps(py_data)
print(js_data)
print(type(js_data))
new_py_data=json.loads(js_data)
print(new_py_data)
print(type(new_py_data))
x='{"name": "mandeep", "age": null, "active": true}'
my_new_data=json.loads(x)
print(x)
print(type(x))