import requests # use to download the website
import hashlib # use to check if the cintent is changed
import time # date and time 



url = "https://httpbin.org/html" # sample url form chat gpt
save_file = "last_hash.txt"


while True:
    page = requests.get(url).text# requests.get(url) this is use to download the url and .text is use to conver it in to a string in python


    new_hash =  hashlib.sha256(page.encode()).hexdigest()
    #hashlib.sha256 is a hash object it {if ant leter changes then the hash file get change completely }
    #page.encoded() convert the hash in to byte code 
    #Converts the hash into a readable hex string.

    try:
        with open(save_file ,"r") as f :
            old_hash =  f.read().strip()

    except FileNotFoundError:
        old_hash = ""    


    if new_hash != old_hash:
        print("the webpage is changed ") 
        with open(save_file ,"w")  as f :
            f.write(new_hash)
    else :
        print("no change ")

    time.sleep(50)        
    
       





