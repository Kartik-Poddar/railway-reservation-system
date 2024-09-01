import requests
from colorama import init , Fore , Style

URL_CHECKING = r"https://www.google.com"

TIMEOUT_TIME = 5

while True :

    FLAG = 0
    
    while True :
        
        try :
            
            REQUESTS = requests.get( URL_CHECKING , timeout = TIMEOUT_TIME )        
            
            FLAG = 1
            break
            
        except :
            
            print()
            print( Fore.RED + " CAN'T CONNECT TO THE INTERNET !!! " )
            print( Fore.RED + " PLEASE CHECK YOUR INTERNET CONNECTION AND TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            print()
            
            FLAG = -1
            break
        
    if ( FLAG == -1 ) :

        INTERNET_CHOICE = input( " DO YOU WANT TO RETRY ESTABLISHING INTERNET CONNECTION AGAIN ? (y/n);(Y/N) : ")

        if INTERNET_CHOICE in [ "Y" , "y" ] :
            continue

        else :
            break

    else :

        print()
        print( Fore.GREEN + " SUCCESSFULLY CONNECTED TO THE INTERNET !!! " )
        print( Style.RESET_ALL )
        print()
        
        break
        
