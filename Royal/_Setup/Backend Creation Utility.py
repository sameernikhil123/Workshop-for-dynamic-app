#import ctypes
#ctypes.windll.kernel32.SetConsoleTitleW("BACKEND SETUP UTILITY - ROYAL RETAILERS\' PVT LTD")
#print()

p = input('  Please enter your MySQL Password for this PC (case-sensitive)...     ')
print('\n'+'-'*80, end='\n\n')

import mysql.connector as sql
try:    
    con = sql.connect(host='localhost',user='root',passwd=p)
    cur = con.cursor()   
    print("\t\t   Welcome to MySQL Resetting/Creating Utility for \n\t\tRoyal Retailers' Invoice & Stock Management System!\n\n")
    print('-'*80, end='\n\n')
    print("    This utility will properly install or reset the BACKEND for our project. \n\n")
    print('\n'+'-'*80, end='\n\n')
    input('Please Press the Enter Key to Continue...[1 of 3]\n\n\n')
    input('If You are sure of your decision, Press the Enter Key to Continue...[2 of 3]\n\n\n')
    input('For the last time, Please Press the Enter Key to Continue...[3 of 3]\n\n\n')
    print('-'*80, end='\n\n')
    print('STARTING THE UTILITY NOW... THIS MAY TAKE SOME TIME. Please BE PATIENT.',end='\n\n\n')

    cur.execute('drop database if exists royal')
    con.commit()

    cur.execute('create database royal')
    con.commit()

    cur.execute('use royal')
    con.commit()

    cur.execute('create table items(Item_name varchar(35),Item_Code varchar(7),Stock integer)')
    con.commit()

    lst = ['Apple','Mango','Pineapple','Orange','Lemon','Banana','Grapes','Potato','Onion','Cauliflower',\
           'Carrot','Cabbage','Spinach','Peas','Tomato','Beans',]      
    dst = ['F101','F102','F103','F104','F105','F106','F107','V101','V102','V103','V104','V105','V106','V107','V108','V109']
    r=0
    for i in lst:
        a = "insert into items(Item_name,Item_Code,Stock) values('{}','{}',25)".format(i,dst[r])
        cur.execute(a)
        con.commit()
        r+=1

    cur.execute('create table invlisttable(Bill_No integer primary key, Bill_Date varchar(15),Amount bigint, Cus_Name varchar(20))')
    con.commit()

    cur.execute('create table purlisttable(Bill_No integer primary key, Bill_Date varchar(15),Amount bigint, Sel_Name varchar(20))')
    con.commit()

    cur.execute('create table customers(Cus_Name varchar(25), Cus_Phno bigint, Bill_No integer primary key,Date varchar(15),POS varchar(100),Address varchar(100))')
    con.commit()
    cur.execute('create table sellers(Sel_Name varchar(25), Sel_Phno bigint, Bill_No integer primary key,Date varchar(15),POS varchar(100),Address varchar(100))')
    con.commit()
    cur.execute('create table explisttable(Ref_No varchar(10) primary key, Exp_Date varchar(15),Amount bigint, Payment_type varchar(20),Exp_Name varchar(25))')
    con.commit()
    print('.'*6)
    print('Successfully created a new Backend for this PC. Removed Old if existed earlier.')
    print('Yay! Done! MySQL Backend is ready for use again!')
    input('Press enter key to exit.')  
except:
    print('The Password entered above is incorrect for the MySQL in this PC.\n\nPlease Restart the utility.\n')
    input('Press enter key to exit.')









