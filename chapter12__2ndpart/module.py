#IF __NAME__==__MAIN__IN PYTHON
def myfunc():
    print("hellow world ")

myfunc()    

# myfunc()
# print(__name__)
   
# it will print __main__ if the code is run from module file 
# and if the code is run form main.py the the code __module__ will be printed

if __name__ == "__main__":
    #if this code is exicuted by running the file its present in
    print("we are directly rynning this code ")
    myfunc()
    print(__name__)
