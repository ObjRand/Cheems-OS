import pwinput, os

password = pwinput.pwinput(prompt='Password: ', mask='*')
os.chdir("acc")

os.remove('password.txt')

file = open("password.txt", "w") 
file.write(password) 
file.close() 