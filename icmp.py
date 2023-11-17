import subprocess
from colorama import Fore, Back, Style





def ic(n, typ):
    toprint = ""

    if typ == 1:
        print("\n\n SCANNING... Please Wait \n\n")
        address = n
        res = subprocess.call(['ping', '-c', '3', address])

        if res == 0:
            toprint += ( " " + address)
            toprint += (Fore.GREEN + " is LIVE\n")
            toprint += (Style.RESET_ALL)


    if typ == 2:
        le = len(n)
        i = le - 1
        s = ""
    

        while n[i] != '.':
            i-= 1
        z = i + 1
        add = ""
        e = 0
        while e <= i:
            add += n[e]
            e += 1
    

        deb = ""
        while n[z] != '/':
            deb += n[z]
            z += 1
    

        z += 1
        fin = ""
        while z != le:
            fin += n[z]
            z += 1
    



    
        for q in range(int(deb),int(fin)):
            print("\n\n SCANNING... Please Wait \n\n")
            address = add + str(q)
            res = subprocess.call(['ping', '-c', '3', address])
            if res == 0:
                toprint += ( " " + address)
                toprint += (Fore.GREEN + " LIVE\n")
                toprint += (Style.RESET_ALL)




    print("\n\n\n")
    print("----------Scan List of live IP Adresses----------\n\n")
    print(toprint)
