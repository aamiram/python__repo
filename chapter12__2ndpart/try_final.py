def main():
 
 try:
   a =  int(input(" hay enter the num : "))
   print(a)
   return #It immediately stops the function’s execution and exits it.
 
 except Exception as e: 
   print(e)
   return

 finally:  # so if we dont write the finally then the print statement will not work 
    
    print("i am inside finally ")


main()