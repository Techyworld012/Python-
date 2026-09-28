# this is the type conversion , where to edit the tuple , first we cinver the tuple into the type list and then edit that list and again covert it to tuple again , as shown below 


a=("Piyush", " Riddhi","KIrti")
print("Before conversion: ",type(a))

a = list(a)              # converted to list ; 
print("After conversion : ",type(a))   

a.append("vanshika")
print(a)              # printed in list form 

a=tuple(a)
print(type(a))
print(a)             # printed in tuple form ;

