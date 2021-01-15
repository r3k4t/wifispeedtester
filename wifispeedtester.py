
import os
import sys
import speedtest   
import pyfiglet

os.system("clear")

banner = pyfiglet.figlet_format("WifiSpeedTester", font="slant" )

print (banner)

print ("                      Author : Rahat Khan Tusar(rkt)")
print ("                     Github  : https://github.com/r3k4t")
  
st = speedtest.Speedtest() 
  
option = int(input('''What speed do you want to test:   
  
1) Download Speed   
  
2) Upload Speed   
  
3) Ping  
  
Your Choice: ''')) 
  
  
if option == 1:   
  
    print(st.download())   
  
elif option == 2:  
  
    print(st.upload())   
  
elif option == 3: 
  
    st.download()

    st.upload()

    servername = []   
  
    st.get_servers(servername)   
  
    print(st.results.ping)   
  
else: 
  
    print("Please enter the correct choice !")  
