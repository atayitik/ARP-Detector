import subprocess
import time

while True:

    choice = input("ARP Dedektörünü Test Etmek için (T/t) veya Başlatmak için (B/b) 'ye basın ")

    if choice == "T" or choice == "t":
        print("ARP SALDIRISI BELİRLENDİ!")


    elif choice == "B" or choice == "b":

        while True:
            subprocess.call("arp -a 192.168.0.1")  # Kullanıcı IP adresi yazılır#
            get_output = subprocess.getoutput("arp -a 192.168.0.1")  # Kullanıcı IP adresi yazılır#
            output_log = open("Logs.txt", "w")
            output_log.write(get_output)
            output_log.close()
            log = open("Logs.txt", "r")
            if log.mode == "r":
                contents = log.read()
                if " 98:f2:17:4:e0:dd" in contents:  # Kullanıcı internet MAC adresi yazılır#
                    print("ARP SALDIRISI BELİRLENMEDİ")
                elif "ff-ff-ff-ff-ff-ff" != contents:
                    print("ARP SALDIRISI BELİRLENDİ!")

                    break
            time.sleep(10)
