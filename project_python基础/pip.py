import os
libs={"numpy","matplotlib"}
os.system("D:")
os.system("cd D:\\programfiles\\Python\\3.0\\Scripts")
try:
    for lib in libs:
        os.system("pip install"+ lib)
    print("Successful")
except:
    print("Failed")
