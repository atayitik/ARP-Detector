import subprocess
import time


while True:

    choice = input("ARP Dedektörünü Test Etmek için (T/t) veya Başlatmak için (B/b) 'ye basın ")

    if choice == "T" or choice == "t":
        print("ARP SALDIRISI BELİRLENDİ!")
        

    elif choice == "B" or choice == "b":

        while True:
            subprocess.call("arp -a 0.0.0.0")#Kullanıcı IP adresi yazılır#
            get_output = subprocess.getoutput("arp -a 0.0.0.0")#Kullanıcı IP adresi yazılır#
            output_log = open("Logs.txt", "w")
            output_log.write(get_output)
            output_log.close()
            log = open("Logs.txt", "r")
            if log.mode == "r":
                contents = log.read()
                if " 38-22-d6-e7-ed-00" in contents: #Kullanıcı internet MAC adresi yazılır#
                    print("ARP SALDIRISI BELİRLENMEDİ")
                elif "ff-ff-ff-ff-ff-ff" != contents:
                    print("ARP SALDIRISI BELİRLENDİ!")
                   
                    break
            time.sleep(10)
