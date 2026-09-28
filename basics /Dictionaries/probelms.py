#- Convert the following dictionary into JSON format.
# Student_data = {"name": "David", "age":13, "marks":87}


import json
Student_data = {"name": "David", "age":13, "marks":87}
print(type(Student_data))

data = json.dumps(Student_data)   # to convert dictionary to json string 
print(data)
print(type(data))



# - Access the value of age from the given data.
Student_dat = '{"name": "David","age":13, "marks":87}'   # strign format called as json
para = json.loads(Student_dat)    # json string to dictionary or object,sothat we can access
print(para["age"])      


# - Pretty Print following JSON data.
Student_details = {"name": "David", "age":13, "marks":87}

details = json.dumps(Student_details,indent=4,separators=(",","=")) # converted to string format  + giving indent and separators 
print(type(details))        # string format 
print(details)


#-  Sort the following JSON keys and write them into a file.
# Student_data = {"name": "David", "age":13, "marks":8)



