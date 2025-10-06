from typing import List, Union,Tuple,Dict

# lsit of intiger 
number : List[int]   =  [1,2,3,4,5]


# tuple of a string and an integer 
person : Tuple[str,int] =  ("Alice",30)


#dictionary with srting key and intiger values 
scores : Dict[str ,int] = {"alice " : 90 , "bob" : 85}


#union type for variable that can hold multiple types 
identifire :Union[int ,str]  = "ID 1223"
identifire  =  12345 # also valid 