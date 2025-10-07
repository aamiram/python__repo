try:#same as if else if try bolck is valid then the code will skip the except bolck
 
 a =  int(input(" hay enter the num : "))
 print(a)
 # what if we do not  uses the exception the will will bbecrashgeed and "thanku " will not be printed  

except Exception as e: #except Exception as variable: is use to print the error or give the error without crashing the code
   print(e)

else:
  # the else bolck will be only run when the try block is true ans be exicuted 
  print("i am inside else ")