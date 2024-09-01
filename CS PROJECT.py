import random
import datetime
import prettytable
import os
import openpyxl
import pickle
from colorama import init , Fore , Style , ansi
import smtplib
import requests
init()


def CREATE_DATABASE_RAILWAY_RESERVATION_SYSTEM() :
    
    import mysql.connector as MS
    MYCONNECTION = MS.connect ( host = "localhost" , user = "root" , passwd = "12345" )    
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True

    try :
    
        NEW_DATABASE = " create database RAILWAY_RESERVATION_SYSTEM ; "
        
        CURSOR.execute ( NEW_DATABASE )

    except :
        pass


def USE_DATABASE_RAILWAY_RESERVATION_SYSTEM() :

    import mysql.connector as MS
    MYCONNECTION = MS.connect ( host = "localhost" , user = "root" , passwd = "12345" )    
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True

    SQL_QUERY = " use RAILWAY_RESERVATION_SYSTEM ; "
    CURSOR.execute( SQL_QUERY )



def CONNECTION() :
    
    import mysql.connector as MS
    MYCONNECTION = MS.connect ( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    
    if MYCONNECTION.is_connected() :
        print( " !!! SUCCESFULLY CONNECTED TO THE DATABASE !!! " )

    else :
        pass


         
def TABLE_CREATION():

    import mysql.connector as MS
    MYCONNECTION = MS.connect ( host = "localhost" , user = "root" , passwd = "12345" ,database = "RAILWAY_RESERVATION_SYSTEM" )    
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True

    try :
        TABLE_CREATION_RAILWAY_TICKET()
        TABLE_CREATION_USER_ACCOUNTS()
        TABLE_CREATION_ADMIN_ACCOUNTS()
        TABLE_CREATION_FRAUD_REPORTS_TICKETS()
        TABLE_CREATION_FRAUD_REPORTS_ACCOUNTS()
                
    except :
        pass



def TABLE_CREATION_RAILWAY_TICKET() :
    
    import mysql.connector as MS
    MYCONNECTION = MS.connect ( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True

    CREATE1 = " create table RAILWAY_TICKET ( PNR_NUMBER bigint, PASSENGER_NAME varchar( 30 ) , ID_TYPE varchar( 20 ) , ID_NUMBER varchar( 20 ) , SEAT_BOOKED int( 3 ) , DATE_GOING date ) "
    CURSOR.execute( CREATE1 )
    
    CREATE2 = " alter table RAILWAY_TICKET add column STARTING_POINT varchar( 20 ) , add column ENDING_POINT varchar( 20 ) , add column DATE_RETURN date , add column PASSENGER_CONTACT bigint "
    CURSOR.execute( CREATE2 )
    
    CREATE3 = " alter table RAILWAY_TICKET add column PASSENGER_AGE int( 4 ) , add column PASSENGER_GENDER varchar( 40 ) , add column QUOTA varchar( 30 ) , add column CLASS varchar( 20 ) "
    CURSOR.execute( CREATE3 )
    
    CREATE4 = " alter table RAILWAY_TICKET add column PREFERRED_BERTH varchar( 20 ) , add column MEAL varchar( 15 ) , add column PASSENGER_TYPE varchar(10) , add column USER_CONTACT bigint "
    CURSOR.execute( CREATE4 )


   
def TABLE_CREATION_USER_ACCOUNTS() :
    
    import mysql.connector as MS
    MYCONNECTION = MS.connect ( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True

    CREATE = " create table USER_ACCOUNTS ( USER_NAME varchar( 50 ) primary key , PASSWORD varchar( 50 ) binary , NAME varchar( 30 ) , USER_CONTACT bigint unique key , GENDER varchar( 40 ) , DATE_OF_BIRTH date , EMAIL_ACCOUNT varchar( 100 ) unique key ) "
    CURSOR.execute( CREATE )



def TABLE_CREATION_ADMIN_ACCOUNTS() :

    import mysql.connector as MS
    MYCONNECTION = MS.connect ( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True

    CREATE = " create table ADMIN_ACCOUNTS ( USER_NAME varchar( 50 ) primary key , PASSWORD varchar( 50 ) binary , NAME varchar( 30 ) , ADMIN_CONTACT bigint unique key , GENDER varchar( 40 ) , DATE_OF_BIRTH date ) "
    CURSOR.execute( CREATE )



def TABLE_CREATION_FRAUD_REPORTS_TICKETS():

    import mysql.connector as MS
    MYCONNECTION = MS.connect ( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True

    CREATE1 = " create table FRAUD_REPORTS_TICKETS ( PNR_NUMBER bigint , PASSENGER_NAME varchar( 30 ) , ID_TYPE varchar( 20 ) , ID_NUMBER varchar( 20 ) , SEAT_BOOKED int( 3 ) , DATE_GOING date  ) "
    CURSOR.execute( CREATE1 )
    
    CREATE2 = " alter table FRAUD_REPORTS_TICKETS add column STARTING_POINT varchar( 20 ) , add column ENDING_POINT varchar( 20 ) , add column DATE_RETURN date , add column PASSENGER_CONTACT bigint "
    CURSOR.execute( CREATE2 )
    
    CREATE3 = " alter table FRAUD_REPORTS_TICKETS  add column PASSENGER_AGE int( 4 ) , add column PASSENGER_GENDER varchar( 40 ) , add column PASSENGER_TYPE varchar(10) , add column USER_CONTACT bigint "
    CURSOR.execute( CREATE3 )



def TABLE_CREATION_FRAUD_REPORTS_ACCOUNTS():

    import mysql.connector as MS
    MYCONNECTION = MS.connect ( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True

    CREATE1 = " create table FRAUD_REPORTS_ACCOUNTS ( USER_NAME varchar( 50 ) , PASSWORD varchar( 50 ) binary , NAME varchar( 30 ) , USER_CONTACT bigint unique key , GENDER varchar( 40 ) , DATE_OF_BIRTH date , EMAIL_ACCOUNT varchar( 100 ) ) "                         
       
    CURSOR.execute( CREATE1 )


    
def MENU() :
    
    import mysql.connector as MS
    MYCONNECTION = MS.connect ( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    print()

    print( Fore.MAGENTA )
    print( Style.BRIGHT )
    print( " WELCOME TO ONLINE RAILWAY RESERVATION SYSTEM !!! " )
    print( Style.RESET_ALL )

        
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
            


    SQL_QUERY_1 = " delete from USER_ACCOUNTS where USER_NAME is null or PASSWORD is null or NAME is null or USER_CONTACT is null or GENDER is null or DATE_OF_BIRTH is null or EMAIL_ACCOUNT is null "
    CURSOR.execute( SQL_QUERY_1 )

    SQL_QUERY_2 = " delete from ADMIN_ACCOUNTS where USER_NAME is null or PASSWORD is null or NAME is null or ADMIN_CONTACT is null or GENDER is null or DATE_OF_BIRTH is null "
    CURSOR.execute( SQL_QUERY_2 )

    SQL_QUERY_3 = " delete from RAILWAY_TICKET where PASSENGER_NAME is null or ID_TYPE is null or ID_NUMBER is null or SEAT_BOOKED is null or DATE_GOING is null or STARTING_POINT is null "
    CURSOR.execute( SQL_QUERY_3 )
    
    SQL_QUERY_4 = " delete from RAILWAY_TICKET where ENDING_POINT is null or PASSENGER_CONTACT is null or PASSENGER_AGE is null or PASSENGER_GENDER is null or QUOTA is null or CLASS is null "
    CURSOR.execute( SQL_QUERY_4 )

    SQL_QUERY_5 = " delete from FRAUD_REPORTS_ACCOUNTS where USER_NAME is null or PASSWORD is null or NAME is null or USER_CONTACT is null or GENDER is null or DATE_OF_BIRTH is null or EMAIL_ACCOUNT is null "
    CURSOR.execute( SQL_QUERY_5 )

    SQL_QUERY_6 = " delete from FRAUD_REPORTS_TICKETS where PASSENGER_NAME is null or ID_TYPE is null or ID_NUMBER is null or SEAT_BOOKED is null or DATE_GOING is null "
    CURSOR.execute( SQL_QUERY_6 )
    
    SQL_QUERY_7 = " delete from FRAUD_REPORTS_TICKETS where STARTING_POINT is null or ENDING_POINT is null or PASSENGER_CONTACT is null or PASSENGER_AGE is null or PASSENGER_GENDER is null "
    CURSOR.execute( SQL_QUERY_7 )
    
    
    CURRENT_DATE = str( datetime.date.today() )

    CURRENT_DATE_TIME_NOW = str( datetime.datetime.now() )

    CURRENT_DATE_TIME_STORE = ""

    for DATE_AND_TIME in CURRENT_DATE_TIME_NOW.split() :
        CURRENT_DATE_TIME_STORE += DATE_AND_TIME + "    "
        

    SQL_QUERY_8 = " select count(*) from RAILWAY_TICKET where DATE_GOING = '{}' or DATE_RETURN = '{}' ; ".format( CURRENT_DATE , CURRENT_DATE )
    
    CURSOR.execute( SQL_QUERY_8 )
    FOOTFALL_DATA = CURSOR.fetchall()[0][0]
    
    print( "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t TODAY'S FOOTFALL : " , FOOTFALL_DATA )
    
    print( "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t CURRENT DATE AND TIME : " , CURRENT_DATE_TIME_STORE )


    
    while True :
        try :
            print( Fore.YELLOW )
            
            print( " 1. USER SIGN IN \n" )

            print( " 2. USER SIGN UP \n" )
            
            print( " 3. ADMIN LOGIN \n" )
            
            print( " 4. ADMIN SIGNUP \n" )

            print( " 5. HEAD ADMIN \n" )

            print( " 6. EXIT \n" )

            print( Style.RESET_ALL )

            print()
            
            CHOICE = int ( eval ( input ( " PLEASE ENTER YOUR CHOICE - " ) ) )
            print( ansi.clear_screen() )
            print()
            print()
            
            if ( CHOICE == 1 ) :
                while True :
                    USER_TIME1 = datetime.datetime.now() 
                    CHECK = USER_SIGN_IN( USER_TIME1 )
                
                    if ( CHECK == True ) :
                        print( " WELCOME !!! " )
                        MAIN_PROGRAM_USER()
                        break
                    
                    else:
                        break
                    
                continue

                
            elif ( CHOICE == 2 ) :
                while True :
                    CHECK = USER_SIGN_UP()
                
                    if ( CHECK == True ) :
                        print( " TO CONTINUE PLEASE SIGN IN !!! " )
                        print()
                        break
                    
                    else :
                        break
                continue

            
            elif ( CHOICE == 3 ) : 
                while True :
                    ADMIN_TIME1 = datetime.datetime.now()
                    CHECK = ADMIN_LOGIN( ADMIN_TIME1 )

                    if ( CHECK == True ) :
                        MAIN_PROGRAM_ADMIN()
                        break
                    
                    else :
                        break
                    
                continue

            
            elif ( CHOICE == 4 ) :
                 while True :
                    CHECK = ADMIN_SIGN_UP()

                    if ( CHECK == True ) :
                        print( " TO CONTINUE PLEASE SIGN IN !!! " )
                        print()
                        break
                    
                    else :
                        break
                    
                    continue
                    
            
            elif ( CHOICE == 5 ) :
                UNIQUE_CODE = "JaiHind@1947"
                
                CODE = input( " PLEASE ENTER THE UNIQUE CODE : " )
                print()
                print()
                
                for ATTEMPTS in range( 0 , 4 , 1 ) :
                    if ( CODE == UNIQUE_CODE ) :
                        MAIN_PROGRAM_HEAD_ADMIN()
                        break
                    
                    else :
                        break

                     
            elif ( CHOICE == 6 ) :
                print( " THANK YOU !!! " )
                break
            
            else:
                print( Fore.RED + " INVALID INPUT !!! " )
                print( Fore.RED + " PLEASE ENTER A VALID CHOICE !!! " )
                print( Style.RESET_ALL )
                continue

        
        except :
            print()
            print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            continue



def USER_SIGN_IN( TIME1 ) :
    
    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    while True :
        for ATTEMPTS in range(0,4,1) :
            print()
            FLAG1 = 0
            FLAG2 = 0
            FLAG3 = 0
            DATA = []
            USERNAME = input( " PLEASE ENTER YOUR USERNAME : " ).strip()
            print()

            SQL_QUERY_1 = " select * from USER_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
            CURSOR.execute( SQL_QUERY_1 )
            DATA = CURSOR.fetchall()
            
            if ( DATA == [] ) :
                print( Fore.RED + " ACCOUNT DOES NOT EXISTS !!! " )
                print( Style.RESET_ALL )
                print()
                FLAG1 = -1
                
            else :
                PASSWORD = input( " PLEASE ENTER YOUR PASSWORD : " )
                print()
                
                
                SQL_QUERY_2 = "select PASSWORD , NAME , USER_CONTACT  from USER_ACCOUNTS where USER_NAME = '{}' ".format( USERNAME )
                CURSOR.execute( SQL_QUERY_2 )
                DATA1 = CURSOR.fetchall()
                NAME = DATA1[0][1]
                
                if ( PASSWORD == DATA1[ 0 ][ 0 ] ) :
                    
                    SQL_QUERY_3 = "select EMAIL_ACCOUNT from USER_ACCOUNTS where USER_NAME = '{}' ".format( USERNAME )
                    CURSOR.execute( SQL_QUERY_3 )
                    DATA2 = CURSOR.fetchall()
                    EMAIL = DATA2[ 0 ][ 0 ]
                    
                    OTP = random.randrange( 99999 , 999999 )
                    
                    SERVER = smtplib.SMTP_SSL( "smtp.gmail.com" , 465 )
                    SERVER.login( "railwaysofindia.1853@gmail.com" , "JaiHind@Indian" )
                    SERVER.sendmail( "railwaysofindia.1853@gmail.com" , EMAIL , " YOUR VERIFICATION OTP IS " + str( OTP ) + "\n FOR SIGNING IN INDIAN RAILWAYS WITH USERNAME " + USERNAME )
                    SERVER.quit()

                    for ATTEMPTS in range( 0 , 4 , 1 ) :
                        try :
                            print()
                            OTP_INPUT = int ( eval ( input ( " PLEASE ENTER OTP SEND AT YOUR REGISTERED EMAIL ADDRESS : " ) ) )
                            print()
                            
                            if ( OTP == OTP_INPUT ) :
                                TIME2 = datetime.datetime.now()
                                DIFFERENCE_TIME = TIME2 - TIME1
                                STRING_DIFFERENCE = str( DIFFERENCE_TIME )
                                SPLITTING_STRING = STRING_DIFFERENCE.split(":")
                                DIFFERENCE_HOUR = int( SPLITTING_STRING[0] )
                                DIFFERENCE_MINUTE = int( SPLITTING_STRING[1] )
                                FLAG3 = 1
                                break

                            else :
                                FLAG3 = -1
                                print( Fore.RED + " ENTERED OTP IS INCORRECT !!! " )
                                print( Fore.RED + " HENCE, PLEASE TRY AGAIN !!! " )
                                print( Style.RESET_ALL )
                                print()
                                continue
                        except :
                            FLAG3 = -1
                            print( Fore.RED + " INVALID INPUT !!! " )
                            print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
                            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                            print( Style.RESET_ALL )
                            print()
                            continue
                            
                                    
                
                    if (( DIFFERENCE_HOUR >= 0 ) and (DIFFERENCE_MINUTE > 10 )) :
                        FLAG2 = -1
                        break
    
                    else :
                        print( GREETINGS() , NAME )
                        print()
                        print()
                        global USER_CONTACT
                        USER_CONTACT = DATA1[0][2]
                        FLAG1 = 1
                        break
                
                else :
                    print( Fore.RED + " WRONG PASSWORD !!! " )
                    print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                    print( Style.RESET_ALL )
                    print()
                    print()
                    FLAG1 = -1
                    continue
                
                
        if ( FLAG1 == -1 ) :
            print( Fore.RED + " YOU HAVE EXCEDEED THE MAXIMUM NUMBER OF YOUR TRIALS FOR PASSWORD !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN AFTER 1 HOUR !!! " )
            print( Style.RESET_ALL )
            return False

        
        elif ( FLAG2 == -1 ) :
            print( Fore.RED + " SESSION TIMED OUT !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            return False
        
        elif ( FLAG3 == -1 ) :
            print( Fore.RED + " YOU HAVE EXCEDEED THE MAXIMUM NUMBER OF YOUR TRIALS FOR OTP !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN AFTER 1 HOUR !!! " )
            print( Style.RESET_ALL )
            return False
        
        else :
            FILE_HANDLE = open( r"C:\Users\dell\Desktop\TIMELINES\USER_ACCOUNT_TIMELINE.dat" , "ab" )
            
            TIME_USER_ACCOUNT = datetime.datetime.today()
            USER_TIMELINE_LIST = [ USERNAME , str( USER_CONTACT ) , "ACCOUNT_SIGN_IN" , str( TIME_USER_ACCOUNT ) ]

            pickle.dump( USER_TIMELINE_LIST , FILE_HANDLE )

            FILE_HANDLE.close()

            return True



def USER_SIGN_UP() :

    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True

    while True :
        
        print()
        
        FIRST_NAME = input( " PLEASE ENTER YOUR FIRST NAME : " ).upper().strip()

        print()
    
        MIDDLE_NAME = input( " PLEASE ENTER YOUR MIDDLE NAME ( PRESS ENTER IF NOT ): " ).upper().strip()
        
        print()

        LAST_NAME = input( " PLEASE ENTER YOUR LAST NAME : " ).upper().strip()

        print()
        
        if FIRST_NAME == "" :
            print( Fore.RED + " SORRY FIRST NAME CAN'T BE NULL !!! " )
            print( Fore.RED + " HENCE, PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            continue
        
        else :
            if ( MIDDLE_NAME == "" ) :
                NAME = FIRST_NAME + " " + LAST_NAME

            else :
                NAME = FIRST_NAME + " " + MIDDLE_NAME + " " + LAST_NAME
                
            break
            
            
    while True :
        try :
            print()
            USERNAME  = input( " PLEASE ENTER YOUR USERNAME : " )
            
            if USERNAME == "" :
                print( Fore.RED + " SORRY USERNAME CAN'T BE NULL !!! " )
                print( Fore.RED + " HENCE, PLEASE TRY AGAIN !!! " )
                print( Style.RESET_ALL )
                continue
            
            else :
                INSERT = " insert into USER_ACCOUNTS ( USER_NAME ) values('{}') ; ".format( USERNAME )
                CURSOR.execute( INSERT )
                print()
                break
        
        except :
            print( Fore.RED + " USERNAME ALREADY EXISTS !!! " )
            print( Fore.RED + " HENCE, PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            print()
            continue

    PASSWORD = PASSWORD_CREATION( USERNAME )
    
    while True :
        try :
            print()
            print( Fore.GREEN + Style.BRIGHT + " PLEASE AVOID USING '0' OR '+' SIGN BEFORE USER'S CONTACT !!! " )
            print( Style.RESET_ALL )
            print()
            USER_CONTACT = int ( eval ( input ( " PLEASE ENTER YOUR CONTACT NUMBER : " ) ) )
            CHECKING = str( USER_CONTACT )
        
            if  ( 7 <= len( CHECKING ) <= 13 ) :
                    try :
                        INSERT = " update USER_ACCOUNTS set USER_CONTACT = {} where USER_NAME = '{}' ; ".format( USER_CONTACT , USERNAME  )
                        CURSOR.execute( INSERT )
                        print()
                        break
            
                    except :
                        print()
                        print( Fore.RED + " CONTACT NUMBER ALREADY EXISTS !!! " )
                        print( Fore.RED + " HENCE, PLEASE TRY AGAIN !!! " )
                        print( Style.RESET_ALL )
                        print()
                        continue
            
            else :
                print()
                print( Fore.RED + " INVALID CONTACT !!! " )
                print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                print( Style.RESET_ALL )
                print()
                continue

        except :
            print( Fore.RED + " INVALID INPUT !!! " )
            print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
            print( Style.RESET_ALL )
            print()
            continue
        
    while True :
            FLAG1 = 0
            FLAG2 = 0
            print()
            print( Fore.GREEN + Style.BRIGHT + " EMAIL ADDRESS CAN'T BE MODIFIED LATER !!! " )
            print( Fore.GREEN + Style.BRIGHT + " THIS EMAIL ADDRESS WILL BE USED FOR SENDING YOU OTP !!! " )
            print( Style.RESET_ALL )
            print()
            EMAIL = input( " PLEASE ENTER YOUR EMAIL ADDRESS : " ).upper().strip()
            OTP = random.randrange( 99999 , 999999 )
            
            try :
                SERVER = smtplib.SMTP_SSL( "smtp.gmail.com" , 465 )
                SERVER.login( "railwaysofindia.1853@gmail.com" , "JaiHind@Indian" )
                SERVER.sendmail( "railwaysofindia.1853@gmail.com" , EMAIL , " YOUR VERIFICATION OTP IS " + str( OTP ) + "\n FOR SIGNING UP ON INDIAN RAILWAYS WITH USERNAME " + USERNAME )
                SERVER.quit()
                print( " OTP HAS BEEN SEND SUCCESSFULLY AT YOUR EMAIL ADDRESS " )
            
            
            except :
                print()
                print( Fore.RED + " PLEASE ENTER A VALID EMAIL ID !!! " )
                print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                print( Style.RESET_ALL )
                print()
                continue


            for ATTEMPTS in range( 0 , 4 , 1 ) :
                try :
                    OTP_INPUT = int ( eval ( input ( " PLEASE ENTER OTP SEND AT YOUR REGISTERED EMAIL ADDRESS : " ) ) )
                    if ( OTP == OTP_INPUT ) :
                        try :
                            INSERT = " update USER_ACCOUNTS set EMAIL_ACCOUNT = '{}' where USER_NAME = '{}' ; ".format( EMAIL , USERNAME  )
                            CURSOR.execute( INSERT )
                            print()
                            FLAG1 = FLAG2 = 1
                            break
                        
                        except :
                            print()
                            print( Fore.RED + " THIS EMAIL ID ALREADY EXISTS WITH ANOTHER USERNAME REGISTERED ON IT !!! " )
                            print( Fore.RED + " HENCE, PLEASE TRY AGAIN !!! " )
                            print( Fore.RED + " FOR ANY FURTHER QUERIES PLEASE CONTACT ADMINISTRATOR AT   !!! " )
                            print( Fore.RED + " GMAIL : INDIANRAILWAYS@GMAIL.COM " )
                            print( Fore.RED + " CONTACT : 9876543210 " )
                            print( Style.RESET_ALL )
                            print()
                            FLAG1 = -1
                            continue
            
                    else :
                        print()
                        print( Fore.RED + " ENTERED OTP IS INCORRECT !!! " )
                        print( Fore.RED + " HENCE, PLEASE TRY AGAIN !!! " )
                        print( Style.RESET_ALL )
                        print()
                        FLAG2 = -1
                        continue

                except :
                    print( Fore.RED + " INVALID INPUT !!! " )
                    print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
                    print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                    print( Style.RESET_ALL )
                    print()
                    FLAG1 = -1
                    continue
                
            if ( FLAG1 == -1 ) :
                print( Fore.RED + " YOU HAVE EXCEEDED THE MAXIMUM NUMBER OF TRIALS OF ENTERING EMAIL ID !!! " )
                print( Fore.RED + " PLEASE TRY AGAIN AFTER 1 HOUR !!! " )
                print( Style.RESET_ALL )
                print()
                break
            
            elif ( FLAG2 == -1 ) :
                print( Fore.RED + " YOU HAVE EXCEEDED THE MAXIMUM NUMBER OF TRIALS OF ENTERING EMAIL ID !!! " )
                print( Fore.RED + " PLEASE TRY AGAIN AFTER 1 HOUR !!! " )
                print( Style.RESET_ALL )
                print()
                break
            
            else :
                break

    while True :
        print()
        
        print( " M = MALE " , "\n" , "\n" , "F = FEMALE " , "\n" , "\n" , "LGBT = LESBIAN, GAY, BISEXUAL, TRANSGENDER " , "\n" , "\n" , "N = NOT TO MENTION " , "\n" )
        
        VALUE = input( " PLEASE ENTER USER'S GENDER : " ).upper().strip()
        
        if VALUE in [ "M" , "F" , "LGBT" , "N" ] :
            print()
            break
        
        else :
            print( Fore.RED + " INVALID INPUT !!! " )
            print( Fore.RED + " PLEASE ENTER A VALID CHOICE !!! " )
            print( Style.RESET_ALL )
            print()
            continue
        

    while True :
        try :
            print()
            print( " PLEASE ENTER YOUR DATE OF BIRTH IN THE FOLLOWING FORMAT " )

            print()
            
            DAY = int ( eval ( input ( " PLEASE ENTER DATE (dd) : " ) ) )

            print()
            
            MONTH = int ( eval ( input ( " PLEASE ENTER MONTH (mm) : " ) ) )

            print()
            
            YEAR = int ( eval ( input ( " PLEASE ENTER YEAR (yyyy): " ) ) )

            print()
            
            DATE = datetime.date( YEAR , MONTH , DAY )
            
            CURRENT_DATE = datetime.date.today()
            DIFFERENCE1 = str( CURRENT_DATE - DATE )
            DIFFERENCE2 = DIFFERENCE1[-14::-1] 
            DIFFERENCE3 = int( DIFFERENCE2[-1::-1] )
            
            if ( DIFFERENCE3 >= 3650 ) :
                DATE_OF_BIRTH = DATE
                print()
                break
            
            else :
                print( Fore.RED + " YOU ARE TOO SMALL TO SIGN UP !!! " )
                print( Fore.RED + " MINIMUM AGE REQUIRED TO SIGN UP IS 10 YEARS !!! " )
                print( Style.RESET_ALL )
                print()
                continue
            
        except :
            print( Fore.RED + " INVALID DATE OF BIRTH !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            print()
            continue
        
        
    SATISFY = CAPTCHA()
    
    
    if ( SATISFY == False ) :
        DELETE = " delete from USER_ACCOUNTS where USER_NAME = '{}' ".format( USERNAME )
        CURSOR.execute( DELETE )
        return False

    else :
        SERVER = smtplib.SMTP_SSL( "smtp.gmail.com" , 465 )
        SERVER.login( "railwaysofindia.1853@gmail.com" , "JaiHind@Indian" )
        SERVER.sendmail( "railwaysofindia.1853@gmail.com" , EMAIL , " THANK YOU FOR SIGNING UP WITH INDIAN RAILWAYS. YOUR USERNAME IS " + USERNAME + " \n AND PASSWORD IS " + PASSWORD + " !!! " )
        SERVER.quit()
        
        DICT = { "M" : "MALE" , "F" :  "FEMALE" , "LGBT" : "LESBIAN, GAY, BISEXUAL, TRANSGENDER" , "N" : "NOT TO MENTION" }
        GENDER = DICT[ VALUE ]
        
        INSERT1 = " update USER_ACCOUNTS set PASSWORD = '{}', NAME = '{}' , GENDER = '{}', DATE_OF_BIRTH = '{}' where USER_NAME = '{}' ; ".format( PASSWORD , NAME , GENDER , DATE_OF_BIRTH , USERNAME )
        CURSOR.execute( INSERT1 )
        
        print( GREETINGS() , NAME )
        print( " YOUR ACCOUNT IS SUCCESSFULLY CREATED !!! " )
        
        print()
        print()

        FILE_HANDLE = open( r"C:\Users\dell\Desktop\TIMELINES\USER_ACCOUNT_TIMELINE.dat" , "ab" )
        
        TIME_USER_ACCOUNT = datetime.datetime.today()
        USER_TIMELINE_LIST = [ USERNAME , str( USER_CONTACT ) , "ACCOUNT_SIGN_UP" , str( TIME_USER_ACCOUNT ) ]

        pickle.dump( USER_TIMELINE_LIST , FILE_HANDLE )

        FILE_HANDLE.close()

        return True



def ADMIN_LOGIN( TIME1 ) :
    
    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    UNIQUE_CODE = "IndianRailways@1853"
    
    for ATTEMPTS1 in range(0,4,1) :
        CODE = input( " PLEASE ENTER THE UNIQUE CODE : " )
        
        SATISFY1 = 0
        SATISFY2 = 0

        if ( CODE == UNIQUE_CODE ) :
            for ATTEMPTS2 in range( 0 , 4 , 1 ) :
                FLAG1 = 0
                FLAG2 = 0
                DATA = []
                USERNAME = input( " PLEASE ENTER YOUR USERNAME : " ).strip()

                SQL_QUERY_1 = " select * from ADMIN_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
                CURSOR.execute( SQL_QUERY_1 )
                DATA = CURSOR.fetchall()
                global ADMIN_CONTACT
                ADMIN_CONTACT = DATA[ 0 ][ 3 ] 
                
                if ( DATA == [] ) :
                    print( Fore.RED + " ACCOUNT DOES NOT EXISTS !!! " )
                    print( Style.RESET_ALL )
                    FLAG1 = -1
                    
                else :
                    PASSWORD = input( " PLEASE ENTER YOUR PASSWORD : " )
                    
                    TIME2 = datetime.datetime.now()
                    
                    DIFFERENCE_TIME = TIME2 - TIME1
                    STRING_DIFFERENCE = str( DIFFERENCE_TIME )
                    SPLITTING_STRING = STRING_DIFFERENCE.split( ":" )
                    DIFFERENCE_HOUR = int( SPLITTING_STRING[0] )
                    DIFFERENCE_MINUTE = int( SPLITTING_STRING[1] )
                    
                    if ( ( DIFFERENCE_HOUR >= 0 ) and ( DIFFERENCE_MINUTE > 10 ) ) :
                        FLAG2 = -1
                        break
                    
                    else :
                        SQL_QUERY_2 = "select PASSWORD, NAME from ADMIN_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
                        CURSOR.execute( SQL_QUERY_2 )
                        DATA1 = CURSOR.fetchall()
                        
                        if ( PASSWORD == DATA1[ 0 ][ 0 ] ) :
                            NAME = DATA1[ 0 ][ 1 ]
                            print( GREETINGS() , NAME )
                            FLAG1 = 1
                            break
                    
                        else :
                            print( Fore.RED + " WRONG PASSWORD !!! " )
                            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                            print( Style.RESET_ALL )
                            FLAG1 = -1
                            continue
                    
            if ( FLAG1 == -1 ) :
                print( Fore.RED + " YOU HAVE EXCEDEED THE MAXIMUM NUMBER OF YOUR TRIALS !!! " )
                print( Fore.RED + " PLEASE TRY AGAIN AFTER 1 HOUR !!! " )
                print( Style.RESET_ALL )
                SATISFY2 = -1
                break
            
            elif ( FLAG2 == -1 ) :
                print( Fore.RED + " SESSION TIMED OUT !!! " )
                print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                print( Style.RESET_ALL )
                SATISFY2 = -1
                break
            
            else :
                SATISFY2 = 1
                break
                
            
        else :
            print( Fore.RED + " INVALID UNIQUE CODE !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            SATISFY1 = -1
            continue
        
        break

        
    if ( SATISFY1 == -1 ) :
        print( Fore.RED + " YOUR TRIALS ARE OVER !!! " )
        print( Fore.RED + " PLEASE TRY AGAIN AFTER 1 HOUR !!! " )
        print( Style.RESET_ALL )
        return False
    
    elif ( SATISFY2 == -1 ) :
        return False
    
    else :

        FILE_HANDLE = open( r"C:\Users\dell\Desktop\TIMELINES\ADMIN_ACCOUNT_TIMELINE.dat" , "ab" )

        TIME_ADMIN_ACCOUNT = datetime.datetime.today()
        ADMIN_TIMELINE_LIST = [ USERNAME , str( ADMIN_CONTACT ) , "ACCOUNT_SIGN_IN" , str( TIME_ADMIN_ACCOUNT ) ]

        pickle.dump( ADMIN_TIMELINE_LIST , FILE_HANDLE )

        FILE_HANDLE.close()

        return True



def ADMIN_SIGN_UP() :
    
    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True

    UNIQUE_CODE = "IndianRailways@1853"

    FLAG = 0 

    for ATTEMPTS in range(0,4,1) :
        CODE = input( " PLEASE ENTER THE UNIQUE CODE : " )
        if ( CODE == UNIQUE_CODE ) :
   
            print()
            FIRST_NAME = input( " PLEASE ENTER YOUR FIRST NAME : " ).upper().strip()
            print()
            MIDDLE_NAME = input( " PLEASE ENTER YOUR MIDDLE NAME ( PRESS ENTER IF NOT ) : " ).upper().strip()
            print()
            LAST_NAME = input( " PLEASE ENTER YOUR LAST NAME : " ).upper().strip()
            print()
            
            if ( MIDDLE_NAME == "" ) :
                NAME = FIRST_NAME + " " + LAST_NAME

            else :
                NAME = FIRST_NAME + " " + MIDDLE_NAME + " " + LAST_NAME
                
                            
            while True :
                try :
                    print()
                    USERNAME  = input( " PLEASE ENTER YOUR USERNAME : " ).strip()
                    INSERT = " insert into ADMIN_ACCOUNTS ( USER_NAME ) values('{}') ; ".format( USERNAME )
                    CURSOR.execute( INSERT )
                    print()
                    break
                
                except :
                    print( Fore.RED + " USERNAME ALREADY EXISTS !!! " )
                    print( Fore.RED + " HENCE, PLEASE TRY AGAIN !!! " )
                    print( Style.RESET_ALL )
                    print()
                    continue

            PASSWORD = PASSWORD_CREATION( USERNAME )
            
            while True :
                try :
                    print()
                    print( Fore.GREEN + Style.BRIGHT + " PLEASE AVOID USING '0' OR '+' SIGN BEFORE ADMIN'S CONTACT !!! " )
                    print( Style.RESET_ALL )
                    print()
                    ADMIN_CONTACT = int ( eval ( input ( " PLEASE ENTER YOUR CONTACT NUMBER : " ) ) )
                    CHECKING = str( ADMIN_CONTACT )
                
                    if  ( 7 <= len( CHECKING ) <= 13 ) :
                            try :
                                INSERT = " update ADMIN_ACCOUNTS set ADMIN_CONTACT = {} where USER_NAME = '{}' ; ".format( ADMIN_CONTACT , USERNAME  )
                                CURSOR.execute( INSERT )
                                print()
                                break
                    
                            except :
                                print()
                                print( Fore.RED + " CONTACT NUMBER ALREADY EXISTS !!! " )
                                print( Fore.RED + " HENCE, PLEASE TRY AGAIN !!! " )
                                print( Style.RESET_ALL )
                                print()
                                continue
                    
                    else :
                        print()
                        print( Fore.RED + " INVALID CONTACT !!! " )
                        print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                        print( Style.RESET_ALL )
                        print()
                        continue

                except :
                    print( Fore.RED + " INVALID INPUT !!! " )
                    print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
                    print( Style.RESET_ALL )
                    print()
                    continue
                

            while True :
                print()
                print( " M = MALE " , "\n" , "F = FEMALE " , "\n" , "LGBT = LESBIAN, GAY, BISEXUAL, TRANSGENDER " , "\n" , "N = NOT TO MENTION " )
                
                VALUE = input( " PLEASE ENTER ADMIN'S GENDER : " ).upper().strip()
                
                if VALUE in [ "M" , "F" , "LGBT" , "N" ] :
                    print()
                    break
                
                else :
                    print( Fore.RED + " INVALID INPUT !!! " )
                    print( Fore.RED + " PLEASE ENTER A VALID CHOICE !!! " )
                    print( Style.RESET_ALL )
                    print()
                    continue
                

            while True :
                try :
                    print()
                    print( " PLEASE ENTER YOUR DATE OF BIRTH IN THE FOLLOWING FORMAT " )
                    
                    DAY = int ( eval ( input ( " PLEASE ENTER DATE (dd) : " ) ) )
                    MONTH = int ( eval ( input ( " PLEASE ENTER MONTH (mm) : " ) ) )
                    YEAR = int ( eval ( input ( " PLEASE ENTER YEAR (yyyy): " ) ) )
                    
                    DATE = datetime.date( YEAR , MONTH , DAY )
                    
                    CURRENT_DATE = datetime.date.today()
                    DIFFERENCE1 = str( CURRENT_DATE - DATE )
                    DIFFERENCE2 = DIFFERENCE1[-14::-1] 
                    DIFFERENCE3 = int( DIFFERENCE2[-1::-1] )
                    
                    if ( DIFFERENCE3 >= 3650 ) :
                        DATE_OF_BIRTH = DATE
                        print()
                        break
                    
                    else :
                        print( Fore.RED + " YOU ARE TOO SMALL TOO SIGN UP !!! " )
                        print( Fore.RED + " MINIMUM AGE REQUIRED TO SIGN UP IS 10 YEARS !!! " )
                        print( Style.RESET_ALL )
                        print()
                        continue
                    
                except :
                    print( Fore.RED + " INVALID DATE OF BIRTH !!! " )
                    print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                    print( Style.RESET_ALL )
                    print()
                    continue
                
            SATISFY = CAPTCHA()
            
            if ( SATISFY == False ) :
                DELETE = " delete from ADMIN_ACCOUNTS where USER_NAME = '{}' ".format( USERNAME  )
                CURSOR.execute( DELETE )
                return False

            else :
                DICT = { "M" : "MALE" , "F" :  "FEMALE" , "LGBT" : "LESBIAN, GAY, BISEXUAL, TRANSGENDER" , "N" : "NOT TO MENTION" }
                GENDER = DICT[ VALUE ]
                INSERT1 = " update ADMIN_ACCOUNTS set PASSWORD = '{}', NAME = '{}' , GENDER = '{}', DATE_OF_BIRTH = '{}' ; ".format( PASSWORD , NAME , GENDER , DATE_OF_BIRTH )
                CURSOR.execute( INSERT1 )
                print( GREETINGS() , NAME )
                print( " YOUR ACCOUNT IS SUCCESSFULLY CREATED !!! " )

                FILE_HANDLE = open( r"C:\Users\dell\Desktop\TIMELINES\ADMIN_ACCOUNT_TIMELINE.dat" , "ab" )
                
                TIME_ADMIN_ACCOUNT = datetime.datetime.today()
                ADMIN_TIMELINE_LIST = [ USERNAME , str( ADMIN_CONTACT ) , "ACCOUNT_SIGN_UP" , str( TIME_ADMIN_ACCOUNT ) ]

                pickle.dump( ADMIN_TIMELINE_LIST , FILE_HANDLE )

                FILE_HANDLE.close()

                return True

        else :
            print( Fore.RED + " INVALID UNIQUE CODE !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            FLAG = -1
            continue

    if ( FLAG == -1 ) :
        print( Fore.RED + " YOUR TRIALS ARE OVER !!! " )
        print( Fore.RED + " PLEASE TRY AGAIN AFTER 1 HOUR !!! " )
        print( Style.RESET_ALL )



def MAIN_PROGRAM_USER() :
    
    while True :
        
        try :
            print()
            print( Fore.CYAN )
            
            print( " 1. TICKET BOOKING " , "\n" , "\n" , "2. TICKET CHECKING " , "\n" , "\n" , "3. TICKET MODIFYING " , "\n" , "\n" , "4. TICKET CANCELLING " , "\n" )
            print( " 5. ACCOUNT DETAILS " , "\n" , "\n" , "6. MODIFY ACCOUNT " , "\n" , "\n" , "7. DELETE ACCOUNT " , "\n" , "\n" , "8. LOG OUT " , "\n" )

            print( Style.RESET_ALL )
            
            CHOICE = int ( eval ( input ( " PLEASE ENTER YOUR CHOICE : " ) ) )
            
            print( ansi.clear_screen() )
            print()
            print()
        
            if ( CHOICE == 1 ) :
                TICKET_BOOKING()
                continue
            
            elif ( CHOICE == 2 ) :
                TICKET_CHECKING()
                continue
            
            elif ( CHOICE == 3 ) :
                print( Fore.RED + " FOR MODIFYING THE TICKET YOU HAVE TO FIRST CANCEL THE TICKET AND THEN REBOOK IT !!! " )
                print( Style.RESET_ALL )
                
                CHECK = TICKET_CANCELLING()
                
                if ( CHECK == True ) :
                    TICKET_BOOKING()
                    
                else :
                    print( Fore.RED + " UNABLE TO CANCEL THE TICKET !!! " )
                    print( Fore.RED + " HENCE, PLEASE TRY AGAIN !!! " )
                    print( Style.RESET_ALL )
                    continue
            
            elif ( CHOICE == 4 ) :
                TICKET_CANCELLING()
                continue
            
            elif ( CHOICE == 5 ) :
                USER_ACCOUNT_DETAILS()
                continue
            
            elif ( CHOICE == 6 ) :
                USER_MODIFY_ACCOUNT()
                continue
            
            elif ( CHOICE == 7 ) :
                USER_DELETE_ACCOUNT()
                continue
                 
            elif ( CHOICE == 8 ) :
                print( " THANK YOU !!! " )
                break
            
            else:
                print( Fore.RED + " INVALID INPUT !!! " )
                print( Fore.RED + " PLEASE ENTER A VALID CHOICE !!! " )
                print( Style.RESET_ALL )
                continue
        
        except :
            print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            continue

        

def TICKET_BOOKING() :
    
    import mysql.connector as MS
    MYCONNECTION = MS.connect ( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    while True :
        CHOICE = input( " DO YOU WANT TO CONTINUE OR NOT ?  (Y/N);(y/n) " )
        print()
        print()
        
        if ( CHOICE in [ "Y" , "y" ] ) :
            while True :
                PNR_NUMBER = random.randrange( ( 10 ** 12 ) , ( 10 ** 13 ) )
                
                SQL_QUERY_1 = " select PNR_NUMBER from RAILWAY_TICKET where PNR_NUMBER = {} ; ".format( PNR_NUMBER )
                CURSOR.execute( SQL_QUERY_1 )
                DATA = CURSOR.fetchall()
                
                try :
                    PNR_NUMBER == DATA[ 0 ][ 0 ]
                    continue
                
                except :
                    break
                
            print ( " PLEASE NOTE YOUR PNR NUMBER : " , PNR_NUMBER )
            print()

            while True :
                
                try :
                    HEAD_COUNT_A = int ( eval ( input ( " PLEASE ENTER THE NUMBER OF ADULTS ( AGE > 12 YEARS ) : " ) ) )
                    print()
                    break
                
                except :
                    print( Fore.RED + " INVALID INPUT !!! " )
                    print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
                    print( Style.RESET_ALL )
                    print()
                    continue
                
            while True :
                
                try :
                    HEAD_COUNT_K = int ( eval ( input ( " PLEASE ENTER THE NUMBER OF KIDS ( 5 YEARS <= AGE <= 12 YEARS ) : " ) ) )
                    print()
                    break
                
                except :
                    print( Fore.RED + " INVALID INPUT !!! " )
                    print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
                    print( Style.RESET_ALL )
                    print()
                    continue
                
            while True :
                
                try :
                    HEAD_COUNT_I = int ( eval ( input ( " PLEASE ENTER THE NUMBER OF INFANTS ( 5 YEARS < AGE ) : " ) ) )
                    print()
                    break
                
                except :
                    print( Fore.RED + " INVALID INPUT !!! " )
                    print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
                    print( Style.RESET_ALL )
                    print()
                    continue
                
            if ( HEAD_COUNT_I > HEAD_COUNT_A ) :
                INFANT_SEAT = (( HEAD_COUNT_I - HEAD_COUNT_A ) // 2 )
                
                print( Fore.RED + " AS INFANTS ARE MORE THAN ADULTS HENCE , " , INFANT_SEAT , " THESE NUMBER OF TICKETS WILL BE BOOKED EXTRA !!! " )
                print( Style.RESET_ALL )
                print()
                
                SEAT_BOOKED = INFANT_SEAT + HEAD_COUNT_A + HEAD_COUNT_K
                
            else :
                SEAT_BOOKED = HEAD_COUNT_A + HEAD_COUNT_K
                  
                    
            while True :
                 
                try :
                    print( " PLEASE ENTER YOUR DATE OF GOING IN THE FOLLWING FORMAT " )
                    print()
                    
                    DAY_G = int ( eval ( input ( " PLEASE ENTER DATE (dd) : " ) ) )
                    print()
                    
                    MONTH_G = int ( eval ( input ( " PLEASE ENTER MONTH (mm) : " ) ) )
                    print()
                    
                    YEAR_G = int( eval ( input ( " PLEASE ENTER YEAR (yyyy): " ) ) )
                    print()
                    
                    DATE_G = datetime.date( YEAR_G , MONTH_G , DAY_G )
                    CURRENT_DATE = datetime.date.today()
                    DIFFERENCE1_G = str( DATE_G - CURRENT_DATE )
                    DIFFERENCE2_G = DIFFERENCE1_G[-14::-1] 
                    DIFFERENCE3_G = int( DIFFERENCE2_G[-1::-1] )
                    
                    if ( -1 < DIFFERENCE3_G <= 93 ) :
                        DATE_GOING = DATE_G
                        break
                    
                    else :
                        print( Fore.RED + " YOU CAN ONLY BOOK THE TICKET UPTO 93 DAYS FROM THE DATE OF BOOKING IN ADVANCE !!! " )
                        print( Fore.RED + " HENCE, PLEASE TRY AGAIN !!! " )
                        print( Style.RESET_ALL )
                        print()
                        continue
                    
                except :
                    print( Fore.RED + " INVALID DATE !!! " )
                    print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                    print( Style.RESET_ALL )
                    print()
                    continue
                
            while True :
                RETURN = input( " DO YOU WANT A RETURN TICKET ALSO ? (Y/N);(y/n) " )
                print()
                if ( RETURN in [ "Y" , "y" ] ) :
                    try :
                        print( " PLEASE ENTER DATE OF RETURNING " )
                        print()
                        
                        DAY_R = int ( eval ( input ( " PLEASE ENTER DATE (dd) : " ) ) )
                        print()
                        
                        MONTH_R = int ( eval ( input ( " PLEASE ENTER MONTH (mm) : " ) ) )
                        print()
                        
                        YEAR_R = int ( eval ( input ( " PLEASE ENTER YEAR (yyyy): " ) ) )
                        print()
                        
                        DATE_R = datetime.date( YEAR_R , MONTH_R , DAY_R )
                        CURRENT_DATE = datetime.date.today()
                        DIFFERENCE1_R = str( DATE_R - CURRENT_DATE )
                        DIFFERENCE2_R = DIFFERENCE1_R[-14::-1] 
                        DIFFERENCE3_R = int( DIFFERENCE2_R[-1::-1] )
                        
                        if ( -1 < DIFFERENCE3_R <= 93 ) :
                            DATE_RETURN = DATE_R
                            break
                        
                        else :
                            print( Fore.RED + " YOU CAN ONLY BOOK THE TICKET UPTO 93 DAYS FROM THE DATE OF BOOKING IN ADVANCE !!! " )
                            print( Fore.RED + " HENCE, PLEASE TRY AGAIN !!! " )
                            print( Style.RESET_ALL )
                            print()
                            continue
                   
                    except :
                        print( Fore.RED + " INVALID DATE !!! " )
                        print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                        print( Style.RESET_ALL )
                        print()
                        continue

                else :
                    DATE_RETURN = '0000-00-00'
                    break
                
            STARTING_POINT = input( " PLEASE ENTER STARTING POINT : " ).upper().strip()
            print()
            ENDING_POINT = input( " PLEASE ENTER DESTINATION POINT  : " ).upper().strip()
            print()

            for LOOP1 in range( 0 , HEAD_COUNT_A , 1 ) :
                
                PASSENGER_NAME_TEMP = input( " PLEASE ENTER PASSENGER'S NAME : " ).upper()
                print()
                
                SPLITTING_PASSENGER_NAME = PASSENGER_NAME_TEMP.split()
                
                NAME_TEMP = ""
                
                for NAME in range( 0 , len( SPLITTING_PASSENGER_NAME ) , 1 ) :
                    NAME_TEMP = NAME_TEMP + " " + SPLITTING_PASSENGER_NAME[NAME]
                    
                PASSENGER_NAME = NAME_TEMP.strip()
                
                while True :
                    print( " AD = ADHAAR CARD " , "\n" , "\n" , "PP = PASSPORT " , "\n" , "\n" , "DL = DRIVING LICENSE " , "\n" , "\n" , "VC = VOTER ID CARD " , "\n" , "\n" , "PN = PAN CARD " )
                    VALUE1 = input( " PLEASE CHOOSE ID TYPE : ").upper()
                    print()
                    
                    if VALUE1 in [ "AD" , "PP" , "DL" , "VC" , "PN" ] :
                        if ( VALUE1 == "AD" ) :
                            
                            while True :
                                ID_NUMBER = input( " PLEASE ENTER PASSENGER'S ADHAAR NUMBER : " ).strip()
                                print()
                                
                                if ( len( ID_NUMBER ) != 16 ) :
                                    print( Fore.RED + " PLEASE ENTER A VALID ADHAAR NUMBER !!! " )
                                    print( Style.RESET_ALL )
                                    print()
                                    continue
                                
                                else :
                                    break
                    
                        elif ( VALUE1 == "PP" ) :
                            while True :
                                ID_NUMBER = input( " PLEASE ENTER PASSENGER'S PASSPORT NUMBER : " ).strip()
                                print()
                                
                                if ( 7 <= len( ID_NUMBER ) <= 10 ) :
                                    break
                                
                                else :
                                    print( Fore.RED + " PLEASE ENTER A VALID PASSPORT NUMBER !!! " )
                                    print( Style.RESET_ALL )
                                    print()
                                    continue
                                
                        elif ( VALUE1 == "DL" ) :
                            while True :
                                ID_NUMBER = input( " PLEASE ENTER PASSENGER'S DRIVING LICENSE NUMBER : " ).strip()
                                print()
                                
                                if ( len(ID_NUMBER)!=15 ) :
                                    print( Fore.RED + " PLEASE ENTER A VALID DRIVING LICENSE NUMBER !!! " )
                                    print( Style.RESET_ALL )
                                    print()
                                    continue
                                
                                else :
                                    break
                                
                        elif ( VALUE1 == "VC" ) :
                            while True :
                                ID_NUMBER = input( " PLEASE ENTER PASSENGER'S VOTER ID CARD NUMBER : " ).strip()
                                print()
                                
                                if ( len(ID_NUMBER) !=10 ) :
                                    print( Fore.RED + " PLEASE ENTER A VALID VOTER ID CARD NUMBER !!! " )
                                    print( Style.RESET_ALL )
                                    print()
                                    continue
                                
                                else :
                                    break
                                
                        elif ( VALUE1 == "PN" ) :
                            while True :
                                ID_NUMBER = input( " PLEASE ENTER PASSENGER'S PAN CARD NUMBER : " ),strip()
                                print()
                                
                                if ( len( ID_NUMBER ) != 15 ) :
                                    print( Fore.RED + " PLEASE ENTER A VALID PAN CARD NUMBER !!! " )
                                    print( Style.RESET_ALL )
                                    print()
                                    continue
                                
                                else :
                                    break
                            
                        else :
                            print( Fore.RED + " INVALID CHOICE !!! " )
                            print( Fore.RED + " PLEASE ENTER A VALID CHOICE !!! " )
                            print( Style.RESET_ALL )
                            print()
                            continue
                        
                        DICT1 = { "AD" : "ADHAAR CARD" , "PP" : "PASSPORT" , "DL" : "DRIVING LICENSE" , "VC" : "VOTER ID CARD" , "PN" : "PAN CARD" }
                        ID_TYPE = DICT1[VALUE1]
                        
                        SQL_QUERY_2 = " select ID_NUMBER , ID_TYPE , PASSENGER_NAME from RAILWAY_TICKET where ID_NUMBER = '{}' ; ".format( ID_NUMBER )
                        CURSOR.execute( SQL_QUERY_2 )
                        DATA = CURSOR.fetchall()
                        
                        try :
                            for ROWS in range(0,len(DATA),1) :
                                
                                if ( ID_NUMBER == DATA[ROWS][0] and ID_TYPE == DATA[ROWS][1] and PASSENGER_NAME == DATA[ROWS][2] ) :
                                    break
                                
                                else :
                                    print( Fore.RED + " THIS ID ALREADY EXISTS WITH ANOTHER NAME REGISTERED ON IT !!! " )
                                    print( Fore.RED + " HENCE, PLEASE TRY AGAIN !!! " )
                                    print( Fore.RED + " FOR ANY FURTHER QUERIES PLEASE CONTACT ADMINISTRATOR AT   !!! " )
                                    print( Fore.RED + " GMAIL : INDIANRAILWAYS@GMAIL.COM " )
                                    print( Fore.RED + " CONTACT : 9876543210 " )
                                    print( Style.RESET_ALL )
                                    print()
                                    continue
                        
                        except :
                            break

                    
                    INSERT = " insert into RAILWAY_TICKET ( PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )  values( {} , '{}' , '{}' , '{}' ) ".format( PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                    CURSOR.execute( INSERT )
                    break
                    
                ( PASSENGER_CONTACT , PASSENGER_AGE , PASSENGER_GENDER , QUOTA , CLASS , PREFERRED_BERTH , MEAL ) = TICKET_BOOKING_DETAILS()
                INSERT1 = " update RAILWAY_TICKET set SEAT_BOOKED = {} where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( SEAT_BOOKED , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT2 = " update RAILWAY_TICKET set DATE_GOING = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( DATE_GOING , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE ) 
                INSERT3 = " update RAILWAY_TICKET set STARTING_POINT = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( STARTING_POINT , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT4 = " update RAILWAY_TICKET set ENDING_POINT = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( ENDING_POINT , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT5 = " update RAILWAY_TICKET set DATE_RETURN = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( DATE_RETURN , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT6 = " update RAILWAY_TICKET set PASSENGER_CONTACT = {} where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( PASSENGER_CONTACT , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE ) 
                INSERT7 = " update RAILWAY_TICKET set PASSENGER_AGE = {} where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( PASSENGER_AGE , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT8 = " update RAILWAY_TICKET set PASSENGER_GENDER = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( PASSENGER_GENDER , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT9 = " update RAILWAY_TICKET set QUOTA = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( QUOTA , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT10 = " update RAILWAY_TICKET set CLASS = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( CLASS , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE ) 
                INSERT11 = " update RAILWAY_TICKET set PREFERRED_BERTH = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( PREFERRED_BERTH , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT12 = " update RAILWAY_TICKET set MEAL = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( MEAL , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT13 = " update RAILWAY_TICKET set PASSENGER_TYPE = 'ADULT' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT14 = " update RAILWAY_TICKET set USER_CONTACT = {} where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( USER_CONTACT , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                
                CURSOR.execute( INSERT1 )
                CURSOR.execute( INSERT2 )
                CURSOR.execute( INSERT3 )
                CURSOR.execute( INSERT4 )
                CURSOR.execute( INSERT5 )
                CURSOR.execute( INSERT6 )
                CURSOR.execute( INSERT7 )
                CURSOR.execute( INSERT8 )
                CURSOR.execute( INSERT9 )
                CURSOR.execute( INSERT10 )
                CURSOR.execute( INSERT11 )
                CURSOR.execute( INSERT12 )
                CURSOR.execute( INSERT13 )
                CURSOR.execute( INSERT14 )
                
            for LOOP2 in range( 0 , HEAD_COUNT_K , 1 ) :
                while True :

                    PASSENGER_NAME_TEMP = input( " PLEASE ENTER PASSENGER'S NAME : " ).upper()
                    print()
                    SPLITTING_PASSENGER_NAME = PASSENGER_NAME_TEMP.split()
                    
                    NAME_TEMP = ""
                    
                    for NAME in range( 0 , len( SPLITTING_PASSENGER_NAME ) , 1 ) :
                        NAME_TEMP = NAME_TEMP + " " + SPLITTING_PASSENGER_NAME[NAME]
                        
                    PASSENGER_NAME = NAME_TEMP.strip()
                    
                    print( " AD = ADHAAR CARD " , "\n" , "PP = PASSPORT " ) 
                    VALUE1 = input( " PLEASE CHOOSE ID TYPE : ").upper().strip()
                    print()
                    
                    if VALUE1 in [ "AD" , "PP" ] :
                        
                        if ( VALUE1 == "AD" ) :
                            
                            while True :
                                ID_NUMBER = input( " PLEASE ENTER PASSENGER'S ADHAAR NUMBER : " ).strip()
                                print()
                                
                                if ( len( ID_NUMBER ) != 16 ) :
                                    print( Fore.RED + " PLEASE ENTER A VALID ADHAAR NUMBER !!! " )
                                    print( Style.RESET_ALL )
                                    print()
                                    continue
                                
                                else :
                                    break
                    
                        elif ( VALUE1 == "PP" ) :
                            while True :
                                ID_NUMBER = input( " PLEASE ENTER PASSENGER'S PASSPORT NUMBER : " ).strip()
                                print()
                                
                                if ( 7 <= len( ID_NUMBER ) <= 10 ) :
                                    break
                                
                                else :
                                    print( Fore.RED + " PLEASE ENTER A VALID PASSPORT NUMBER !!! " )
                                    print( Style.RESET_ALL )
                                    print()
                                    continue
                                
                            
                        DICT1 = { "AD" : "ADHAAR CARD" , "PP" : "PASSPORT" }
                        ID_TYPE = DICT1[ VALUE1 ]
                        
                        SQL_QUERY_2 = " select ID_NUMBER , ID_TYPE , NAME from RAILWAY_TICKET where ID_NUMBER = '{}' ; ".format( ID_NUMBER )
                        CURSOR.execute( SQL_QUERY_2 )
                        DATA = CURSOR.fetchall()
                        
                        try :
                            for ROWS in range( 0 , len( DATA ) , 1 ) :
                                if ( ID_NUMBER == DATA[ ROWS ][ 0 ] and ID_TYPE == DATA[ ROWS ][ 1 ] and PASSENGER_NAME == DATA[ ROWS ][ 2 ] ) :
                                    break
                                
                                else :
                                    print( Fore.RED + " THIS ID ALREADY EXISTS WITH ANOTHER NAME REGISTERED ON IT !!! " )
                                    print( Fore.RED + " HENCE, PLEASE TRY AGAIN !!! " )
                                    print( Fore.RED + " FOR ANY FURTHER QUERIES PLEASE CONTACT ADMINISTRATOR AT   !!! " )
                                    print( Fore.RED + " GMAIL : INDIANRAILWAYS@GMAIL.COM " )
                                    print( Fore.RED + " CONTACT : 9876543210 " )
                                    print( Style.RESET_ALL )
                                    print()
                                    continue
                        
                        except :
                            break
                        

                    INSERT = " insert into RAILWAY_TICKET ( PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )  values( {} , '{}' , '{}' , '{}' ) ".format( PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                    CURSOR.execute( INSERT )
                    break
                    
                ( PASSENGER_CONTACT , PASSENGER_AGE , PASSENGER_GENDER , QUOTA , CLASS , PREFERRED_BERTH , MEAL ) = TICKET_BOOKING_DETAILS()
                INSERT1 = " update RAILWAY_TICKET set SEAT_BOOKED = {} where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( SEAT_BOOKED , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT2 = " update RAILWAY_TICKET set DATE_GOING = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( DATE_GOING , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE ) 
                INSERT3 = " update RAILWAY_TICKET set STARTING_POINT = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( STARTING_POINT , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT4 = " update RAILWAY_TICKET set ENDING_POINT = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( ENDING_POINT , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT5 = " update RAILWAY_TICKET set DATE_RETURN = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( DATE_RETURN , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT6 = " update RAILWAY_TICKET set PASSENGER_CONTACT = {} where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( PASSENGER_CONTACT , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE ) 
                INSERT7 = " update RAILWAY_TICKET set PASSENGER_AGE = {} where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( PASSENGER_AGE , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT8 = " update RAILWAY_TICKET set PASSENGER_GENDER = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( PASSENGER_GENDER , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT9 = " update RAILWAY_TICKET set QUOTA = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( QUOTA , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT10 = " update RAILWAY_TICKET set CLASS = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( CLASS , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE ) 
                INSERT11 = " update RAILWAY_TICKET set PREFERRED_BERTH = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( PREFERRED_BERTH , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT12 = " update RAILWAY_TICKET set MEAL = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( MEAL , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT13 = " update RAILWAY_TICKET set PASSENGER_TYPE = 'KID' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                INSERT14 = " update RAILWAY_TICKET set USER_CONTACT = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_NUMBER = '{}' and ID_TYPE = '{}' ".format( USER_CONTACT , PNR_NUMBER , PASSENGER_NAME , ID_NUMBER , ID_TYPE )
                
                CURSOR.execute( INSERT1 )
                CURSOR.execute( INSERT2 )
                CURSOR.execute( INSERT3 )
                CURSOR.execute( INSERT4 )
                CURSOR.execute( INSERT5 )
                CURSOR.execute( INSERT6 )
                CURSOR.execute( INSERT7 )
                CURSOR.execute( INSERT8 )
                CURSOR.execute( INSERT9 )
                CURSOR.execute( INSERT10 )
                CURSOR.execute( INSERT11 )
                CURSOR.execute( INSERT12 )
                CURSOR.execute( INSERT13 )
                CURSOR.execute( INSERT14 )
                
            for LOOP3 in range( 0 , HEAD_COUNT_I , 1 ) :
                PASSENGER_TYPE = "INFANT"
                INSERT = " insert into RAILWAY_TICKET ( PNR_NUMBER , PASSENGER_NAME , PASSENGER_TYPE )  values( {} , '{}' , '{}' ) ".format( PNR_NUMBER , PASSENGER_NAME , PASSENGER_TYPE )
                CURSOR.execute( INSERT )
                                
                ( PASSENGER_CONTACT , PASSENGER_AGE , PASSENGER_GENDER , QUOTA , CLASS , PREFERRED_BERTH , MEAL ) = TICKET_BOOKING_DETAILS()
                INSERT1 = " update RAILWAY_TICKET set SEAT_BOOKED = {} where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and PASSENGER_TYPE = 'INFANT' ".format( SEAT_BOOKED , PNR_NUMBER , PASSENGER_NAME )
                INSERT2 = " update RAILWAY_TICKET set DATE_GOING = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and PASSENGER_TYPE = 'INFANT' ".format( DATE_GOING , PNR_NUMBER , PASSENGER_NAME ) 
                INSERT3 = " update RAILWAY_TICKET set STARTING_POINT = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and PASSENGER_TYPE = 'INFANT' ".format( STARTING_POINT , PNR_NUMBER , PASSENGER_NAME )
                INSERT4 = " update RAILWAY_TICKET set ENDING_POINT = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and PASSENGER_TYPE = 'INFANT' ".format( ENDING_POINT , PNR_NUMBER , PASSENGER_NAME )
                INSERT5 = " update RAILWAY_TICKET set DATE_RETURN = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and PASSENGER_TYPE = 'INFANT' ".format( DATE_RETURN , PNR_NUMBER , PASSENGER_NAME )
                INSERT6 = " update RAILWAY_TICKET set PASSENGER_CONTACT = {} where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and PASSENGER_TYPE = 'INFANT' ".format( PASSENGER_CONTACT , PNR_NUMBER , PASSENGER_NAME ) 
                INSERT7 = " update RAILWAY_TICKET set PASSENGER_AGE = {} where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and PASSENGER_TYPE = 'INFANT' ".format( PASSENGER_AGE , PNR_NUMBER , PASSENGER_NAME )
                INSERT8 = " update RAILWAY_TICKET set PASSENGER_GENDER = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and PASSENGER_TYPE = 'INFANT' ".format( PASSENGER_GENDER , PNR_NUMBER , PASSENGER_NAME )
                INSERT9 = " update RAILWAY_TICKET set QUOTA = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and PASSENGER_TYPE = 'INFANT' ".format( QUOTA , PNR_NUMBER , PASSENGER_NAME )
                INSERT10 = " update RAILWAY_TICKET set CLASS = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and PASSENGER_TYPE = 'INFANT' ".format( CLASS , PNR_NUMBER , PASSENGER_NAME ) 
                INSERT11 = " update RAILWAY_TICKET set PREFERRED_BERTH = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and PASSENGER_TYPE = 'INFANT' ".format( PREFERRED_BERTH , PNR_NUMBER , PASSENGER_NAME )
                INSERT12 = " update RAILWAY_TICKET set MEAL = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and PASSENGER_TYPE = 'INFANT' ".format( MEAL , PNR_NUMBER , PASSENGER_NAME )
                INSERT13 = " update RAILWAY_TICKET set USER_CONTACT = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and PASSENGER_TYPE = 'INFANT' ".format( USER_CONTACT , PNR_NUMBER , PASSENGER_NAME )
                
                CURSOR.execute( INSERT1 )
                CURSOR.execute( INSERT2 )
                CURSOR.execute( INSERT3 )
                CURSOR.execute( INSERT4 )
                CURSOR.execute( INSERT5 )
                CURSOR.execute( INSERT6 )
                CURSOR.execute( INSERT7 )
                CURSOR.execute( INSERT8 )
                CURSOR.execute( INSERT9 )
                CURSOR.execute( INSERT10 )
                CURSOR.execute( INSERT11 )
                CURSOR.execute( INSERT12 )
                CURSOR.execute( INSERT13 )
                
            print( " BOOKED SUCCESSFULLY !!! " )
            print( " SEATS BOOKED FOR THIS PNR NUMBER" , PNR_NUMBER , "ARE" , SEAT_BOOKED , "!!! " )
            print( " HAVE A SAFE AND HAPPY JOURNEY !!! " )
            print()


            FILE_HANDLE = open( r"C:\Users\dell\Desktop\TIMELINES\USER_TICKET_TIMELINE.txt" , "a" )
            
            TIME_USER_TICKET = datetime.datetime.today()
            USER_TICKET_TIMELINE_LIST = [ str( USER_CONTACT ) , "\t" , "TICKET_BOOKING" , "\t" , str( SEAT_BOOKED ) , "\t" , str( PNR_NUMBER ) , "\t" , str( TIME_USER_TICKET ) , "\n" ]

            FILE_HANDLE.writelines( USER_TICKET_TIMELINE_LIST )

            FILE_HANDLE.close()
            
            continue
        
        else :
            print( " THANK YOU " )
            break
        


def TICKET_BOOKING_DETAILS() :

    while True :
        try :
            print( Fore.GREEN + Style.BRIGHT + " PLEASE AVOID USING '0' OR '+' SIGN BEFORE PASSENGER'S CONTACT !!! " )
            print( Style.RESET_ALL )
            print()
            
            PASSENGER_CONTACT = int ( eval ( input ( " PLEASE ENTER PASSENGER'S CONTACT : " ) ) )
            CHECKING = str( PASSENGER_CONTACT )
            
            if  ( 7 <= len( CHECKING ) <= 13 ) :
                break
            
            else :
                print( Fore.RED + " INVALID CONTACT NUMBER !!! \n" )
                print( Fore.RED + " PLEASE TRY AGAIN !!! \n" )
                print( Style.RESET_ALL )
                print()
                continue

        except :
            print( Fore.RED + " INVALID INPUT !!! \n" )
            print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! \n" )
            print( Style.RESET_ALL )
            print()
            continue
        
    while True :
        PASSENGER_AGE = int ( eval ( input ( " PLEASE ENTER PASSENGER'S AGE : " ) ) )
        print()
        
        if ( type(PASSENGER_AGE) == int ) :
            break
        
        else :
            print( Fore.RED + " INVALID INPUT !!! " )
            print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
            print( Style.RESET_ALL )
            print()
            continue

    while True :
        print( " M = MALE " , "\n" , "F = FEMALE " , "\n" , "LGBT = LESBIAN, GAY, BISEXUAL, TRANSGENDER" , "\n" , "N = NOT TO MENTION " )
        VALUE2 = input( " PLEASE ENTER PASSENGER'S GENDER : " ).upper().strip()
        print()
        
        if VALUE2 in [ "M" , "F" , "LGBT" , "N" ] :
            break
        
        else :
            print( Fore.RED + " INVALID INPUT !!! " )
            print( Fore.RED + " PLEASE ENTER A VALID CHOICE !!! " )
            print( Style.RESET_ALL )
            print()
            continue
        
    while True :
        print( " GN = GENERAL QUOTA " , "\n" , "\n" , "TQ = TATKAL QUOTA " , "\n" , "\n" , "PT = PREMIUM TATKAL QUOTA " , "\n" , "\n" , "LD = LADIES QUOTA " , "\n" )
        print( " SS = LOWER BERTH QUOTA " , "\n" , "\n" , "HP = PHYSICALLY HANDICAPPED QUOTA " , "\n" , "\n" , "HO = HEADQUARTERS/HIGH OFFICIAL QUOTA " , "\n" , "\n" , "YU = YUVA QUOTA " , "\n" )
        print( " PH = PARLIAMENT HOUSE QUOTA " , "\n" , "\n" , "DF = DEFENCE QUOTA " , "\n" , "\n" , "FT = FOREIGNER TOURIST QUOTA " , "\n" , "\n" , "DP = DUTY PASS " , "\n" )
        print()
        
        VALUE3 = input( " PLEASE CHOOSE QUOTA : " ).upper().strip()
        print()
        
        if VALUE3 in [ "GN" , "TQ" , "PT" , "LD" , "SS" , "HP" , "HO" , "YU" , "PH" , "DF" , "FT" , "DP" ] :
            break
        
        else :
            print( Fore.RED + " INVALID INPUT !!! " )
            print( Fore.RED + " PLEASE ENTER A VALID CHOICE !!! " )
            print( Style.RESET_ALL )
            print()
            continue
                
    while True :    
        print( " EA = ANUBHUTI CLASS " , "\n" , "\n" , "1A = AC FIRST CLASS " , "\n" , "\n" , "EC = EXECUTIVE CHAIR CAR " , "\n" , "\n" , "2A = AC 2 TIER " , "\n" , "\n" , "SL = SLEEPER " , "\n" )
        print( " FC = FIRST CLASS" , "\n" , "\n" , "3A = AC 3 TIER " , "\n" , "\n" , "3E = AC 3 ECONOMY " , "\n" , "\n" , "CC = AC CHAIR CAR " , "\n" , "\n" , "2S = SECOND SITTING " , "\n" )
        print()
        
        VALUE4 = input( " PLEASE CHOOSE CLASS : " ).upper().strip()
        print()
        
        if VALUE4 in [ "EA" , "1A" , "EC" , "2A" , "SL" , "FC" , "3A" , "3E" , "CC" , "2S" ] :
            break
        
        else :
            print( Fore.RED + " INVALID INPUT !!! " )
            print( Fore.RED + " PLEASE ENTER A VALID CHOICE !!! " )
            print( Style.RESET_ALL )
            print()
            continue
                
    if VALUE4 in [ "2A" , "FC" , "3A" , "3E" , "SL" ] :
        if VALUE4 in [ "2A" , "FC" ] :
            while True :
                print( " LB = LOWER BERTH " , "\n" , "UB = UPPER BERTH " )
                print()
                VALUE5 = input( " PLEASE ENTER PREFERRED BERTH : " ).upper().strip()
                print()
                
                if VALUE5 in [ "LB" , "UB" ] :
                    break
                
                else :
                    print( Fore.RED + " INVALID INPUT !!! " )
                    print( Fore.RED + " PLEASE ENTER A VALID CHOICE !!! " )
                    print( Style.RESET_ALL )
                    print()
                    continue
                        
        else :
             while True :
                print( " LB = LOWER BERTH " , "\n" , "\n" , "MB = MIDDLE BERTH " , "\n" , "\n" , "UB = UPPER BERTH " , "\n" )
                print( " SL = SIDE LOWER BERTH " , "\n" , "\n" , "SU = SIDE UPPER BERTH " , "\n" )
                print()
                
                VALUE5 = input( " PLEASE ENTER PREFERRED BERTH : " ).upper().strip()
                print()
                
                if VALUE5 in [ "LB" , "UB" , "MB" , "SL" , "SU" ] :
                    break
                
                else :
                    print( Fore.RED + " INVALID INPUT !!! " )
                    print( Fore.RED + " PLEASE ENTER A VALID CHOICE !!! " )
                    print( Style.RESET_ALL )
                    print()
                    continue

                
    elif VALUE4 ==  "1A" :
        VALUE5 = "COUPE"
        
    else :
        VALUE5 = "CHAIR"

    while True :
        
        CHOICE = input( " DO YOU WANT A MEAL OR NOT ? (Y/N);(y/n) " ).strip()
        print()
        
        if ( CHOICE in [ "Y" , "y" ] ) :
            VALUE6 = input( " PLEASE SELECT YOUR MEAL (VEG/NONVEG);(veg/nonveg) : " ).upper().strip()
            print()
            
            if VALUE6 in [ "VEG" , "NONVEG" ] :
                break
            
            else :
                print( Fore.RED + " INVALID INPUT !!! " )
                print( Fore.RED + " PLEASE ENTER A VALID CHOICE !!! " )
                print( Style.RESET_ALL )
                print()
                continue

        else :
            VALUE6 = "NO_MEAL"
            break
                
    DICT2 = { "M" : "MALE" , "F" :  "FEMALE" , "LGBT" : "LGBT" , "N" : "NOT TO MENTION" }
    
    DICT3 = { "GN" : "GENERAL QUOTA" ,"TQ" : "TATKAL QUOTA" , "PT" : "PREMIUM TATKAL QUOTA" , "LD" : "LADIES QUOTA" ,
              "SS" : "LOWER BERTH QUOTA" , "HP" : "PHYSICALLY HANDICAPPED QUOTA" , "HO" : "HEADQUARTERS/HIGH OFFICIAL QUOTA" , "YU" : "YUVA QUOTA" ,
              "PH" : "PARLIAMENT HOUSE QUOTA" , "DF" : "DEFENCE QUOTA" , "FT" : "FOREIGNER TOURIST QUOTA" , "DP" : "DUTY PASS" }
    
    DICT4 = { "EA" : "ANUBHUTI CLASS" , "1A" : "AC FIRST CLASS" , "EC" : "EXECUTIVE CHAIR CAR" , "2A" : "AC 2 TIER" , "SL" : "SLEEPER" ,
              "FC" : "FIRST CLASS" , "3A" : "AC 3 TIER" , "3E" : "AC 3 ECONOMY" , "CC" : "AC CHAIR CAR" , "2S" : "SECOND SITTING" }
    
    DICT5 = {  "LB" : "LOWER BERTH" , "MB" : "MIDDLE BERTH" , "UB" : "UPPER BERTH" , "SL" : "SIDE LOWER BERTH" , "SU" : "SIDE UPPER BERTH" , "COUPE" : "COUPE" , "CHAIR" : "CHAIR" }
    
    DICT6 = { "VEG" : "VEG MEAL" , "NONVEG" : "NONVEG MEAL" , "NO_MEAL" : "NO MEAL" }

    PASSENGER_GENDER = DICT2[VALUE2]
    
    QUOTA = DICT3[VALUE3]
    
    CLASS = DICT4[VALUE4]
    
    PREFERRED_BERTH = DICT5[VALUE5]
    
    MEAL = DICT6[VALUE6]
    
    return PASSENGER_CONTACT , PASSENGER_AGE , PASSENGER_GENDER , QUOTA , CLASS , PREFERRED_BERTH , MEAL 


def TICKET_CHECKING() :
    
    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    while True :
        try :
            CHOICE = input( " DO YOU WANT TO CONTINUE OR NOT ?  (Y/N);(y/n) " ).strip()
            print()
        
            if ( CHOICE in [ "Y" , "y" ] ) :
                RECORDS = []
                INSERT = []
                
                PNR_NUMBER = int ( eval ( input ( " PLEASE ENTER YOUR PNR NUMBER : " ) ) )
                print()
                
                SQL_QUERY_1 = " select * from RAILWAY_TICKET where USER_CONTACT = {} and PNR_NUMBER = {} ; ".format( USER_CONTACT , PNR_NUMBER )
                CURSOR.execute( SQL_QUERY_1 )
                DATA = CURSOR.fetchall()
                
                TABLE1 = prettytable.PrettyTable( ( "PNR NUMBER" , "PASSENGER NAME" , "ID TYPE" , "ID NUMBER" , "TOTAL NUMBER OF SEATS BOOKED" , "DATE GOING" , "STARTING POINT" , "ENDING POINT" , "DATE RETURN" ) )
                TABLE2 = prettytable.PrettyTable( ( "PASSENGER CONTACT" , "PASSENGER AGE" , "PASSENGER GENDER" , "QUOTA" , "CLASS" , "PREFFERED BERTH" , "MEAL" , "PASSENGER TYPE" , "USER ID CONTACT" ) )

                if ( DATA == [] ) :
                    print( Fore.RED + " SORRY NO SUCH TICKET WITH PNR NUMBER" , PNR_NUMBER , "FOUND IN YOUR ACCOUNT !!! " )
                    print( Fore.RED + " PLEASE TRY AGAIN !!! ")
                    print( Style.RESET_ALL )
                    print()
                    continue
                    
                else :
                    for INSERT in DATA :
                        TABLE1.add_row( INSERT[ 0 : 9 : 1 ] )
                        TABLE2.add_row( INSERT[ 9 : 18 : 1 ] )

                    print( TABLE1 )
                    print( TABLE2 )
                    print()
                    continue
                
            else :
                break
                        
        except :
            print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            print()
            continue



def TICKET_CANCELLING():
    
    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    while True :
        try :
            CHOICE = input( " DO YOU WANT TO CONTINUE OR NOT ?  (Y/N);(y/n) " ).strip()
            print()
            
            if ( CHOICE in [ "Y" , "y" ] ) :
                PNR_NUMBER = int ( eval ( input ( " PLEASE ENTER YOUR PNR NUMBER : " ) ) )
                print()
                CHECK = CAPTCHA()
                 
                if ( CHECK == True ) :
                 
                    CURSOR = MYCONNECTION.cursor()
                    SQL_QUERY_1 = " select * from RAILWAY_TICKET where USER_CONTACT = {} ; ".format( USER_CONTACT )
                    CURSOR.execute( SQL_QUERY_1 )
                    DATA1 = CURSOR.fetchall()
                 
                    for LOOP in range( 0 , len( DATA1 ) , 1 ) :
                        if ( PNR_NUMBER == DATA1[ LOOP ][ 0 ] ) :
                            SEAT_BOOKED = DATA1[ LOOP ][ 4 ]
                 
                            DELETE = " delete from RAILWAY_TICKET where PNR_NUMBER = {} and USER_CONTACT = {} ; ".format( PNR_NUMBER , USER_CONTACT )
                 
                            CURSOR.execute( DELETE )
                            print( Fore.RED + " YOUR TICKET IS BEEN CANCELLED !!! " )
                            print( Style.RESET_ALL )
                            print()
                 
                            FILE_HANDLE = open( r"C:\Users\dell\Desktop\TIMELINES\USER_TICKET_TIMELINE.txt" , "a" )
            
                            TIME_USER_TICKET = datetime.datetime.today()
                            USER_TICKET_TIMELINE_LIST = [ str( USER_CONTACT ) , "\t" , "TICKET_CANCELLING" , "\t" , str( SEAT_BOOKED ) , "\t" , str( PNR_NUMBER ) , "\t" , str( TIME_USER_TICKET ) , "\n" ]

                            FILE_HANDLE.writelines( USER_TICKET_TIMELINE_LIST )

                            FILE_HANDLE.close()
                            return True
                        
                        else :
                            print( Fore.RED + " SORRY, NO SUCH TICKET WITH PNR NUMBER" , PNR_NUMBER , "FOUND !!! " )
                            print( Fore.RED + " PLEASE TRY AGAIN !!! ")
                            print( Style.RESET_ALL )
                            print()
                            return False
                        
                else :
                    continue
                
            else :
                return False
                        
        except :
            print( Fore.RED + " INVALID PNR NUMBER !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            print()
            continue

        
    
def USER_ACCOUNT_DETAILS() :
    
    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    while True :
        
        try :
            CHOICE = input( " DO YOU WANT TO REVIEW YOUR ACCOUNT OR NOT ?  (Y/N);(y/n) " ).strip()
            print()
            
            if ( CHOICE in [ "Y" , "y" ] ) :
                
                USERNAME = input( " PLEASE ENTER YOUR USERNAME : " ).strip()
                print()
                
                PASSWORD = input( " PLEASE ENTER YOUR PASSWORD : " ).strip()
                print()
                
                SQL_QUERY_1 = " select * from USER_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
                CURSOR.execute( SQL_QUERY_1 )
                DATA = CURSOR.fetchall()
                
                if ( PASSWORD == DATA[ 0 ][ 1 ] ) :
                    LIST1 = [ " USERNAME " , " PASSWORD " , " NAME " , " CONTACT " , " GENDER " , " DATE OF BIRTH " ]
                    PASSWORD_SHOWN = (( len( PASSWORD ) - 3 ) * "*" + PASSWORD[ len( PASSWORD ) - 3 : : ] )
                 
                    print( LIST1[ 0 ] , ":" , DATA[ 0 ][ 0 ] )
                    
                    print()

                    print( LIST1[ 1 ] , ":" , PASSWORD_SHOWN )

                    print()

                    print( LIST1[ 2 ] , ":" , DATA[ 0 ][ 2 ] )

                    print()

                    print( LIST1[ 3 ] , ":" , DATA[ 0 ][ 3 ] )

                    print()

                    print( LIST1[ 4 ] , ":" , DATA[ 0 ][ 4 ] )

                    print()

                    print( LIST1[ 5 ] , ":" , DATA[ 0 ][ 5 ] )

                    print()

                    break
                
                else :
                    print( Fore.RED + " SORRY, WRONG PASSWORD !!! " )
                    print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                    print( Style.RESET_ALL )
                    print()
                    break

            else :
                break
                        
        except :
            print( Fore.RED + " INVALID USERNAME !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            print()
            continue


def USER_MODIFY_ACCOUNT() :
    
    import mysql.connector as MS
    MYCONNECTION  = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True

    while True :
        FLAG = 0
        
        try :
            CHOICE1 = input( " DO YOU WANT TO CONTINUE OR NOT ?  (Y/N);(y/n) " ).strip()
            print()
            
            if ( CHOICE1 in [ "Y" , "y" ] ) :

                USERNAME = input( " PLEASE ENTER YOUR USERNAME : " ).strip()
                print()
                
                PASSWORD = input( " PLEASE ENTER YOUR PASSWORD : " ).strip()
                print()
                
                SQL_QUERY_1 = " select * from USER_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
                CURSOR.execute( SQL_QUERY_1 )
                DATA = CURSOR.fetchall()
                print()
                
                if ( PASSWORD == DATA[ 0 ][ 1 ] ) :
                    
                    print( " 1. NAME \n" )

                    print( " 2. PASSWORD \n" )

                    print( " 3. CONTACT \n" )

                    print( " 4. DATE OF BIRTH \n" )

                    print( " 5. GENDER \n" )

                    print()
                     
                    CHOICE2 = int ( eval ( input ( " PLEASE ENTER THE CHOICE YOU WANT TO EDIT : " ) ) )
                    print()
                     
                    if ( CHOICE2 == 1 ) :

                        NEW_FIRST_NAME = input( " PLEASE ENTER YOUR FIRST NAME WANTED TO UPDATE : " ).upper().strip()
                        print()
                        
                        NEW_MIDDLE_NAME = input( " PLEASE ENTER YOUR MIDDLE NAME ( IF NOT PRESS ENTER ) WANTED TO UPDATE : " ).upper().strip()
                        print()
                        
                        NEW_LAST_NAME = input( " PLEASE ENTER YOUR LAST NAME WANTED TO UPDATE : " ).upper().strip()
                        print()
                        
                        if ( NEW_MIDDLE_NAME == "" ) :
                            NEW_NAME = NEW_FIRST_NAME + " " + NEW_LAST_NAME
                            
                        else :
                            NEW_NAME = NEW_FIRST_NAME + " " + NEW_MIDDLE_NAME + " " + NEW_LAST_NAME
                            
                        SQL_QUERY_2 = " update USER_ACCOUNTS set NAME = '{}' where USER_CONTACT = {} ; ".format( NEW_NAME , USER_CONTACT )
                        CURSOR.execute( SQL_QUERY_2 )
                        
                        print( Fore.RED + " YOUR ACCOUNT IS UPDATED !!! " )
                        print( Style.RESET_ALL )
                        print()
                        
                        USER_ACCOUNT_DETAILS()
                        FLAG = 1
                            
                    elif ( CHOICE2 == 2 ) :

                        NEW_PASSWORD = PASSWORD_CREATION( USERNAME )
                        
                        SQL_QUERY_2 = " update USER_ACCOUNTS set PASSWORD = '{}' where USER_CONTACT = {} ; ".format( NEW_PASSWORD , USER_CONTACT )
                        CURSOR.execute( SQL_QUERY_2 )
                        
                        print( Fore.RED + " YOUR ACCOUNT IS UPDATED !!! " )
                        print( Style.RESET_ALL )
                        print()
                        
                        USER_ACCOUNT_DETAILS()
                        FLAG = 1

                    elif ( CHOICE2 == 3 ) :
                        
                        while True :
                            try :
                                print( Fore.GREEN + Style.BRIGHT + " PLEASE AVOID USING '0' OR '+' SIGN BEFORE USER'S CONTACT !!! " )
                                print( Style.RESET_ALL )
                                print()
                                
                                NEW_CONTACT = int ( eval ( input ( " PLEASE ENTER YOUR NEW CONTACT : " ) ) )
                                print()
                                CHECKING = str( NEW_CONTACT )
                
                                if  ( 7 <= len( CHECKING ) <= 13 ) :
                                    try :
                                        SQL_QUERY_2 = " update USER_ACCOUNTS set USER_CONTACT = {} where USER_CONTACT = {} ; ".format( NEW_CONTACT , USER_CONTACT )
                                        CURSOR.execute( SQL_QUERY_2 )
                                        
                                        print( Fore.RED + " YOUR ACCOUNT IS UPDATED !!! " )
                                        print( Style.RESET_ALL )
                                        print()
                                        
                                        USER_ACCOUNT_DETAILS()
                                        FLAG = 1
                                        break
                                   
                                    except :
                                        print( Fore.RED + " THIS CONTACT ALREADY EXISTS WITH ANOTHER USERNAME REGISTERED ON IT !!! " )
                                        print( Fore.RED + " HENCE, PLEASE TRY AGAIN !!! " )
                                        print( Fore.RED + " FOR ANY FURTHER QUERIES PLEASE CONTACT ADMINISTRATOR AT !!! " )
                                        print( Fore.RED + " GMAIL : INDIANRAILWAYS@GMAIL.COM " )
                                        print( Fore.RED + " CONTACT : 9876543210 " )
                                        print( Style.RESET_ALL )
                                        print()
                                        continue
                                    
                                else :
                                    print( Fore.RED + " INVALID CONTACT NUMBER !!! " )
                                    print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                                    print( Style.RESET_ALL )
                                    print()
                                    continue

                            except :
                                print( Fore.RED + " INVALID CONTACT NUMBER !!! " )
                                print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
                                print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                                print( Style.RESET_ALL )
                                print()
                                continue
                                
                    elif ( CHOICE2 == 4 ) :

                        while True :
                            try :
                                print( " PLEASE ENTER YOUR DATE OF BIRTH IN THE FOLLOWING FORMAT " )
                                print()
                                
                                DAY = int ( eval ( input ( " PLEASE ENTER DATE (dd) : " ) ) )
                                
                                MONTH = int ( eval ( input ( " PLEASE ENTER MONTH (mm) : " ) ) )
                                
                                YEAR = int ( eval ( input ( " PLEASE ENTER YEAR (yyyy) : " ) ) )

                                print()
                                
                                NEW_DATE_OF_BIRTH = datetime.date( YEAR , MONTH , DAY )
                                CURRENT_DATE = datetime.date.today()
                                DIFFERENCE1 = str( CURRENT_DATE - NEW_DATE_OF_BIRTH )
                                DIFFERENCE2 = DIFFERENCE1[ -14 : : -1 ] 
                                DIFFERENCE3 = int( DIFFERENCE2[ -1 : : -1 ] )
                                
                                if ( DIFFERENCE3 >= 3650 ) :
                                    SQL_QUERY_2 = " update USER_ACCOUNTS set DATE_OF_BIRTH = '{}' where USER_CONTACT = {} ; ".format( NEW_DATE_OF_BIRTH , USER_CONTACT )
                                    CURSOR.execute( SQL_QUERY_2 )
                                    
                                    print( Fore.RED + " YOUR ACCOUNT IS UPDATED !!! " )
                                    print( Style.RESET_ALL )
                                    print()
                                    
                                    USER_ACCOUNT_DETAILS()
                                    FLAG = 1
                                    break
                                
                                else :
                                    print( Fore.RED + " MINIMUM AGE REQUIRED TO SIGN UP IS 10 YEARS !!! " )
                                    print( Style.RESET_ALL )
                                    print()
                                    continue
                                
                            except :
                                print( Fore.RED + " INVALID DATE OF BIRTH !!! " )
                                print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                                print( Style.RESET_ALL )
                                print()
                                continue

                    elif ( CHOICE2 == 5 ) :
                        while True :
                            print( " M = MALE " , "\n " , " F = FEMALE " , "\n" , " LGBT = LESBIAN, GAY, BISEXUAL, TRANSGENDER " , "\n" , " N = NOT TO MENTION " )
                            print()
                            
                            VALUE = input( " PLEASE ENTER YOUR NEW GENDER : " ).upper().strip()
                            print()
                            
                            if ( VALUE in [ "M" , "F" , "LGBT" , "N" ] ) :
                                break
                
                            else :
                                print( Fore.RED + " INVALID INPUT !!! " )
                                print( Fore.RED + " PLEASE ENTER A VALID CHOICE !!! " )
                                print( Style.RESET_ALL )
                                print()
                                continue

                        DICT = { "M" : "MALE" , "F" :  "FEMALE" , "LGBT" : "LGBT" , "N" : "NOT TO MENTION" }
                        NEW_GENDER = DICT[ VALUE ]
                        
                        SQL_QUERY_2 = " update USER_ACCOUNTS set GENDER = '{}' where USER_CONTACT = {} ; ".format( NEW_GENDER , USER_CONTACT )
                        CURSOR.execute( SQL_QUERY_2 )
                        
                        print( Fore.RED + " YOUR ACCOUNT IS UPDATED !!! " )
                        print( Style.RESET_ALL )
                        print()
                        
                        USER_ACCOUNT_DETAILS()
                        FLAG = 1
                        continue

                    else :
                        print( Fore.RED + " PLEASE ENTER A VALID OPTION !!! " )
                        print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                        print( Style.RESET_ALL )
                        print()
                        continue
                    

                if ( FLAG == 1 ) :

                    SQL_QUERY_3 = " select EMAIL_ACCOUNT from USER_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
                    CURSOR.execute( SQL_QUERY_3 )
                    DATA = CURSOR.fetchall()
                    EMAIL = DATA[ 0 ][ 0 ]
                    
                    SERVER = smtplib.SMTP_SSL( "smtp.gmail.com" , 465 )
                    SERVER.login( "railwaysofindia.1853@gmail.com" , "JaiHind@Indian" )
                    SERVER.sendmail( "railwaysofindia.1853@gmail.com" , EMAIL , " YOUR ACCOUNT HAS BEEN SUCCESSFULLY MODIFIED i.e. WITH USERNAME " + USERNAME + " AND PASSWORD " + PASSWORD + " !!! " )
                    SERVER.quit()

                    FILE_HANDLE = open( r"C:\Users\dell\Desktop\TIMELINES\USER_ACCOUNT_TIMELINE.dat" , "ab" )

                    TIME_USER_ACCOUNT = datetime.datetime.today()
                    USER_TIMELINE_LIST = [ USERNAME , str( USER_CONTACT ) , "ACCOUNT_MODIFCATION" , str( TIME_USER_ACCOUNT ) ]
                    
                    pickle.dump( USER_TIMELINE_LIST , FILE_HANDLE )

                    FILE_HANDLE.close()
                    continue

                else :
                    continue
                

        except :
              print( Fore.RED + " INVALID INPUT !!! " )
              print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
              print( Fore.RED + " PLEASE TRY AGAIN !!! " )
              print( Style.RESET_ALL )
              print()

            
    
def USER_DELETE_ACCOUNT() :
    
    import mysql.connector as MS
    MYCONNECTION  = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    for ATTEMPTS in range( 0 , 4 , 1 ) :
        FLAG1 = 0
        DATA = []
        USERNAME = input( " PLEASE ENTER YOUR USERNAME : " ).strip()
        print()

        SQL_QUERY_1 = " select * from USER_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
        CURSOR.execute( SQL_QUERY_1 )
        DATA = CURSOR.fetchall()
        
        if ( DATA == [] ) :
            print( Fore.RED + " ACCOUNT DOES NOT EXISTS !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            print()
            FLAG1 = -1
            continue
            
        else :
            PASSWORD = input( " PLEASE ENTER YOUR PASSWORD : " ).strip()
            print()
            
            if ( PASSWORD == DATA[ 0 ][ 1 ] ) :
                print( GREETINGS() , DATA[ 0 ][ 2 ] )
                
                LIST = [ " USERNAME  " , " PASSWORD " , " NAME " , " CONTACT " , " GENDER " , " DATE_OF_BIRTH " ]
                PASSWORD_SHOWN = (( len( PASSWORD ) - 3 ) * "*" + PASSWORD[ len( PASSWORD ) - 3 : : ] )
                
                print( LIST[ 0 ] , ":" , DATA[ 0 ][ 0 ] )
                
                print()
                
                print( LIST[ 1 ] , ":" , PASSWORD_SHOWN )

                print()
                
                print( LIST[ 2 ] , ":" , DATA[ 0 ][ 2 ] )

                print()

                print( LIST[ 3 ] , ":" , DATA[ 0 ][ 3 ] )

                print()
                
                print( LIST[ 4 ] , ":" , DATA[ 0 ][ 4 ] )

                print()
                
                print( LIST[ 5 ] , ":" , DATA[ 0 ][ 5 ] )
                print()
                print()
                    
                CHOICE = input( " IS THIS YOUR ACCOUNT (Y/N);(y/n) : " ).strip()
                print()
                
                if ( CHOICE in [ "Y" , "y" ] ) :
                    CHECK = CAPTCHA()
                    
                    if ( CHECK == True ) :
                        SQL_QUERY_2 = " delete from USER_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
                        CURSOR.execute( SQL_QUERY_2 )
                        FLAG = 1
                        break
                    
                    else :
                        FLAG = 0
                        break
                    
                else :
                    FLAG = 0
                    break
                            
            else :
                print( Fore.RED + " WRONG PASSWORD !!! " )
                print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                print( Style.RESET_ALL )
                print()
                FLAG1 = -1
                continue   
                    
    if ( FLAG == -1 ) :
        print( Fore.RED + " YOU HAVE EXCEDEED THE MAXIMUM NUMBER OF YOUR TRIALS !!! " )
        print( Fore.RED + " PLEASE TRY AGAIN AFTER 1 HOUR !!! " )
        print( Style.RESET_ALL )
        print()

    elif ( FLAG == 1 ) :

        SQL_QUERY_3 = " select EMAIL_ACCOUNT from USER_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
        CURSOR.execute( SQL_QUERY_3 )
        DATA = CURSOR.fetchall()
        EMAIL = DATA[ 0 ][ 0 ]
        
        SERVER = smtplib.SMTP_SSL( "smtp.gmail.com" , 465 )
        SERVER.login( "railwaysofindia.1853@gmail.com" , "JaiHind@Indian" )
        SERVER.sendmail( "railwaysofindia.1853@gmail.com" , EMAIL , " YOUR ACCOUNT HAS BEEN SUCCESSFULLY DELETED i.e. WITH USERNAME " + USERNAME + " AND PASSWORD " + PASSWORD + " !!! " )
        SERVER.quit()


        FILE_HANDLE = open( r"C:\Users\dell\Desktop\TIMELINES\USER_ACCOUNT_TIMELINE.dat" , "ab" )

        TIME_USER_ACCOUNT = datetime.datetime.today()
        USER_TIMELINE_LIST = [ USERNAME , str( USER_CONTACT ) , "ACCOUNT_DELETION" , str( TIME_USER_ACCOUNT ) ]

        pickle.dump( USER_TIMELINE_LIST , FILE_HANDLE )

        FILE_HANDLE.close()

        print( " YOUR ACCOUNT WAS SUCCESSFULLY DELETED !!! " )
        print( " WE ARE SAD SEEING YOU GO !!! " )
        print( " SEE YOU SOON AGAIN !!! " )
        print()
        
    else :
        print( Fore.RED + " YOU EITHER ENTERED WRONG CAPTCHA OR SELECTED NO FOR DELETION OF ACCOUNT !!! " )
        print( Style.RESET_ALL )
        print()
           

def MAIN_PROGRAM_ADMIN() :
    
    while True :
        try :
            print()
            print( Fore.CYAN )
            
            print( " 1. SHOW ALL DATA " , "\n" , " 2. SHOW PARTICULAR DATA " , "\n" , " 3. ACCOUNT DETAILS " , "\n" , " 4. MODIFY ACCOUNT " , "\n" , " 5. DELETE ACCOUNT " )        
            print( " 6. PRINT PARTICULAR TICKET " , "\n" , " 7. PRINT ALL DATA " , "\n" , " 8. LOG OUT " )
            
            print( Style.RESET_ALL )
            print()
            
            CHOICE = int ( eval ( input( " PLEASE ENTER YOUR CHOICE : " )))
            print( ansi.clear_screen() )
            print()
            print()
            
            if ( CHOICE == 1 ) :
                SHOW_ALL_TICKET()
                continue
            
            elif ( CHOICE == 2 ) :
                SHOW_PARTICULAR_TICKET()
                continue
            
            elif ( CHOICE == 3 ) :
                ADMIN_ACCOUNT_DETAILS()
                continue
            
            elif ( CHOICE == 4 ) :
                ADMIN_MODIFY_ACCOUNT()
                continue

            elif ( CHOICE == 5 ) :
                ADMIN_DELETE_ACCOUNT()
                continue

            elif ( CHOICE == 6 ) :
                PRINT_PARTICULAR_TICKET()
                continue

            elif ( CHOICE == 7 ) :
                PRINT_ALL_TICKET()
                continue

            elif ( CHOICE == 8 ) :
                print( " THANK YOU !!! " )
                break
            
            else:
                print( Fore.RED + " INVALID INPUT !!! " )
                print( Fore.RED + " PLEASE ENTER A VALID CHOICE !!! " )
                print( Style.RESET_ALL )
                continue
        
        except :
            print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            continue



def SHOW_ALL_TICKET() :

    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    while True :
        CHOICE = input( " DO YOU WANT TO CONTINUE OR NOT ?  (Y/N);(y/n) " ).strip()
        print()
        
        if ( CHOICE in [ "Y" , "y" ] ) :
            SQL_QUERY = " select * from RAILWAY_TICKET ; "
            CURSOR.execute( SQL_QUERY )
            DATA = CURSOR.fetchall()

            if ( DATA == [] ) :
               print( Fore.RED + " NO DATA EXISTS !!! " )
               print( Style.RESET_ALL )
               print()
               break

            else :
                TABLE1 = prettytable.PrettyTable( [ " PNR NUMBER " , " PASSENGER NAME " , " ID TYPE " , " ID NUMBER " , " TOTAL NUMBER OF SEATS BOOKED " , " DATE GOING " , " STARTING POINT " , " ENDING POINT " , " DATE RETURN " ] )
                TABLE2 = prettytable.PrettyTable( [ " PASSENGER CONTACT " , " PASSENGER AGE " , " PASSENGER GENDER " , " QUOTA " , " CLASS " , " PREFFERED BERTH " , " MEAL " , " PASSENGER TYPE " , " USER ID CONTACT " ] )

                for INSERT in DATA :
                    
                    TABLE1.add_row( INSERT[ 0 : 9 : 1 ] )
                    TABLE2.add_row( INSERT[ 9 : 18 : 1 ] )

                print( TABLE1 )
                print( TABLE2 )
                print()
            
        else :
            break
                    
       
def SHOW_PARTICULAR_TICKET() :

    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    while True :
        try : 
        
            CHOICE1 = input( " DO YOU WANT TO CONTINUE OR NOT ?  (Y/N);(y/n) " )
            print()
            
            if ( CHOICE1 in [ "Y" , "y" ] ) :
                print( " 1. CONTACT \n" )
                print( " 2. PNR NUMBER \n" )
                print()
                
                CHOICE2 = int( eval ( input ( " PLEASE SELECT THE OPTIONS BY WHICH YOU WANT TO SEARCH : " ) ) )
                print()
                
                if ( CHOICE2 == 1 ) :
                    print( Fore.GREEN + Style.BRIGHT + " PLEASE AVOID USING '0' OR '+' SIGN BEFORE PASSENGER'S CONTACT !!! " )
                    print( Style.RESET_ALL )
                    print()
                    
                    CONTACT = int ( eval ( input ( " PLEASE ENTER USER'S CONTACT : " ) ) )
                    print()
                    SQL_QUERY_1 = " select * from RAILWAY_TICKET where USER_CONTACT = {} ; ".format( CONTACT )
                 
                elif ( CHOICE2 == 2 ) :
                    PNR_NUMBER = int ( eval ( input ( " PLEASE ENTER PASSENGER'S PNR NUMBER : " ) ) )
                    print()
                    SQL_QUERY_1 = " select * from RAILWAY_TICKET where PNR_NUMBER = {} ; ".format( PNR_NUMBER )
                    
                else :
                    print( Fore.RED + " PLEASE ENTER A VALID OPTION " )
                    print( Fore.RED + " PLEASE TRY AGAIN  !!! " )
                    print( Style.RESET_ALL )
                    print()
                    continue
                
                CURSOR.execute( SQL_QUERY_1 )
                DATA = CURSOR.fetchall()
                
                if ( DATA == [] ) :
                   print( Fore.RED + " NO DATA FOUND !!! " )
                   print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                   print( Style.RESET_ALL )
                   print()
                   continue
                
                else :
                    TABLE1 = prettytable.PrettyTable( [ " PNR NUMBER " , " PASSENGER NAME " , " ID TYPE " , " ID NUMBER " , " TOTAL NUMBER OF SEATS BOOKED " , " DATE GOING " , " STARTING POINT " , " ENDING POINT " , " DATE RETURN " ] )
                    TABLE2 = prettytable.PrettyTable( [ " PASSENGER CONTACT " , " PASSENGER AGE " , " PASSENGER GENDER " , " QUOTA " , " CLASS " , " PREFFERED BERTH " , " MEAL " , " PASSENGER TYPE " , " USER ID CONTACT " ] )

                    for INSERT in DATA :
                        TABLE1.add_row( INSERT[ 0 : 9 : 1 ] )
                        TABLE2.add_row( INSERT[ 9 : 18 : 1 ] )
                        continue
                    
                    print( TABLE1 )
                    print( TABLE2 )
                    print()
                    
            else :
                break
                
        except :
                print( Fore.RED + " PLEASE ENTER A NUMERIC VALUE !!! " )
                print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                print( Style.RESET_ALL )
                print()
                continue

                        

def ADMIN_ACCOUNT_DETAILS() :

    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    while True :
        
        try :
            CHOICE = input( " DO YOU WANT TO REVIEW YOUR ACCOUNT ?  (Y/N);(y/n) " )
            print()
            
            if ( CHOICE in [ "Y" , "y" ] ) :
                USERNAME = input( " PLEASE ENTER YOUR USERNAME : " ).strip()
                print()
                
                PASSWORD = input( " PLEASE ENTER YOUR PASSWORD : " ).strip()
                print()
                
                SQL_QUERY_1 = " select * from ADMIN_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
                CURSOR.execute( SQL_QUERY_1 )
                DATA = CURSOR.fetchall()
                
                if ( PASSWORD == DATA[0][1] ) :
                    LIST1 = [ " USER_NAME " , " PASSWORD " , " NAME " , " CONTACT " , " GENDER " , " DATE OF BIRTH " ]
                    PASSWORD_SHOWN = (( len( PASSWORD ) - 3 ) * "*" + PASSWORD[ len( PASSWORD ) - 3 : : ] )
                    
                    print( LIST1[ 0 ] , ":" , DATA[ 0 ][ 0 ] )

                    print()
                    
                    print( LIST1[ 1 ] , ":" , PASSWORD_SHOWN )

                    print()
                    
                    print( LIST1[ 2 ] , ":" , DATA[ 0 ][ 2 ] )

                    print()
                    
                    print( LIST1[ 3 ] , ":" , DATA[ 0 ][ 3 ] )

                    print()
                    
                    print( LIST1[ 4 ] , ":" , DATA[ 0 ][ 4 ] )

                    print()
                    
                    print( LIST1[ 5 ] , ":" , DATA[ 0 ][ 5 ] )
                    
                    print()
                    print()
                    break
                
                else :
                    print( Fore.RED + " SORRY, WRONG PASSWORD !!! " )
                    print( Fore.RED + " PLEASE TRY AGAIN !!! ")
                    print( Style.RESET_ALL )
                    print()
                    break

            else :
                break
                        
        except :
            print( Fore.RED + " INVALID USERNAME !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            print()
            continue



def ADMIN_MODIFY_ACCOUNT() :

    import mysql.connector as MS
    MYCONNECTION  = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True

    while True :
        FLAG = 0
        
        try :
            CHOICE1 = input( " DO YOU WANT TO CONTINUE OR NOT ?  (Y/N);(y/n) " )
            print()
            
            if ( CHOICE1 in [ "Y" , "y" ] ) :

                USERNAME = input( " PLEASE ENTER YOUR USERNAME : " )
                print()
                
                PASSWORD = input( " PLEASE ENTER YOUR PASSWORD : " )
                print()
                
                SQL_QUERY_1 = " select * from ADMIN_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
                CURSOR.execute( SQL_QUERY_1 )
                DATA = CURSOR.fetchall()
                print()
                
                if ( PASSWORD == DATA[ 0 ][ 1 ] ) :
                    
                    print( " 1. NAME \n" )

                    print( " 2. PASSWORD \n" )

                    print( " 3. CONTACT \n" )

                    print( " 4. DATE OF BIRTH \n" )

                    print( " 5. GENDER \n" )

                    print()
                     
                    CHOICE2 = int ( eval ( input ( " PLEASE ENTER THE CHOICE YOU WANT TO EDIT : " ) ) )
                    print()
                     
                    if ( CHOICE2 == 1 ) :

                        NEW_FIRST_NAME = input( " PLEASE ENTER YOUR FIRST NAME WANTED TO UPDATE : " ).upper().strip()
                        print()
                        
                        NEW_MIDDLE_NAME = input( " PLEASE ENTER YOUR MIDDLE NAME ( IF NOT PRESS ENTER ) WANTED TO UPDATE : " ).upper().strip()
                        print()
                        
                        NEW_LAST_NAME = input( " PLEASE ENTER YOUR LAST NAME WANTED TO UPDATE : " ).upper().strip()
                        print()
                        
                        
                        if ( NEW_MIDDLE_NAME == "" ) :
                            NEW_NAME = NEW_FIRST_NAME + " " + NEW_LAST_NAME
                            
                        else :
                            NEW_NAME = NEW_FIRST_NAME + " " + NEW_MIDDLE_NAME + " " + NEW_LAST_NAME
                            
                        SQL_QUERY_2 = " update ADMIN_ACCOUNTS set NAME = '{}' where ADMIN_CONTACT = {} ; ".format( NEW_NAME , ADMIN_CONTACT )
                        CURSOR.execute( SQL_QUERY_2 )
                        
                        print( Fore.RED + " YOUR ACCOUNT IS UPDATED !!! " )
                        print( Style.RESET_ALL )
                        print()
                        
                        ADMIN_ACCOUNT_DETAILS()
                        FLAG = 1
                            
                    elif ( CHOICE2 == 2 ) :

                        NEW_PASSWORD = PASSWORD_CREATION( USERNAME )
                        
                        SQL_QUERY_2 = " update ADMIN_ACCOUNTS set PASSWORD = '{}' where ADMIN_CONTACT = {} ; ".format( NEW_PASSWORD , ADMIN_CONTACT )
                        CURSOR.execute( SQL_QUERY_2 )
                        
                        print( Fore.RED + " YOUR ACCOUNT IS UPDATED !!! " )
                        print( Style.RESET_ALL )
                        print()
                        
                        ADMIN_ACCOUNT_DETAILS()
                        FLAG = 1

                    elif ( CHOICE2 == 3 ) :
                        
                        while True :
                            try :
                                print( Fore.RED + " PLEASE AVOID USING '0' OR '+' SIGN BEFORE ADMIN'S CONTACT !!! " )
                                print( Style.RESET_ALL )
                                print()
                                
                                NEW_CONTACT = int ( eval ( input ( " PLEASE ENTER YOUR NEW CONTACT : " ) ) )
                                print()
                                CHECKING = str( NEW_CONTACT )
                
                                if  ( 7 <= len( CHECKING ) <= 13 ) :
                                    try :
                                        SQL_QUERY_2 = " update ADMIN_ACCOUNTS set ADMIN_CONTACT = {} where ADMIN_CONTACT = {} ; ".format( NEW_CONTACT , ADMIN_CONTACT )
                                        CURSOR.execute( SQL_QUERY_2 )
                                        
                                        print( Fore.RED + " YOUR ACCOUNT IS UPDATED !!! " )
                                        print( Style.RESET_ALL )
                                        print()
                                        
                                        ADMIN_ACCOUNT_DETAILS()
                                        FLAG = 1
                                        break
                                   
                                    except :
                                        print( Fore.RED + " THIS CONTACT ALREADY EXISTS WITH ANOTHER USERNAME REGISTERED ON IT !!! " )
                                        print( Fore.RED + " HENCE, PLEASE TRY AGAIN !!! " )
                                        print( Fore.RED + " FOR ANY FURTHER QUERIES PLEASE CONTACT ADMINISTRATOR AT !!! " )
                                        print( Fore.RED + " GMAIL : INDIANRAILWAYS@GMAIL.COM " )
                                        print( Fore.RED + " CONTACT : 9876543210 " )
                                        print( Style.RESET_ALL )
                                        print()
                                        continue
                                    
                                else :
                                    print( Fore.RED + " INVALID CONTACT NUMBER !!! " )
                                    print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                                    print( Style.RESET_ALL )
                                    print()
                                    continue

                            except :
                                print( Fore.RED + " INVALID CONTACT NUMBER !!! " )
                                print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
                                print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                                print( Style.RESET_ALL )
                                print()
                                continue
                                
                    elif ( CHOICE2 == 4 ) :

                        while True :
                            try :
                                print( " PLEASE ENTER YOUR DATE OF BIRTH IN THE FOLLOWING FORMAT " )
                                print()
                                
                                DAY = int ( eval ( input ( " PLEASE ENTER DATE (dd) : " ) ) )
                                print()
                                
                                MONTH = int ( eval ( input ( " PLEASE ENTER MONTH (mm) : " ) ) )
                                print()
                                
                                YEAR = int ( eval ( input ( " PLEASE ENTER YEAR (yyyy) : " ) ) )
                                print()
                                
                                NEW_DATE_OF_BIRTH = datetime.date( YEAR , MONTH , DAY )
                                CURRENT_DATE = datetime.date.today()
                                DIFFERENCE1 = str( CURRENT_DATE - NEW_DATE_OF_BIRTH )
                                DIFFERENCE2 = DIFFERENCE1[ -14 : : -1 ] 
                                DIFFERENCE3 = int( DIFFERENCE2[ -1 : : -1 ] )
                                
                                if ( DIFFERENCE3 >= 7670 ) :
                                    SQL_QUERY_2 = " update ADMIN_ACCOUNTS set DATE_OF_BIRTH = '{}' where ADMIN_CONTACT = {} ; ".format( NEW_DATE_OF_BIRTH , ADMIN_CONTACT )
                                    CURSOR.execute( SQL_QUERY_2 )
                                    
                                    print( Fore.RED + " YOUR ACCOUNT IS UPDATED !!! " )
                                    print( Style.RESET_ALL )
                                    print()
                                    
                                    ADMIN_ACCOUNT_DETAILS()
                                    FLAG = 1
                                    break
                                
                                else :
                                    print( Fore.RED + " MINIMUM AGE REQUIRED TO SIGN UP IS 21 YEARS !!! " )
                                    print( Style.RESET_ALL )
                                    print()
                                    continue
                                
                            except :
                                print( Fore.RED + " INVALID DATE OF BIRTH !!! " )
                                print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                                print( Style.RESET_ALL )
                                print()
                                continue

                    elif ( CHOICE2 == 5 ) :
                        while True :
                            print( " M = MALE " , " \n " , "F = FEMALE " , " \n " ,"LGBT = LESBIAN, GAY, BISEXUAL, TRANSGENDER " , " \n " , "N = NOT TO MENTION " )
                            print()
                            
                            VALUE = input( " PLEASE ENTER YOUR NEW GENDER : " ).upper().strip()
                            print()
                            
                            if ( VALUE in [ "M" , "F" , "LGBT" , "N" ] ) :
                                break
                
                            else :
                                print( Fore.RED + " INVALID INPUT !!! " )
                                print( Fore.RED + " PLEASE ENTER A VALID CHOICE !!! " )
                                print( Style.RESET_ALL )
                                print()
                                continue

                        DICT = { "M" : "MALE" , "F" :  "FEMALE" , "LGBT" : "LGBT" , "N" : "NOT TO MENTION" }
                        NEW_GENDER = DICT[ VALUE ]
                        
                        SQL_QUERY_2 = " update ADMIN_ACCOUNTS set GENDER = '{}' where ADMIN_CONTACT = {} ; ".format( NEW_GENDER , ADMIN_CONTACT )
                        CURSOR.execute( SQL_QUERY_2 )
                        
                        print( Fore.RED + " YOUR ACCOUNT IS UPDATED !!! " )
                        print( Style.RESET_ALL )
                        print()
                        
                        ADMIN_ACCOUNT_DETAILS()
                        FLAG = 1
                        continue

                    else :
                        print( Fore.RED + " PLEASE ENTER A VALID OPTION !!! " )
                        print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                        print( Style.RESET_ALL )
                        print()
                        continue
                    

                if ( FLAG == 1 ) :
                        
                    FILE_HANDLE = open( r"C:\Users\dell\Desktop\TIMELINES\ADMIN_ACCOUNT_TIMELINE.dat" , "ab" )

                    TIME_ADMIN_ACCOUNT = datetime.datetime.today()
                    ADMIN_TIMELINE_LIST = [ USERNAME , str( ADMIN_CONTACT ) , "ACCOUNT_MODIFCATION" , str( TIME_ADMIN_ACCOUNT ) ]

                    pickle.dump( ADMIN_TIMELINE_LIST , FILE_HANDLE )

                    FILE_HANDLE.close()

                    continue

                else :
                    continue

            else :
                break
                

        except :
              print( Fore.RED + " INVALID INPUT !!! " )
              print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
              print( Fore.RED + " PLEASE TRY AGAIN !!! " )
              print( Style.RESET_ALL )
              print()
        
 
    
def PRINT_PARTICULAR_TICKET() :
    
    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    while True :
        
        CHOICE1 = input( " DO YOU WANT TO CONTINUE OR NOT ?  (Y/N);(y/n) " ).strip()
        print()
        
        if ( CHOICE1 in [ "Y" , "y" ] ) :
            print( " 1. CONTACT \n" )
            print( " 2. PNR NUMBER \n" )
            print()
            
            CHOICE2 = int( eval ( input ( " PLEASE SELECT THE OPTIONS BY WHICH YOU WANT TO SEARCH : " ) ) )
            print()
             
            try : 
                if ( CHOICE2 == 1 ) :
                    print( Fore.GREEN + Style.BRIGHT + " PLEASE AVOID USING '0' OR '+' SIGN BEFORE USER'S CONTACT !!! " )
                    print( Style.RESET_ALL )
                    print()
                    
                    CONTACT = int ( eval ( input ( " PLEASE ENTER USER'S CONTACT : " ) ) )
                    print()
                    
                    SQL_QUERY_1 = " select * from RAILWAY_TICKET where USER_CONTACT = {} ; ".format( CONTACT )
                 
                elif ( CHOICE2 == 2 ) :
                    PNR_NUMBER = int ( eval ( input ( " PLEASE ENTER USER'S PNR NUMBER : " ) ) )
                    print()
                    SQL_QUERY_1 = " select * from RAILWAY_TICKET where PNR_NUMBER = {} ; ".format( PNR_NUMBER )
                    
                else :
                    print( Fore.RED + " PLEASE ENTER A VALID OPTION !!! " )
                    print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                    print( Style.RESET_ALL )
                    print()
                    continue
                
            except :
                print( Fore.RED + " PLEASE ENTER A NUMERIC VALUE !!! " )
                print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                print( Style.RESET_ALL )
                print()
                continue
                
                
            CURSOR.execute( SQL_QUERY_1 )
            DATA = CURSOR.fetchall()
            
            if ( DATA == [] ) :
               print( Fore.RED + " NO DATA FOUND !!! " )
               print( Fore.RED + " PLEASE TRY AGAIN !!! " )
               print( Style.RESET_ALL )
               print()
               continue
            
            else :
                print( Fore.RED + " PLEASE ENTER THE NAME OF CSV FILE IN WHICH YOUR DATA WOULD BE PRINTED " )
                print( Fore.RED + " PLEASE NOTE YOU CAN ENTER THE NAME OF FILE EITHER EXISTING OR NOT " )
                print( Fore.RED + " DATA WOULD GET APPENDED IN THE EXISTING FILE !!! " )
                print( Style.RESET_ALL )
                print()
                
                NAME_OF_FILE = input( " PLEASE ENTER THE NAME OF THE CSV FILE ( WITHOUT EXTENSION ) : " ).strip()
                NAME_OF_FILE.strip()
                WORKBOOK = openpyxl.Workbook()

                for SLICING in range( len( DATA ) ) :
                    DATA[ SLICING ] = list( DATA[ SLICING ] )
                    
                    for STRINGING in range( len( DATA[ SLICING ] ) ) :
                        DATA[ SLICING ][ STRINGING ] = str( DATA[ SLICING ][ STRINGING ] )


                WORKBOOK_OPEN = WORKBOOK.active
                WORKBOOK_OPEN.column_dimensions[ 'A' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'B' ].width = 30
                WORKBOOK_OPEN.column_dimensions[ 'C' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'D' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'E' ].width = 30
                WORKBOOK_OPEN.column_dimensions[ 'F' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'G' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'H' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'I' ].width = 25
                WORKBOOK_OPEN.column_dimensions[ 'J' ].width = 25
                WORKBOOK_OPEN.column_dimensions[ 'K' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'L' ].width = 25
                WORKBOOK_OPEN.column_dimensions[ 'M' ].width = 30
                WORKBOOK_OPEN.column_dimensions[ 'N' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'O' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'P' ].width = 15
                WORKBOOK_OPEN.column_dimensions[ 'Q' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'R' ].width = 20
                
                WORKBOOK_OPEN.append( ( " PNR NUMBER " , " PASSENGER'S NAME " , " ID_TYPE " , "ID_NUMBER " , " NUMBER OF SEATS BOOKED " , " DATE OF GOING " , " STARTING POINT " , " ENDING POINT " , " DATE OF RETURNING " ,
                                      " PASSENGER'S CONTACT " , " PASSENGER'S AGE " , " PASSENGER'S GENDER " , " QUOTA " , " CLASS " , " PREFFERED BERTH " , " MEAL " , " PASSENGER'S TYPE " , " USER'S CONTACT " ) )

                WORKBOOK_OPEN.append( ( "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" ) )

                for INSERT in DATA :
                    WORKBOOK_OPEN.append( INSERT )
                    
                WORKBOOK.save( NAME_OF_FILE + ".xlsx" )
                
                FILE_PATH = os.path.abspath( NAME_OF_FILE + ".csv" )
                os.startfile( NAME_OF_FILE + ".xlsx" )
                
        else :
            break



def PRINT_ALL_TICKET() :

    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    while True :
        
        CHOICE1 = input( " DO YOU WANT TO CONTINUE OR NOT ?  (Y/N);(y/n) " ).strip()
        print()
        
        if ( CHOICE1 in [ "Y" , "y" ] ) :
            SQL_QUERY_1 = " select * from RAILWAY_TICKET ; "
                
                
            CURSOR.execute( SQL_QUERY_1 )
            DATA = CURSOR.fetchall()
            
            if ( DATA == [] ) :
               print( Fore.RED + " NO DATA FOUND !!! " )
               print( Fore.RED + " PLEASE TRY AGAIN !!! " )
               print( Style.RESET_ALL )
               print()
               continue
            
            else :
                print( Fore.RED + " PLEASE ENTER THE NAME OF CSV FILE IN WHICH YOUR DATA WOULD BE PRINTED " )
                print( Fore.RED + " PLEASE NOTE YOU CAN ENTER THE NAME OF FILE EITHER EXISTING OR NOT " )
                print( Fore.RED + " DATA WOULD GET APPENDED IN THE EXISTING FILE !!! " )
                print( Style.RESET_ALL )
                print()
                
                NAME_OF_FILE = input( " PLEASE ENTER THE NAME OF THE CSV FILE ( WITHOUT EXTENSION ) : " )
                NAME_OF_FILE.strip()
                WORKBOOK = openpyxl.Workbook()

                for SLICING in range( len( DATA ) ) :
                    DATA[ SLICING ] = list( DATA[ SLICING ] )
                    
                    for STRINGING in range( len( DATA[ SLICING ] ) ) :
                        DATA[ SLICING ][ STRINGING ] = str( DATA[ SLICING ][ STRINGING ] )

                WORKBOOK_OPEN = WORKBOOK.active
                WORKBOOK_OPEN.column_dimensions[ 'A' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'B' ].width = 30
                WORKBOOK_OPEN.column_dimensions[ 'C' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'D' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'E' ].width = 30
                WORKBOOK_OPEN.column_dimensions[ 'F' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'G' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'H' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'I' ].width = 25
                WORKBOOK_OPEN.column_dimensions[ 'J' ].width = 25
                WORKBOOK_OPEN.column_dimensions[ 'K' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'L' ].width = 25
                WORKBOOK_OPEN.column_dimensions[ 'M' ].width = 30
                WORKBOOK_OPEN.column_dimensions[ 'N' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'O' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'P' ].width = 15
                WORKBOOK_OPEN.column_dimensions[ 'Q' ].width = 20
                WORKBOOK_OPEN.column_dimensions[ 'R' ].width = 20
                
                WORKBOOK_OPEN.append( ( " PNR_NUMBER " , " PASSENGER_NAME " , " ID_TYPE " , "ID_NUMBER " , " NUMBER OF SEATS BOOKED " , " DATE_GOING " , " STARTING_POINT " , " ENDING_POINT " , " DATE_RETURN " ,
                                      " PASSENGER_CONTACT " , " PASSENGER_AGE " , " PASSENGER_GENDER " , " QUOTA " , " CLASS " , " PREFFERED_BERTH " , " MEAL " , " PASSENGER_TYPE " , " USER_CONTACT " ) )

                WORKBOOK_OPEN.append( ( "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" , "" ) )

                for INSERT in DATA :
                    WORKBOOK_OPEN.append( INSERT )
                    
                WORKBOOK.save( NAME_OF_FILE + ".xlsx" )
                
                FILE_PATH = os.path.abspath( NAME_OF_FILE + ".csv" )
                os.startfile( NAME_OF_FILE + ".xlsx" )
                
        else :
            break



def DELETE_PARTICULAR_TICKET() :

    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    while True :
        CHOICE1 = input( " DO YOU WANT TO CONTINUE OR NOT ?  (Y/N) ; (y/n) " ).strip()
        print()
        
        if ( CHOICE1 in [ "Y" , "y" ] ) :
            print( " AD : ADHAAR CARD " , "\n" , "\n" , " PP : PASSPORT " , "\n" , "\n" , " DL : DRIVING LICENSE " , "\n" , "\n" , " VC : VOTER ID CARD " , "\n" , "\n" , " PN : PAN CARD " )
            print()
            
            ID_VALUE = input( " PLEASE ENTER YOUR ID TYPE : " ).upper().strip()
            print()
            
            ID_NUMBER = input( " PLEASE ENTER YOUR ID NUMBER : " ).upper().strip()
            print()

            if ID_VALUE in [ "AD" , "PP" , "DL" , "VC" , "PN" ] :
            
                DICT = { "AD" : "ADHAAR CARD" , "PP" : "PASSPORT" , "DL" : "DRIVING LICENSE" , "VC" : "VOTER ID CARD" , "PN" : "PAN CARD" }
                ID_TYPE = DICT[ ID_VALUE ]
                
                SQL_QUERY_1 = " select * from RAILWAY_TICKET where ID_TYPE = '{}' and ID_NUMBER = '{}' ; ".format( ID_TYPE , ID_NUMBER )
                CURSOR.execute( SQL_QUERY_1 )
                DATA1 = CURSOR.fetchall()
                
                if ( DATA1 == [] ) :
                    print( Fore.RED + " NO DATA FOUND WITH THE ID" , ID_TYPE , ID_NUMBER , "!!! " )
                    print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                    print( Style.RESET_ALL )
                    print()
                    continue
                
                else :
                    TABLE = prettytable.PrettyTable( [ " PNR NUMBER " , " PASSENGER NAME " , " ID TYPE " , " ID NUMBER " , " TOTAL NUMBER OF SEATS BOOKED " , " DATE GOING " , " STARTING POINT " , " ENDING POINT " , " DATE RETURN " ,
                                                     " PASSENGER CONTACT " , " PASSENGER AGE " , " PASSENGER GENDER " , " QUOTA " , " CLASS " , " PREFFERED BERTH " , " MEAL " , " PASSENGER TYPE " , " USER ID CONTACT " ] )
                    
                    for INSERT in DATA1 :
                        TABLE.add_row( INSERT )

                    print( TABLE )
                    print()
                    print()
                        
                    print( Fore.RED + " WARNING : THE DATA DELETED FROM HERE WILL GET REFLECTED IN FRAUD REPORT !!! " )
                    print( Style.RESET_ALL )
                    print()
                    print()
                    
                    CHOICE2 = input( " DO YOU WANT TO DELETE THIS TICKET DATA ? (Y/N) ; (y/n) " ).strip()
                    print()
                    
                    if CHOICE2 in [ "Y" , "y" ] :
                        
                        SQL_QUERY_2 = " delete from RAILWAY_TICKET where ID_TYPE = '{}' and ID_NUMBER = '{}' ; ".format( ID_TYPE , ID_NUMBER )
                        CURSOR.execute( SQL_QUERY_2 )
                        DATA2 = list( DATA1[ 0 ] )
                        
                        if ( DATA2[8] == None ) :
                            DATA2[8] = '0000-00-00'

                        
                        INSERT1 = " insert into FRAUD_REPORTS_TICKETS ( PNR_NUMBER ) values( {} ) ; ".format( DATA2[ 0 ] )
                        INSERT2 = " update FRAUD_REPORTS_TICKETS set PASSENGER_NAME = '{}' where PNR_NUMBER = {} ; ".format( DATA2[ 1 ] , DATA2[ 0 ] ) 
                        INSERT3 = " update FRAUD_REPORTS_TICKETS set ID_TYPE = '{}' where PNR_NUMBER = {} ; ".format( DATA2[ 2 ] , DATA2[ 0 ] )
                        INSERT4 = " update FRAUD_REPORTS_TICKETS set ID_NUMBER = '{}' where PNR_NUMBER = {} ; ".format( DATA2[ 3 ] , DATA2[ 0 ] )
                        INSERT5 = " update FRAUD_REPORTS_TICKETS set SEAT_BOOKED = {} where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_TYPE = '{}' and ID_NUMBER = '{}' ; ".format( DATA2[4] , DATA2[0] , DATA2[1] , DATA2[2] , DATA2[3] )
                        INSERT6 = " update FRAUD_REPORTS_TICKETS set DATE_GOING = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_TYPE = '{}' and ID_NUMBER = '{}' ; ".format( DATA2[5] , DATA2[0] , DATA2[1] , DATA2[2] , DATA2[3] ) 
                        INSERT7 = " update FRAUD_REPORTS_TICKETS set STARTING_POINT = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_TYPE = '{}' and ID_NUMBER = '{}' ; ".format( DATA2[6] , DATA2[0] , DATA2[1] , DATA2[2] , DATA2[3] )
                        INSERT8 = " update FRAUD_REPORTS_TICKETS set ENDING_POINT = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_TYPE = '{}' and ID_NUMBER = '{}' ; ".format( DATA2[7] , DATA2[0] , DATA2[1] , DATA2[2] , DATA2[3] )
                        INSERT9 = " update FRAUD_REPORTS_TICKETS set DATE_RETURN = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_TYPE = '{}' and ID_NUMBER = '{}' ; ".format( DATA2[8] , DATA2[0] , DATA2[1] , DATA2[2] , DATA2[3] )
                        INSERT10 = " update FRAUD_REPORTS_TICKETS set PASSENGER_CONTACT = {} where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_TYPE = '{}' and ID_NUMBER = '{}' ; ".format( DATA2[9] , DATA2[0] , DATA2[1] , DATA2[2] , DATA2[3] ) 
                        INSERT11 = " update FRAUD_REPORTS_TICKETS set PASSENGER_AGE = {} where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_TYPE = '{}' and ID_NUMBER = '{}' ; ".format( DATA2[10] , DATA2[0] , DATA2[1] , DATA2[2] , DATA2[3] )
                        INSERT12 = " update FRAUD_REPORTS_TICKETS set PASSENGER_GENDER = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_TYPE = '{}' and ID_NUMBER = '{}' ; ".format( DATA2[11] , DATA2[0] , DATA2[1] , DATA2[2] , DATA2[3] )
                        INSERT13 = " update FRAUD_REPORTS_TICKETS set PASSENGER_TYPE = '{}' where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_TYPE = '{}' and ID_NUMBER = '{}' ; ".format( DATA2[16] , DATA2[0] , DATA2[1] , DATA2[2] , DATA2[3] )
                        INSERT14 = " update FRAUD_REPORTS_TICKETS set USER_CONTACT = {} where PNR_NUMBER = {} and PASSENGER_NAME = '{}' and ID_TYPE = '{}' and ID_NUMBER = '{}' ; ".format( DATA2[17] , DATA2[0] , DATA2[1] , DATA2[2] , DATA2[3] )
                        
                        CURSOR.execute( INSERT1 )
                        CURSOR.execute( INSERT2 )
                        CURSOR.execute( INSERT3 )
                        CURSOR.execute( INSERT4 )
                        CURSOR.execute( INSERT5 )
                        CURSOR.execute( INSERT6 )
                        CURSOR.execute( INSERT7 )
                        CURSOR.execute( INSERT8 )
                        CURSOR.execute( INSERT9 )
                        CURSOR.execute( INSERT10 )
                        CURSOR.execute( INSERT11 )
                        CURSOR.execute( INSERT12 )
                        CURSOR.execute( INSERT13 )
                        CURSOR.execute( INSERT14 )
                        continue
                    
                    else :
                        break
                    
            else :
                print( Fore.RED + " PLEASE ENTER A VALID OPTION !!! " )
                print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                print( Style.RESET_ALL )
                print()
                continue
                
        else :
            break

      

def DELETE_ALL_TICKET() :

    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    while True :
        CHOICE = input( " DO YOU WANT TO DELETE ALL DATA ?  (Y/N);(y/n) " ).strip()
        print()
        
        if ( CHOICE in [ "Y" , "y" ] ) :
            CHECKING = CAPTCHA()
             
            if ( CHECKING == True ) :
                SQL_QUERY_1 = " select * from RAILWAY_TICKET ; "
                CURSOR.execute( SQL_QUERY_1 )
                DATA = CURSOR.fetchall()
                
                if ( DATA == [] ) :
                    print( Fore.RED + " NO DATA EXISTS !!! " )
                    print( Fore.RED + " THE DATA HAS BEEN ALREADY DELETED !!! " )
                    print( Style.RESET_ALL )
                    print()
                    break

                else :
                    CURRENT_DATE = datetime.date.today() 
                    SQL_QUERY_2 = " delete from RAILWAY_TICKET where DATE_GOING < '{}' or DATE_RETURN < '{}'; ".format( CURRENT_DATE , CURRENT_DATE )
                    CURSOR.execute( SQL_QUERY_2 )
                    break
                
            else :
                break
                
        else :
            break


    
def ADMIN_DELETE_ACCOUNT() :
    
    import mysql.connector as MS
    MYCONNECTION  = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    for ATTEMPTS in range(0,4,1) :
        FLAG1 = 0
        DATA = []
        
        USERNAME = input( " PLEASE ENTER YOUR USERNAME : " ).strip()
        print()

        SQL_QUERY_1 = " select * from ADMIN_ACCOUNTS where ADMIN_ACCOUNTS = '{}' ; ".format( USERNAME )
        CURSOR.execute( SQL_QUERY_1 )
        DATA = CURSOR.fetchall()
        
        if ( DATA == [] ) :
            print( Fore.RED + " ACCOUNT DOES NOT EXISTS !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            FLAG1 = -1
            print()
            continue
            
        else :
            PASSWORD = input( " PLEASE ENTER YOUR PASSWORD : " ).strip()
            print()
            SQL_QUERY_2 = " select PASSWORD , NAME from ADMIN_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
            CURSOR.execute( SQL_QUERY_2 )
            DATA1 = CURSOR.fetchall()
            
            if ( PASSWORD == DATA1[0][0] ) :
                print( " WELCOME" , DATA1[ 0 ][ 1 ] )
                SQL_QUERY_3 = " select * from ADMIN_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
                LIST = [ " USERNAME  " , " PASSWORD " , " CONTACT " , " GENDER " , " DATE_OF_BIRTH " ]
                CURSOR.execute( SQL_QUERY_3 )
                DATA2 = CURSOR.fetchall()
                DATA2_LISTING = list(DATA2[ 0 ])
                PASSWORD = DATA2_LISTING[ 1 ]
                
                PASSWORD_SHOWN = (( len(A)-3 )*"*" + A[ len(A)-3 : : ] )
                
                print( LIST[ 0 ] , ":" , DATA2_LISTING[ 0 ] )

                print()
                
                print( LIST[ 1 ] , ":" , PASSWORD_SHOWN )

                print()
                
                print( LIST[ 2 ] , ":" , DATA2_LISTING[ 2 ] )

                print()
                
                print( LIST[ 3 ] , ":" , DATA2_LISTING[ 3 ] )

                print()
                
                print( LIST[ 4 ] , ":" , DATA2_LISTING[ 4 ] )

                print()
                
                print( LIST[ 5 ] , ":" , DATA2_LISTING[ 5 ] )

                print()

                print()
                    
                CHOICE = input( " IS THIS YOUR ACCOUNT (Y/N);(y/n) : " )
                print()
                
                if ( CHOICE in [ "Y" , "y" ] ) :
                    CHECK = CAPTCHA()
                    
                    if ( CHECK == True ) :
                        SQL_QUERY_4 = " delete from ADMIN_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
                        CURSOR.execute( SQL_QUERY_4 )
                        FLAG = 1
                        break
                    
                    else :
                        FLAG = 0
                        break
                    
                else :
                    FLAG = 0
                    break
                            
            else :
                print( Fore.RED + " WRONG PASSWORD !!! " )
                print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                print( Style.RESET_ALL )
                print()
                FLAG1 = -1
                continue   
                    
    if ( FLAG == -1 ) :
        print( Fore.RED + " YOU HAVE EXCEDEED THE MAXIMUM NUMBER OF YOUR TRIALS !!! " )
        print( Fore.RED + " PLEASE TRY AGAIN AFTER 1 HOUR !!! " )
        print( Style.RESET_ALL )
        print()

    elif ( FLAG == 1 ) :
        
        FILE_HANDLE = open( r"C:\Users\dell\Desktop\TIMELINES\ADMIN_ACCOUNT_TIMELINE.dat" , "ab" )

        TIME_ADMIN_ACCOUNT = datetime.datetime.today()
        ADMIN_TIMELINE_LIST = [ USERNAME , str( USER_CONTACT ) , "ACCOUNT_DELETION" , str( TIME_ADMIN_ACCOUNT ) ]

        pickle.dump( ADMIN_TIMELINE_LIST , FILE_HANDLE )

        FILE_HANDLE.close()

        print( " YOUR ACCOUNT WAS SUCCESSFULLY DELETED !!! " )
        print( " WE ARE SAD SEEING YOU GO !!! " )
        print( " SEE YOU SOON AGAIN !!! " )
        print()
        
    else :
        print( Fore.RED + " YOU EITHER ENTERED WRONG CAPTCHA OR SELECTED NO FOR DELETION OF ACCOUNT !!! " )
        print( Style.RESET_ALL )
        print()


        
def MAIN_PROGRAM_HEAD_ADMIN() :
    
    while True :
        try :
            print( Fore.CYAN )
            
            print( " 1. ADMIN ACCOUNT DETAILS " , "\n" , "\n" , "2. USER ACCOUNT DETAILS " , "\n" , "\n" , "3. ADMIN TIMELINE " , "\n" , "\n" , "4. USER TIMELINE " , "\n" , "\n" , "5. USER TICKET TIMELINE " , "\n" )
            print( " 6. SHOW ALL TICKET " , "\n" , "\n" , "7. SHOW PARTICULAR TICKET " , "\n" , "\n" , "8. DELETE PARTICULAR TICKET " , "\n" , "\n" , "9. DELETE ALL TICKET " , "\n" , "\n" , "10. SHOW USER COUNT " , "\n" )
            print( " 11. SHOW ADMIN COUNT " , "\n" , "\n" , "12. DELETE USER ACCOUNT " , "\n" , "\n" , "13. DELETE ADMIN ACCOUNT " , "\n" , "\n" , "14. LOG OUT " , "\n" )

            print( Style.RESET_ALL )
           
            CHOICE = int ( eval ( input ( " PLEASE ENTER YOUR CHOICE : " ) ) )
            print( ansi.clear_screen() )
            print()
            print()
            
            if ( CHOICE == 1 ) :
                ADMIN_ACCOUNT_DETAILS_HEAD_ADMIN()
                continue
            
            elif ( CHOICE == 2 ) :
                USER_ACCOUNT_DETAILS_HEAD_ADMIN()
                continue
            
            elif ( CHOICE == 3 ) :
                ADMIN_TIMELINE()
                continue
            
            elif ( CHOICE == 4 ) :
                USER_TIMELINE()
                continue

            elif ( CHOICE == 5 ) :
                USER_TICKET_TIMELINE()
                continue

            elif ( CHOICE == 6 ) :
                SHOW_ALL_TICKET()
                continue

            elif ( CHOICE == 7 ) :
                SHOW_PARTICULAR_TICKET()
                continue
            
            elif ( CHOICE == 8 ) :              
                DELETE_PARTICULAR_TICKET()
                continue

            elif ( CHOICE == 9 ) :
                DELETE_ALL_TICKET()
                continue

            elif ( CHOICE == 10 ) :
                SHOW_USER_COUNT()
                continue

            elif ( CHOICE == 11 ) :
                SHOW_ADMIN_COUNT()
                continue

            elif ( CHOICE == 12 ) :
                DELETE_USER_ACCOUNT()
                continue

            elif ( CHOICE == 13 ) :
                DELETE_ADMIN_ACCOUNT()
                continue
            
            elif ( CHOICE == 14 ) :
                print( " THANK YOU !!! " )
                break
            
            else:
                print( Fore.RED + " INVALID INPUT !!! " )
                print( Fore.RED + " PLEASE ENTER A VALID CHOICE !!! " )
                print( Style.RESET_ALL )
                print()
                continue
                
        except :
            print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            print()
            continue



def ADMIN_ACCOUNT_DETAILS_HEAD_ADMIN() :

    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    while True :
        
        CHOICE1 = input( " DO YOU WANT TO CONTINUE OR NOT ?  (Y/N);(y/n) " ).strip()
        print()
        
        if ( CHOICE1 in [ "Y" , "y" ] ) :
            while True :
                try :
                    print( " 1. SHOW ALL ACCOUNTS \n" )
                    print( " 2. SHOW PARTICULAR ACCOUNT \n" )
                    print()
                    
                    CHOICE2 = int ( eval ( input ( " PLEASE SELECT THE OPTION BY WHICH YOU WANT TO SEARCH : " ) ) )
                    print()
                     
                    if ( CHOICE2 == 1 ) :
                        SQL_QUERY_1 = " select * from ADMIN_ACCOUNTS ; "
                        break
                           
                    elif ( CHOICE2 == 2 ) :
                        while True :
                            try :
                                print( " 1. SEARCH BY CONTACT \n" )
                                print( " 2. SEARCH BY USER NAME \n" )
                                print()
                                
                                CHOICE3 = int ( eval ( input ( " PLEASE SELECT THE OPTION BY WHICH YOU WANT TO SEARCH : " ) ) )
                                print()
                                 
                                if ( CHOICE3 == 1 ) :
                                    while True :
                                        try :
                                            print( Fore.RED + " PLEASE AVOID USING '0' OR '+' SIGN BEFORE ADMIN'S CONTACT !!! " )
                                            print( Style.RESET_ALL )
                                            print()
                                            
                                            CONTACT = int ( eval ( input ( " PLEASE ENTER THE ADMIN'S CONTACT : " ) ) )
                                            print()
                                            
                                            SQL_QUERY_1 = " select * from ADMIN_ACCOUNTS where ADMIN_CONTACT = {} ; ".format( CONTACT )
                                            break
                                        
                                        except :
                                            print( Fore.RED + " INVALID CONTACT !!! " )
                                            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                                            print( Style.RESET_ALL )
                                            print()
                                            continue
                                                
                                elif ( CHOICE3 == 2 ) :
                                    USERNAME = input( " PLEASE ENTER THE ADMIN'S USERNAME : " ).strip()
                                    print()
                                    
                                    SQL_QUERY_1 = " select * from ADMIN_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
                                    break

                                else :
                                    print( Fore.RED + " INVALID CHOICE !!! " )
                                    print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                                    print( Style.RESET_ALL )
                                    print()
                                    continue
                                
                            except :
                                print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
                                print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                                print( Style.RESET_ALL )
                                print()
                                continue
                            
                            break
                        
                    else :
                        print( Fore.RED + " INVALID CHOICE !!! " )
                        print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                        print( Style.RESET_ALL )
                        print()
                        continue
                    
                    break
                
                except :
                    print( Fore.RED + " PLEASE ENTER A NUMERIC VALUE !!! " )
                    print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                    print( Style.RESET_ALL )
                    print()
                    break
                
            CURSOR.execute( SQL_QUERY_1 )
            DATA = CURSOR.fetchall()
            
            if ( DATA == [] ) :
               print( Fore.RED + " NO DATA FOUND !!! " )
               print( Fore.RED + " PLEASE TRY AGAIN !!! " )
               print( Style.RESET_ALL )
               print()
               continue
            
            else :
                TABLE = prettytable.PrettyTable( ( " USER_NAME " , " PASSWORD " , " NAME " , " CONTACT " , " GENDER " , " DATE OF BIRTH " ) )
                
                for INSERT in DATA :
                    TABLE.add_row( INSERT )
                    continue
                
                print( TABLE )
                   
        else :
            break

    

def USER_ACCOUNT_DETAILS_HEAD_ADMIN() :

    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True
    
    while True :
        
        CHOICE1 = input( " DO YOU WANT TO CONTINUE OR NOT ?  (Y/N);(y/n) " ).strip()
        print()
        
        if ( CHOICE1 in [ "Y" , "y" ] ) :
            while True :
                try :
                    print( " 1. SHOW ALL ACCOUNTS \n" )
                    print( " 2. SHOW PARTICULAR ACCOUNT \n" )
                    print()
                    
                    CHOICE2 = int ( eval ( input( " PLEASE SELECT THE OPTION BY WHICH YOU WANT TO SEARCH : " ) ) )
                    print()
                     
                    if ( CHOICE2 == 1 ) :
                        SQL_QUERY_1 = " select * from USER_ACCOUNTS ; "
                        break
                         
                    elif ( CHOICE2 == 2 ) :
                        while True :
                            try :
                                print( " 1. SEARCH BY CONTACT \n" )
                                print( " 2. SEARCH BY USER NAME \n" )
                                print()
                                
                                CHOICE3 = int ( eval ( input ( " PLEASE SELECT THE OPTION BY WHICH YOU WANT TO SEARCH : " ) ) )
                                print()
                                 
                                if ( CHOICE3 == 1 ) :
                                    while True :
                                        try :
                                            print( Fore.GREEN + Style.BRIGHT + " PLEASE AVOID USING '0' OR '+' SIGN BEFORE USER'S CONTACT !!! " )
                                            print( Style.RESET_ALL )
                                            print()
                                            
                                            CONTACT = int ( eval ( input ( " PLEASE ENTER THE USER'S CONTACT : " ) ) )
                                            print()
                                            SQL_QUERY_1 = " select * from USER_ACCOUNTS where USER_CONTACT = {} ; ".format( CONTACT )
                                            break
                                        
                                        except :
                                            print( Fore.RED + " INVALID CONTACT !!! " )
                                            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                                            print( Style.RESET_ALL )
                                            print()
                                            continue
                                                
                                elif ( CHOICE3 == 2 ) :
                                    USERNAME = input( " PLEASE ENTER THE USER'S USERNAME : " )
                                    print()
                                    SQL_QUERY_1 = " select * from USER_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
                                    break

                                else :
                                    print( Fore.RED + " INVALID CHOICE !!! " )
                                    print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                                    print( Style.RESET_ALL )
                                    print()
                                    continue
                                
                            except :
                                print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
                                print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                                print( Style.RESET_ALL )
                                print()
                                continue
                            
                            break
                        
                    else :
                        print( Fore.RED + " INVALID CHOICE !!! " )
                        print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                        print( Style.RESET_ALL )
                        print()
                        continue
                    
                    break
                
                except :
                    print( Fore.RED + " PLEASE ENTER A NUMERIC VALUE !!! " )
                    print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                    print( Style.RESET_ALL )
                    print()
                    break
                
            CURSOR.execute( SQL_QUERY_1 )
            DATA = CURSOR.fetchall()
            
            if ( DATA == [] ) :
               print( Fore.RED + " NO DATA FOUND !!! " )
               print( Fore.RED + " PLEASE TRY AGAIN !!! " )
               print( Style.RESET_ALL )
               print()
               continue
            
            else :
                TABLE = prettytable.PrettyTable( ( " USER_NAME " , " PASSWORD " , " NAME " , " CONTACT " , " GENDER " , " DATE OF BIRTH " , " EMAIL ID " ) )
                
                for LOOP in range( 0 , len( DATA ) , 1 ) :
                    TABLE.add_row( DATA[ LOOP ] )
                    continue

                print( TABLE )
                print()
                print()
                continue
                   
        else :
            break
    

def ADMIN_TIMELINE() :
    
    while True :
        try :    
            CHOICE1 = input( " DO YOU WANT TO CONTINUE OR NOT ?  (Y/N);(y/n) " )
            print()
            
            if ( CHOICE1 in [ "Y" , "y" ] ) :
                RECORD1 = []
                RECORD2 = []
                FILE_HANDLE = open( r"C:\Users\dell\Desktop\TIMELINES\ADMIN_ACCOUNT_TIMELINE.dat" , "rb" )
                
                while True :
                    try :
                        DATA = pickle.load( FILE_HANDLE )
                        RECORD1.append( DATA )
                        continue
                        
                    except :
                        break

                if ( RECORD1 == [] ) :
                    print( Fore.RED + " NO DATA FOUND !!! " )
                    print( Fore.RED + " PLEASE TRY AGAIN  !!! " )
                    print( Style.RESET_ALL )
                    print()
                    break
                    
                else :
                    print( " 1. SHOW ALL ADMIN'S TIMELINE \n" )
                    print( " 2. SHOW PARTICULAR ADMIN'S TIMELINE \n" )
                    print()
                    
                    CHOICE2 = int ( eval ( input ( " PLEASE SELECT THE OPTIONS BY WHICH YOU WANT TO SEARCH : " ) ) )
                    print()

                    if ( CHOICE2 == 1 ) :
                        
                        TABLE = prettytable.PrettyTable( ( " USERNAME " , " ADMIN CONTACT " , " FUNCTION " , " DATE AND TIME " ) )
                        TABLE.add_row( ( "" , "" , "" , "" ) )
                        
                        TABLE.add_rows( RECORD1 )

                        print( TABLE )
                        print()
                        continue
                                           
                    elif ( CHOICE2 == 2 ) :
                        
                        print( " 1. USERNAME \n" )
                        print( " 2. CONTACT \n" )
                        print()
                        
                        CHOICE3 = int ( eval ( input ( " PLEASE SELECT THE OPTIONS BY WHICH YOU WANT TO SEARCH : " ) ) )
                        print()

                        if ( CHOICE3 == 1 ) :
                            
                            USERNAME = input ( " PLEASE ENTER USER'S USERNAME : " ).strip()
                            print()
                            
                            for SHOW in RECORD1 :
                                if ( SHOW[0] == USERNAME ) :
                                    RECORD2.append( SHOW )
                                
                                else :
                                    continue

                            if ( RECORD2 == [] ) :
                                print( Fore.RED + " NO DATA FOUND WITH USERNAME", USERNAME , "!!! " )
                                print( Fore.RED + " PLEASE TRY AGAIN  !!! " )
                                print( Style.RESET_ALL )
                                print()
                                continue

                            else :

                                TABLE = prettytable.PrettyTable( ( " USERNAME " , " ADMIN CONTACT " , " FUNCTION " , " DATE AND TIME " ) )
                                TABLE.add_row( ( "" , "" , "" , "" ) )
                                
                                TABLE.add_rows( RECORD2 )

                                print( TABLE )
                                print()
                                continue

                                
                        elif ( CHOICE3 == 2 ) :

                            print( Fore.RED + " PLEASE AVOID USING '0' OR '+' SIGN BEFORE ADMIN'S CONTACT !!! " )
                            print( Style.RESET_ALL )
                            print()

                            CONTACT = int ( eval ( input ( " PLEASE ENTER ADMIN'S CONTACT : " ) ) )
                            print()
                            
                            for SHOW in RECORD1 :
                                if ( str( CONTACT ) == SHOW[ 1 ] ) :
                                    RECORD2.append( SHOW )
                                    
                                else :
                                    continue

                            if ( RECORD2 == [] ) :
                                print( Fore.RED + " NO DATA FOUND WITH USERNAME", USERNAME , "!!! " )
                                print( Fore.RED + " PLEASE TRY AGAIN  !!! " )
                                print( Style.RESET_ALL )
                                print()
                                continue

                            else :
                                TABLE = prettytable.PrettyTable( ( " USERNAME " , " ADMIN CONTACT " , " FUNCTION " , " DATE AND TIME " ) )
                                TABLE.add_row( ( "" , "" , "" , "" ) )
                                
                                TABLE.add_rows( RECORD2 )

                                print( TABLE )
                                print()
                                continue
                        
                         
                        else :
                            print( Fore.RED + " PLEASE ENTER A VALID OPTION !!! " )
                            print( Fore.RED + " PLEASE TRY AGAIN  !!! " )
                            print( Style.RESET_ALL )
                            print()
                            continue
                
            else :
                break
        
            
        except :
            print( Fore.RED + " PLEASE ENTER A NUMERIC VALUE !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            print()
            continue



def USER_TIMELINE() :
    
    while True :
        try :    
            CHOICE1 = input( " DO YOU WANT TO CONTINUE OR NOT ?  (Y/N);(y/n) " )
            print()
            
            if ( CHOICE1 in [ "Y" , "y" ] ) :
                RECORD1 = []
                RECORD2 = []
                FILE_HANDLE = open( r"C:\Users\dell\Desktop\TIMELINES\USER_ACCOUNT_TIMELINE.dat" , "rb" )
                
                while True :
                    try :
                        DATA = pickle.load( FILE_HANDLE )
                        RECORD1.append( DATA )
                        continue
                        
                    except :
                        break

                if ( RECORD1 == [] ) :
                    print( Fore.RED + " NO DATA FOUND !!! " )
                    print( Fore.RED + " PLEASE TRY AGAIN  !!! " )
                    print( Style.RESET_ALL )
                    print()
                    break
                    
                else :
                    print( " 1. SHOW ALL USER'S TIMELINE \n" )
                    print( " 2. SHOW PARTICULAR USER'S TIMELINE \n" )
                    print()
                    
                    CHOICE2 = int ( eval ( input ( " PLEASE SELECT THE OPTIONS BY WHICH YOU WANT TO SEARCH : " ) ) )
                    print()

                    if ( CHOICE2 == 1 ) :
                        
                        TABLE = prettytable.PrettyTable( ( " USERNAME " , " USER CONTACT " , " FUNCTION " , " DATE AND TIME " ) )
                        TABLE.add_row( ( "" , "" , "" , "" ) )
                        
                        TABLE.add_rows( RECORD1 )

                        print( TABLE )
                        print()
                        print()
                        continue
                                           
                    elif ( CHOICE2 == 2 ) :
                        
                        print( " 1. USERNAME \n" )
                        print( " 2. CONTACT \n" )
                        print()
                        
                        CHOICE3 = int ( eval ( input ( " PLEASE SELECT THE OPTIONS BY WHICH YOU WANT TO SEARCH : " ) ) )
                        print()

                        if ( CHOICE3 == 1 ) :
                            
                            USERNAME = input ( " PLEASE ENTER USER'S USERNAME : " ).strip()
                            print()
                            
                            for SHOW in RECORD1 :
                                if ( SHOW[0] == USERNAME ) :
                                    RECORD2.append( SHOW )
                                
                                else :
                                    continue

                            if ( RECORD2 == [] ) :
                                print( Fore.RED + " NO DATA FOUND WITH USERNAME", USERNAME , "!!! " )
                                print( Fore.RED + " PLEASE TRY AGAIN  !!! " )
                                print( Style.RESET_ALL )
                                print()
                                continue

                            else :

                                TABLE = prettytable.PrettyTable( ( " USERNAME " , " USER CONTACT " , " FUNCTION " , " DATE AND TIME " ) )
                                TABLE.add_row( ( "" , "" , "" , "" ) )
                                
                                TABLE.add_rows( RECORD2 )

                                print( TABLE )
                                print()
                                print()
                                continue

                                
                        elif ( CHOICE3 == 2 ) :

                            print( Fore.GREEN + Style.BRIGHT + " PLEASE AVOID USING '0' OR '+' SIGN BEFORE USER'S CONTACT !!! " )
                            print( Style.RESET_ALL )
                            print()

                            CONTACT = int ( eval ( input ( " PLEASE ENTER USER'S CONTACT : " ) ) )
                            print()
                            
                            for SHOW in RECORD1 :
                                if ( str( CONTACT ) == SHOW[ 1 ] ) :
                                    RECORD2.append( SHOW )
                                    
                                else :
                                    continue

                            if ( RECORD2 == [] ) :
                                print( Fore.RED + " NO DATA FOUND WITH USERNAME", USERNAME , "!!! " )
                                print( Fore.RED + " PLEASE TRY AGAIN  !!! " )
                                print( Style.RESET_ALL )
                                print()
                                continue

                            else :
                                TABLE = prettytable.PrettyTable( ( " USERNAME " , " USER CONTACT " , " FUNCTION " , " DATE AND TIME " ) )
                                TABLE.add_row( ( "" , "" , "" , "" ) )
                                
                                TABLE.add_rows( RECORD2 )

                                print( TABLE )
                                print()
                                print()
                                continue
                         
                        else :
                            print( Fore.RED + " PLEASE ENTER A VALID OPTION !!! " )
                            print( Fore.RED + " PLEASE TRY AGAIN  !!! " )
                            print( Style.RESET_ALL )
                            print()
                            continue
                
            else :
                print()
                break
            
            
        except :
            print( Fore.RED + " PLEASE ENTER A NUMERIC VALUE !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            print()
            continue

    

def USER_TICKET_TIMELINE() :
    
    while True :
        try :    
            CHOICE1 = input( " DO YOU WANT TO CONTINUE OR NOT ?  (Y/N);(y/n) " )
            print()
            
            if ( CHOICE1 in [ "Y" , "y" ] ) :
                FILE_HANDLE = open( r"C:\Users\dell\Desktop\TIMELINES\USER_TICKET_TIMELINE.txt" , "r" )
               
                print( " 1. SHOW ALL USER'S TICKET TIMELINE \n" )
                print( " 2. SHOW PARTICULAR USER'S TICKET TIMELINE \n" )
                print()
                
                CHOICE2 = int ( eval ( input ( " PLEASE SELECT THE OPTIONS BY WHICH YOU WANT TO SEARCH : " ) ) )
                print()

                if ( CHOICE2 == 1 ) :
                    DATA = FILE_HANDLE.readlines()
                    TABLE = prettytable.PrettyTable( ( " CONTACT " , " FUNCTION " , " TOTAL SEAT BOOKED " , " PNR NUMBER "  , " DATE " , " TIME " ) )
                    TABLE.add_row( ( "" , "" , "" , "" , "" , "" ) )
                    
                    for INSERT in DATA :
                        DATA1 = INSERT.split()
                        TABLE.add_row( DATA1 )

                    print( TABLE )
                    print()
                    print()
                    continue
                                       
                elif ( CHOICE2 == 2 ) :
                    
                    print( " 1. CONTACT \n" )
                    print( " 2. PNR NUMBER \n" )
                    print()
                    
                    CHOICE3 = int ( eval ( input ( " PLEASE SELECT THE OPTIONS BY WHICH YOU WANT TO SEARCH : " ) ) )
                    print()
                    print()
                    
                    if ( CHOICE3 == 1 ) :
                        RECORD = []
                        DATA1 = FILE_HANDLE.readlines()

                        print( Fore.GREEN + Style.BRIGHT + " PLEASE AVOID USING '0' OR '+' SIGN BEFORE USER'S CONTACT !!! " )
                        print( Style.RESET_ALL )
                        print()

                        CONTACT = int ( eval ( input ( " PLEASE ENTER USER'S CONTACT : " ) ) )
                        print()
                        
                        for SHOW in DATA1 :
                            DATA2 = SHOW.split()
                            if ( str( CONTACT ) == DATA2[ 0 ] ) :
                                RECORD.append( DATA2 )
                                
                            else :
                                continue                
                     
                    elif ( CHOICE3 == 2 ) :
                        RECORD = []
                        DATA1 = FILE_HANDLE.readlines()

                        PNR_NUMBER = int ( eval ( input ( " PLEASE ENTER TICKET'S PNR NUMBER : " ) ) )
                        print()
                        
                        for SHOW in DATA1 :
                            DATA2 = SHOW.split()
                            if ( str( PNR_NUMBER ) == DATA2[ 3 ] ) :
                                RECORD.append( DATA2 )
                            
                            else :
                                continue                

                    else :
                        print( Fore.RED + " PLEASE ENTER A VALID OPTION !!! " )
                        print( Fore.RED + " PLEASE TRY AGAIN  !!! " )
                        print( Style.RESET_ALL )
                        print()
                        continue
                    
                    TABLE = prettytable.PrettyTable( ( " CONTACT " , " FUNCTION " , " PNR NUMBER " , " TOTAL SEAT BOOKED " , " DATE " , " TIME " ) )
                    TABLE.add_row( ( "" , "" , "" , "" , "" , "" ) )

                    if ( RECORD == [] ) :
                        print( Fore.RED + " NO DATA FOUND !!! " )
                        print( Fore.RED + " PLEASE TRY AGAIN  !!! " )
                        print( Style.RESET_ALL )
                        print()
                        continue
                    
                    else :
                        for INSERT in range( 0 , len( RECORD ) , 1 ) :
                            TABLE.add_row( RECORD[ INSERT ] )
                            continue

                        print( TABLE )
                        print()
                        print()
                        FILE_HANDLE.close()
                    
                else :
                    print( Fore.RED + " PLEASE ENTER A VALID OPTION " )
                    print( Fore.RED + " PLEASE TRY AGAIN  !!! " )
                    print( Style.RESET_ALL )
                    print()
                    continue
                
            else :
                break
                
        except :
            print( Fore.RED + " PLEASE ENTER A NUMERIC VALUE !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN !!! " )
            print( Style.RESET_ALL )
            print()
            continue



def SHOW_USER_COUNT() :
    
    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True

    SQL_QUERY = " select count(*) from USER_ACCOUNTS ; "
    CURSOR.execute( SQL_QUERY )
    DATA = CURSOR.fetchall()
    COUNT = DATA[ 0 ][ 0 ]

    print( " TOTAL NUMBER OF USER ACCOUNTS IN THE DATABASE ARE : " , COUNT )

    

def SHOW_ADMIN_COUNT() :
    
    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True

    SQL_QUERY = " select count(*) from ADMIN_ACCOUNTS ; "
    CURSOR.execute( SQL_QUERY )
    DATA = CURSOR.fetchall()
    COUNT = DATA[ 0 ][ 0 ]

    print( " TOTAL NUMBER OF USER ACCOUNTS IN THE DATABASE ARE : " , COUNT )



def DELETE_USER_ACCOUNT() :

    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True

    while True :
        
        CHOICE1 = input( " DO YOU WANT TO CONTINUE OR NOT ?  (Y/N) ; (y/n) " )
        print()
        
        if ( CHOICE1 in [ "Y" , "y" ] ) :
            while True :
                try :
                    print( " 1. DELETE BY CONTACT \n" )
                    print( " 2. DELETE BY USERNAME \n" )
                    print()
                    
                    CHOICE2 = int ( eval ( input ( " PLEASE ENTER YOUR CHOICE : " ) ) )
                    print()
                    
                    if ( CHOICE2 == 1 ) :
                        print( Fore.GREEN + Style.BRIGHT + " PLEASE AVOID USING '0' OR '+' SIGN BEFORE USER'S CONTACT !!! " )
                        print( Style.RESET_ALL )
                        print()
                        
                        CONTACT = int ( eval ( input ( " PLEASE ENTER USER'S CONTACT : " ) ) )
                        print()
                        
                        SQL_QUERY_1 = " select * from USER_ACCOUNTS where USER_CONTACT = {} ; ".format( CONTACT )
                        SQL_QUERY_2 = " delete from USER_ACCOUNTS where USER_CONTACT = {} ; ".format( CONTACT )
                        print()

                    elif ( CHOICE2 == 2 ) :
                        USERNAME = input( " PLEASE ENTER USER'S USERNAME : " )
                        SQL_QUERY_1 = " select * from USER_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
                        SQL_QUERY_2 = " delete from USER_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
                        print()
                        

                    else :
                        print( Fore.RED + " INVALID CHOICE !!! " )
                        print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                        print( Style.RESET_ALL )
                        print()
                        continue
                    
                    CURSOR.execute( SQL_QUERY_1 )
                    DATA1 = CURSOR.fetchall()
                    
                    
                    if ( DATA1 == [] ) :
                        print( Fore.RED + " ACCOUNT DOES NOT EXISTS !!! " )
                        print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                        print( Style.RESET_ALL )
                        print()
                        break
                        
                    else :
                        TABLE = prettytable.PrettyTable( ( " USER_NAME " , " PASSWORD " , " NAME " , " CONTACT " , " GENDER " , " DATE OF BIRTH " , " EMAIL ID " ) )
                        
                        for INSERT in DATA1 :
                            TABLE.add_row( INSERT )

                        print( TABLE )
                        print()
                        print()
                        
                        print( Fore.RED + " WARNING : THE DATA DELETED FROM HERE WILL GET REFLECTED IN FRAUD REPORT !!! " )
                        print( Style.RESET_ALL )
                        print()
                        
                        CHOICE3 = input( " DO YOU WANT TO DELETE THIS ACCOUNT ? (Y/N) ; (y/n) " )
                        print()
                        
                        if ( CHOICE3 in [ "Y" , "y" ] ) :
                            
                            CURSOR.execute( SQL_QUERY_2 )
                            print( " ACCOUNT DELETED SUCCESFULLY !!! " )
                            
                            DATA2 = DATA1[ 0 ]
                            
                            INSERT1 = " insert into FRAUD_REPORTS_ACCOUNTS ( USER_NAME ) values( '{}' ) ".format( DATA2[ 0 ] )
                            INSERT2 = " update FRAUD_REPORTS_ACCOUNTS set PASSWORD = '{}' where USER_NAME = '{}' ; ".format( DATA2[ 1 ] , DATA2[ 0 ] ) 
                            INSERT3 = " update FRAUD_REPORTS_ACCOUNTS set NAME = '{}' where USER_NAME = '{}' ; ".format( DATA2[ 2 ] , DATA2[ 0 ] )
                            INSERT4 = " update FRAUD_REPORTS_ACCOUNTS set USER_CONTACT = {} where USER_NAME = '{}' ; ".format( DATA2[ 3 ] , DATA2[ 0 ] )
                            INSERT5 = " update FRAUD_REPORTS_ACCOUNTS set GENDER = '{}' where USER_NAME = '{}' ".format( DATA2[4] , DATA2[0] )
                            INSERT6 = " update FRAUD_REPORTS_ACCOUNTS set DATE_OF_BIRTH = '{}' where USER_NAME = '{}' ".format( DATA2[5] , DATA2[0] )
                            INSERT7 = " update FRAUD_REPORTS_ACCOUNTS set EMAIL_ACCOUNT = '{}' where USER_NAME = '{}' ".format( DATA2[6] , DATA2[0] ) 
                            
                            CURSOR.execute( INSERT1 )
                            CURSOR.execute( INSERT2 )
                            CURSOR.execute( INSERT3 )
                            CURSOR.execute( INSERT4 )
                            CURSOR.execute( INSERT5 )
                            CURSOR.execute( INSERT6 )
                            CURSOR.execute( INSERT7 )
                            print()
                            break
                        
                        else :
                            break

                except :
                    print( Fore.RED + " PLEASE ENTER A NUMERIICAL VALUE !!! " )
                    print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                    print( Style.RESET_ALL )
                    print()
                    continue

        else :
            break
                    
                

def DELETE_ADMIN_ACCOUNT() :

    import mysql.connector as MS
    MYCONNECTION = MS.connect( host = "localhost" , user = "root" , passwd = "12345" , database = "RAILWAY_RESERVATION_SYSTEM" )
    CURSOR = MYCONNECTION.cursor()
    MYCONNECTION.autocommit = True

    while True :
        CHOICE1 = input( " DO YOU WANT TO CONTINUE OR NOT ?  (Y/N) ; (y/n) " )
        print()
        
        if ( CHOICE1 in [ "Y" , "y" ] ) :
            while True :
                try :
                    print( " 1. DELETE BY CONTACT \n" )
                    print( " 2. DELETE BY USERNAME \n" )
                    print()
                    
                    CHOICE2 = int ( eval ( input ( " PLEASE ENTER YOUR CHOICE : " ) ) )
                    print()
                    
                    if ( CHOICE2 == 1 ) :
                        print( Fore.RED + " PLEASE AVOID USING '0' OR '+' SIGN BEFORE ADMIN'S CONTACT !!! " )
                        print( Style.RESET_ALL )
                        print()
                        
                        CONTACT = int ( eval ( input ( " PLEASE ENTER ADMIN'S CONTACT : " ) ) )
                        print()
                        
                        SQL_QUERY_1 = " select * from ADMIN_ACCOUNTS where ADMIN_CONTACT = {} ; ".format( CONTACT )
                        SQL_QUERY_2 = " delete from ADMIN_ACCOUNTS where ADMIN_CONTACT = {} ; ".format( CONTACT )

                    elif ( CHOICE2 == 2 ) :
                        USERNAME = input( " PLEASE ENTER ADMIN'S USERNAME : " )
                        print()
                        
                        SQL_QUERY_1 = " select * from ADMIN_ACCOUNTS where USER_NAME = '{}' ; ".format( USERNAME )
                        SQL_QUERY_2 = " delete from ADMIN_ACCOUNTS where USER_NAME = '{}'  ".format( USERNAME )

                    else :
                        print( Fore.RED + " INVALID CHOICE !!! " )
                        print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                        print( Style.RESET_ALL )
                        print()
                        continue
                    
                    CURSOR.execute( SQL_QUERY_1 )
                    DATA1 = CURSOR.fetchall()
                    
                    if ( DATA1 == [] ) :
                        print( Fore.RED + " ACCOUNT DOES NOT EXISTS !!! " )
                        print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                        print( Style.RESET_ALL )
                        print()
                        
                    else :
                        TABLE = prettytable.PrettyTable( ( " USERNAME " , " PASSWORD " , " NAME " , " CONTACT " , " GENDER " , " DATE OF BIRTH " ) )
                        
                        for INSERT in DATA1 :
                            TABLE.add_row( INSERT )

                        print( TABLE )
                        print()
                        print()
                        
                        CHOICE3 = input ( " DO YOU WANT TO DELETE THIS ACCOUNT ? (Y/N) ; (y/n) " )
                        print()
                        
                        if ( CHOICE3 in [ "Y" , "y" ] ) :
                            CURSOR.execute( SQL_QUERY_2 )
                            print( " ACCOUNT DELETED SUCCESSFULLY !!! " )
                            print()
                            break
                        
                        else :
                            break

                except :
                    print( Fore.RED + " PLEASE ENTER A NUMERIICAL VALUE !!! " )
                    print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                    print( Style.RESET_ALL )
                    print()
                    continue

        else :
            break



def PASSWORD_CREATION( USERNAME ) :
    
    while True :
        try :
            print( Fore.GREEN )
            print( Style.BRIGHT )

            print()
            
            print( " CONDITIONS FOR REQUIRED PASSWORD . " )
            
            print()
            
            print()
            
            print( " PASSWORD MUST CONTAIN ATLEAST 8 CHARACTERS . " )

            print()

            print( " PASSWORD MUST NOT CONTAIN ANY BLANK SPACE . " )

            print()
            
            print( " PASSWORD MUST CONTAIN LOWER CASE ALPHABET . " )

            print()
            
            print( " PASSWORD MUST CONTAIN UPPER CASE ALPHABET . " )

            print()
            
            print( " PASSWORD MUST CONTAIN DIGIT . " )

            print()
            
            print( " PASSWORD MUST CONTAIN SPECIAL CHARACTER . "  )

            print()
            
            print( " PASSWORD MUST NOT BE AS SAME AS USERNAME . " )

            print()
            print()
            print( Style.RESET_ALL )

            TRY_PASSWORD = input( " PLEASE ENTER YOUR PASSWORD : " )
            print()
            
            RETRY_PASSWORD = input( " PLEASE RE-TYPE YOUR PASSWORD : " )
            print()
            
            if ( TRY_PASSWORD == RETRY_PASSWORD ) :
                
                FLAG1=0
                FLAG2=0
                FLAG3=0
                FLAG4=0
                FLAG5=0
                
                USERNAME_CHECKING = USERNAME.upper()
                TRY_PASSWORD_CHECKING = TRY_PASSWORD.upper()
                CHECKING = TRY_PASSWORD_CHECKING.__contains__( USERNAME_CHECKING )
                
                if ( CHECKING == False ) :
                    if ( len( TRY_PASSWORD ) >= 8 ) :
                        for ELEMENT in TRY_PASSWORD :
                            if ELEMENT == " " :
                                FLAG1=1
                                
                            if chr(97) <= ELEMENT <= chr(122) :
                                FLAG2 += 1
                                
                            if  chr(65) <= ELEMENT <= chr(90) :
                                FLAG3 += 1
                                
                            if  chr(48) <= ELEMENT <= chr(57)  :
                                FLAG4 += 1
                                
                            if  chr(33) <= ELEMENT <= chr(47) or chr(58) <= ELEMENT <= chr(64) or chr(91) <= ELEMENT <= chr(96) or chr(123) <= ELEMENT <= chr(126) :
                                FLAG5 += 1

                        if (  FLAG1 == 0 and FLAG2 >= 1 and FLAG3 >= 1 and FLAG4 >= 1 and FLAG5 >= 1 ) :
                            TEMP_PASSWORD = TRY_PASSWORD
                            return TEMP_PASSWORD
                            break
                            
                        else :
                            print( Fore.RED + " INVALID PASSWORD !!! " )
                            print( Fore.RED + " YOUR PASSWORD DOESN'T FULFILL ALL THE CONDITIONS MENTIONED ABOVE !!! " )
                            print( Style.RESET_ALL )
                            print()
                            continue

                    else:
                        print( Fore.RED + " INVALID PASSWORD !!! " )
                        print( Fore.RED + " YOU HAVE ENTERED A PASSWORD OF LESS THAN 8 CHARACTER !!! " )
                        print( Style.RESET_ALL )
                        print()
                        continue
                else :
                    print( Fore.RED + " INVALID PASSWORD !!! " )
                    print( Fore.RED + " YOU CAN'T HAVE A PASSWORD SIMILAR TO YOUR USERNAME !!! " )
                    print( Style.RESET_ALL )
                    print()
                    continue
                    
            else :
                print( Fore.RED + " YOUR PASSWORD AND RE-TYPED PASSWORD DOESN'T MATCH !!! " )
                print( Style.RESET_ALL )
                print()
                continue

        except :
             print( Fore.RED + " PLEASE TRY AGAIN !!! " )
             print( Style.RESET_ALL )
             print()
             continue
    

            
def CAPTCHA() :

    while True :
        for ATTEMPTS in range(0,4,1) :
            CAPTCHA1 = random.randint(100,999)
            CAPTCHA2 = random.randint(100,999)
            SUM = CAPTCHA1 + CAPTCHA2
            SATISFY = 0
            
            try :
                print()
                print( " TO CONTINUE PLEASE VALIDATE THE FOLLOWING CAPTCHA " )
                print()
                print( " THE NUMBERS ARE " , CAPTCHA1 , "+"  , CAPTCHA2 , "." )
                print()
                INPUT_SUM = int ( eval ( input( " PLEASE ENTER THE SUM OF TWO NUMBERS BEING DISPLAYED ON YOUR SCREEN HERE : " ) ) )
                print()
                if ( SUM == INPUT_SUM ) :
                    SATISFY = 1
                    print()
                    break
                
                else :
                    print( Fore.RED + " INVALID INPUT !!! " )
                    print( Fore.RED + " PLEASE TRY AGAIN !!! " )
                    print( Style.RESET_ALL )
                    SATISFY = -1
                    print()
                    continue

            except :
                print( Fore.RED + " PLEASE ENTER A NUMERICAL VALUE !!! " )
                print( Fore.RED + " HENCE, PLEASE TRY AGAIN !!! " )
                print( Style.RESET_ALL )
                print()
                continue
            
        if ( SATISFY == -1 ) :
            print( Fore.RED + " YOUR TRIALS ARE OVER !!! " )
            print( Fore.RED + " PLEASE TRY AGAIN AFTER SOME TIME !!! " )
            print( Style.RESET_ALL )
            print()
            return False
        
        else :
            return True



def GREETINGS() :
    
    TIME_NOW = datetime.datetime.now()
    TIME_HOUR = TIME_NOW.hour
    
    if 0 <= TIME_HOUR < 12:
       GREETINGS = " GOOD MORNING "
       
    elif 12 <= TIME_HOUR < 18:
       GREETINGS = " GOOD AFTERNOON "
       
    else :
        GREETINGS = " GOOD EVENING"
        
    return GREETINGS



CREATE_DATABASE_RAILWAY_RESERVATION_SYSTEM()
CONNECTION()
USE_DATABASE_RAILWAY_RESERVATION_SYSTEM()

TABLE_CREATION()
MENU()
