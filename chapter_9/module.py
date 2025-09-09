"""Use Python to scan directories and move files into folders based on type (e.g., PDFs, images) or date.
 This helps keep downloads or shared folders clean.

"""
import os
import shutil

source = r"C:\Users\Aamir\Downloads"
destination = os.path.join(source, "Organized")  
for filename in os.listdir(source):
    #  print(filename)
    #  print(type(filename))
     filepath = os.path.join(source, filename)
    #  print(filepath)
    #  print(type(filepath))

     if os.path.isfile(filepath):
        print("yes")
     
        
        
        ext = os.path.splitext(filename)[1].lower()
        print(ext)
        

        if ext == "":
            folder_name = "Others"
        else:
            folder_name = ext.replace(".", "").upper()  

       
        folder = os.path.join(destination, folder_name)
        os.makedirs(folder, exist_ok=True)
        print("making directory")
        os.makedirs

    
        shutil.move(filepath, os.path.join(folder, filename))

        print(f"Moved {filename} → {folder}")
