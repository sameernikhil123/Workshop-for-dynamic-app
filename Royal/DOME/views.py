




#-------------------------------------------------------------------------------
#          For The User-end; Django Folder Path and Login Configuration

django_folder_path = '//Users//vishwanathkurella//Desktop//django' #Write in a similar fashion
your_mysql_password = 'Vit@event21' 


Login_Username = 'admin'
Login_Password = 'pass'

#                       DO NOT EDIT ANYTHING BELOW THIS LINE
#--------------------------------------------------------------------------------







#                             For the Developer-end

from django.shortcuts import render

                          #MYSQL CONFIGURATION SECTION

import mysql.connector as sql
mpass = your_mysql_password
con = sql.connect(host='localhost',user='root',passwd=mpass,database='royal')
cur = con.cursor(buffered=True)

                    #Django Retrieval Path CONFIGURATION SECTION

djpath = django_folder_path + '//Royal//web//' 
djpathv1= djpath + 'temp_mysql_invlist.html'
djpathv2 = djpath + 'temp_mysql_purlist.html'
djpathv3 = djpath + 'temp_mysql_explist.html' 
djpathv4 = djpath + 'temp_mysql_itemlistwindow.html'
djpathe1 = djpath + 'edit_mysql_inv.html'
djpathe2 = djpath + 'edit_mysql_pur.html'
djpathe3 = djpath + 'edit_mysql_exp.html'
djpathex1 = djpath + 'export_inv.html'
exportpath = django_folder_path + '//Royal//ExportedInvoices//'
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                #BASIC
                        
global logincache
logincache = {0:0}

def ltc(req):                   
    return render(req,'logintocontinue.html')
    
def login(req):          
    return render(req,'loginpage.html')
    
def logout(req):
    logincache[0] = 0
    return render(req,'logout.html')

def validate(req):                                                          
    if req.POST['lo_user'] == Login_Username and req.POST['pas'] == Login_Password:
        logincache[0] = 1
        return render(req,'portal.html')
    else:
        return render(req, 'loginfailed.html')

def portal(req):
    if logincache[0] == 1:
        return render(req,'portal.html')
    else:
        return render(req,'logintocontinue.html')

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                               #INVOICING

                                                        #Creating Invoice and Inserting into all Invoice related tables 

def newinvoice(req):
    if logincache[0] == 1:
        return render(req,'newinv.html')  
    else:
        return render(req,'logintocontinue.html')

def invoice(req):
    if logincache[0] == 1:
        if len(req.POST["cph"]) == 10 and intcheck(req.POST["cph"]):
            if intcheck(req.POST['bill_no']):
                if unique_new_inv_no(req.POST["bill_no"]):
                    try:
                        iti = "insert into customers(Cus_Name, Cus_Phno, Bill_No,Date,POS,Address)\
                               values('{}',{},{},'{}','{}','{}')".format(req.POST["cname"],req.POST["cph"],\
                                                                         req.POST["bill_no"],req.POST["bdate"],
                                                                         req.POST["pos"],req.POST["cadd"])     
                        cur.execute(iti)                                                                                
                        con.commit()                                                                            

                        a = req.POST["bill_no"]
                        sub1 = req.POST["qty1"]
                        sub2 = req.POST["qty2"]
                        sub3 = req.POST["qty3"]
                        sub4 = req.POST["qty4"]
                        sub5 = req.POST["qty5"]
                        sub6 = req.POST["qty6"]
                        sub7 = req.POST["qty7"]

                        ct = "create table sale_no_{}(Item_Code varchar(7) primary key not null,Quantity integer, Rate integer, Tax integer, Amount integer)".format(a)

                        st1 = "insert into sale_no_{}(Item_Code,Quantity,Rate,Tax,Amount)\
                               values('{}',{},{},{},{})".format(a,req.POST["item1"],req.POST["qty1"],\
                                                                req.POST["rate1"],req.POST["tax1"],\
                                                                req.POST["amt1"])
                        
                        st2 = "insert into sale_no_{}(Item_Code,Quantity,Rate,Tax,Amount)\
                               values('{}',{},{},{},{})".format(a,req.POST["item2"],req.POST["qty2"],\
                                                                req.POST["rate2"],req.POST["tax2"],\
                                                                req.POST["amt2"])
                        
                        st3 = "insert into sale_no_{}(Item_Code,Quantity,Rate,Tax,Amount)\
                               values('{}',{},{},{},{})".format(a,req.POST["item3"],req.POST["qty3"],\
                                                                 req.POST["rate3"],req.POST["tax3"],\
                                                                 req.POST["amt3"])
                        
                        st4 = "insert into sale_no_{}(Item_Code,Quantity,Rate,Tax,Amount)\
                               values('{}',{},{},{},{})".format(a,req.POST["item4"],req.POST["qty4"],\
                                                                req.POST["rate4"],req.POST["tax4"],\
                                                                req.POST["amt4"])
                        
                        st5 = "insert into sale_no_{}(Item_Code,Quantity,Rate,Tax,Amount)\
                               values('{}',{},{},{},{})".format(a,req.POST["item5"],req.POST["qty5"],\
                                                                req.POST["rate5"],req.POST["tax5"],\
                                                                req.POST["amt5"])
                        
                        st6 = "insert into sale_no_{}(Item_Code,Quantity,Rate,Tax,Amount)\
                               values('{}',{},{},{},{})".format(a,req.POST["item6"],req.POST["qty6"],\
                                                                req.POST["rate6"],req.POST["tax6"],\
                                                                req.POST["amt6"])
                        
                        st7 = "insert into sale_no_{}(Item_Code,Quantity,Rate,Tax,Amount)\
                               values('{}',{},{},{},{})".format(a,req.POST["item7"],req.POST["qty7"],\
                                                                req.POST["rate7"],req.POST["tax7"],\
                                                                req.POST["amt7"])
                        cur.execute(ct)
                        con.commit()

                        if req.POST['item1'] != '':
                            cur.execute(st1)
                            con.commit()
                        if req.POST['item2'] != '':
                            cur.execute(st2)
                            con.commit()
                        if req.POST['item3'] != '':
                            cur.execute(st3)
                            con.commit()
                        if req.POST['item4'] != '':
                            cur.execute(st4)
                            con.commit()
                        if req.POST['item5'] != '':
                            cur.execute(st5)
                            con.commit()
                        if req.POST['item6'] != '':
                            cur.execute(st6)
                            con.commit()
                        if req.POST['item7'] != '':
                            cur.execute(st7)
                            con.commit()

                        if req.POST["item1"] !='':
                            if itemexists(req.POST['item1']):
                                cal1 = "select stock from items where Item_Code='{}'".format(req.POST["item1"])
                                row1 = cur.execute(cal1)
                                rows1 = cur.fetchall()
                                for row1 in rows1:
                                    i = row1    
                                s1 = cur.execute("select stock from items")
                                for s1 in i:
                                    stk1 = s1
                                dif1 = int(sub1)
                                sum1 = stk1 - dif1
                                fcal1 = "update items set stock={} where Item_Code='{}'".format(sum1,req.POST["item1"])
                                cur.execute(fcal1)
                                con.commit()
                            else:
                                raise NameError 

                        if req.POST["item2"] !='':
                            if itemexists(req.POST['item2']):
                                cal2 = "select stock from items where Item_Code='{}'".format(req.POST["item2"])
                                row2 = cur.execute(cal2)
                                rows2 = cur.fetchall()
                                for row2 in rows2:
                                    i = row2    
                                s1 = cur.execute("select stock from items")
                                for s2 in i:
                                    stk2 = s2
                                dif2 = int(sub2)
                                sum2 = stk2 - dif2
                                fcal2 = "update items set stock={} where Item_Code='{}'".format(sum2,req.POST["item2"])
                                cur.execute(fcal2)
                                con.commit()
                            else:
                                raise NameError 
           
                        if req.POST["item3"] !='':
                            if itemexists(req.POST['item3']):
                                cal3 = "select stock from items where Item_Code='{}'".format(req.POST["item3"])
                                row3 = cur.execute(cal3)
                                rows3 = cur.fetchall()
                                for row3 in rows3:
                                    i = row3    
                                s3 = cur.execute("select stock from items")
                                for s3 in i:
                                    stk3 = s3
                                dif3 = int(sub3)
                                sum3 = stk3 - dif3
                                fcal3 = "update items set stock={} where Item_Code='{}'".format(sum3,req.POST["item3"])
                                cur.execute(fcal3)
                                con.commit() 
                            else:
                                raise NameError 

                        if req.POST["item4"] !='':
                            if itemexists(req.POST['item4']):
                                cal4 = "select stock from items where Item_Code='{}'".format(req.POST["item4"])
                                row4 = cur.execute(cal4)
                                rows4 = cur.fetchall()
                                for row4 in rows4:
                                    i = row4  
                                s4 = cur.execute("select stock from items")
                                for s4 in i:
                                    stk4 = s4
                                dif4 = int(sub4)
                                sum4 = stk4 - dif4
                                fcal4 = "update items set stock={} where Item_Code='{}'".format(sum4,req.POST["item4"])
                                cur.execute(fcal4)
                                con.commit()
                            else:
                                raise NameError 
                                
                        if req.POST["item5"] !='':
                            if itemexists(req.POST['item5']):
                                cal5 = "select stock from items where Item_Code='{}'".format(req.POST["item5"])
                                row5 = cur.execute(cal5)
                                rows5 = cur.fetchall()
                                for row5 in rows5:
                                    i = row5    
                                s5 = cur.execute("select stock from items")
                                for s5 in i:
                                    stk5 = s5
                                dif5 = int(sub5)
                                sum5 = stk5 - dif5
                                fcal5 = "update items set stock={} where Item_Code='{}'".format(sum5,req.POST["item5"])
                                cur.execute(fcal5)
                                con.commit()    
                            else:
                                raise NameError 

                        if req.POST["item6"] !='':
                            if itemexists(req.POST['item6']):
                                cal6 = "select stock from items where Item_Code='{}'".format(req.POST["item6"])
                                row6 = cur.execute(cal6)
                                rows6 = cur.fetchall()
                                for row6 in rows6:
                                    i = row6   
                                s6 = cur.execute("select stock from items")
                                for s6 in i:
                                    stk6 = s6
                                dif6 = int(sub6)
                                sum6 = stk6 - dif6
                                fcal6 = "update items set stock={} where Item_Code='{}'".format(sum6,req.POST["item6"])
                                cur.execute(fcal6)
                                con.commit()    
                            else:
                                raise NameError 

                        if req.POST["item7"] !='':
                            if itemexists(req.POST['item7']):
                                cal7 = "select stock from items where Item_Code='{}'".format(req.POST["item7"])
                                row7 = cur.execute(cal7)
                                rows7 = cur.fetchall()
                                for row7 in rows7:
                                    i = row7    
                                s7 = cur.execute("select stock from items")
                                for s7 in i:
                                    stk7 = s7
                                dif7 = int(sub7)
                                sum7 = stk7 - dif7
                                fcal7 = "update items set stock={} where Item_Code='{}'".format(sum7,req.POST["item7"])
                                cur.execute(fcal7)
                                con.commit()
                            else:
                                raise NameError 

                        ilt = "insert into invlisttable(Bill_No, Bill_Date,Amount,Cus_Name)\
                               values({},'{}',{},'{}')".format(req.POST["bill_no"],req.POST["bdate"],\
                                                               req.POST["bill_amt"],req.POST["cname"])
                        cur.execute(ilt)                                                                
                        con.commit()
                        return render(req,'salesavedsuccessfully.html')
                                      
                    except NameError:
                        cur.execute("delete from invlisttable where bill_no = {}".format(req.POST["bill_no"]))
                        con.commit()
                        cur.execute("drop table if exists sale_no_{}".format(req.POST["bill_no"]))
                        con.commit()
                        cur.execute("delete from customers where bill_no = {}".format(req.POST["bill_no"]))
                        con.commit()
                        if req.POST["item1"] !='':
                            if itemexists(req.POST['item1']):
                                cal1 = "select stock from items where Item_Code='{}'".format(req.POST["item1"])
                                row1 = cur.execute(cal1)
                                rows1 = cur.fetchall()
                                for row1 in rows1:
                                    i = row1    
                                s1 = cur.execute("select stock from items")
                                for s1 in i:
                                    stk1 = s1
                                dif1 = int(sub1)
                                sum1 = stk1 + dif1
                                fcal1 = "update items set stock={} where Item_Code='{}'".format(sum1,req.POST["item1"])
                                cur.execute(fcal1)
                                con.commit()
                           
                        if req.POST["item2"] !='':
                            if itemexists(req.POST['item2']):
                                cal2 = "select stock from items where Item_Code='{}'".format(req.POST["item2"])
                                row2 = cur.execute(cal2)
                                rows2 = cur.fetchall()
                                for row2 in rows2:
                                    i = row2    
                                s1 = cur.execute("select stock from items")
                                for s2 in i:
                                    stk2 = s2
                                dif2 = int(sub2)
                                sum2 = stk2 + dif2
                                fcal2 = "update items set stock={} where Item_Code='{}'".format(sum2,req.POST["item2"])
                                cur.execute(fcal2)
                                con.commit()
                           
                        if req.POST["item3"] !='':
                            if itemexists(req.POST['item3']):
                                cal3 = "select stock from items where Item_Code='{}'".format(req.POST["item3"])
                                row3 = cur.execute(cal3)
                                rows3 = cur.fetchall()
                                for row3 in rows3:
                                    i = row3    
                                s3 = cur.execute("select stock from items")
                                for s3 in i:
                                    stk3 = s3
                                dif3 = int(sub3)
                                sum3 = stk3 + dif3
                                fcal3 = "update items set stock={} where Item_Code='{}'".format(sum3,req.POST["item3"])
                                cur.execute(fcal3)
                                con.commit() 
                           

                        if req.POST["item4"] !='':
                            if itemexists(req.POST['item4']):
                                cal4 = "select stock from items where Item_Code='{}'".format(req.POST["item4"])
                                row4 = cur.execute(cal4)
                                rows4 = cur.fetchall()
                                for row4 in rows4:
                                    i = row4  
                                s4 = cur.execute("select stock from items")
                                for s4 in i:
                                    stk4 = s4
                                dif4 = int(sub4)
                                sum4 = stk4 + dif4
                                fcal4 = "update items set stock={} where Item_Code='{}'".format(sum4,req.POST["item4"])
                                cur.execute(fcal4)
                                con.commit()
                                
                        if req.POST["item5"] !='':
                            if itemexists(req.POST['item5']):
                                cal5 = "select stock from items where Item_Code='{}'".format(req.POST["item5"])
                                row5 = cur.execute(cal5)
                                rows5 = cur.fetchall()
                                for row5 in rows5:
                                    i = row5    
                                s5 = cur.execute("select stock from items")
                                for s5 in i:
                                    stk5 = s5
                                dif5 = int(sub5)
                                sum5 = stk5 + dif5
                                fcal5 = "update items set stock={} where Item_Code='{}'".format(sum5,req.POST["item5"])
                                cur.execute(fcal5)
                                con.commit()    
                           
                        if req.POST["item6"] !='':
                            if itemexists(req.POST['item6']):
                                cal6 = "select stock from items where Item_Code='{}'".format(req.POST["item6"])
                                row6 = cur.execute(cal6)
                                rows6 = cur.fetchall()
                                for row6 in rows6:
                                    i = row6   
                                s6 = cur.execute("select stock from items")
                                for s6 in i:
                                    stk6 = s6
                                dif6 = int(sub6)
                                sum6 = stk6 + dif6
                                fcal6 = "update items set stock={} where Item_Code='{}'".format(sum6,req.POST["item6"])
                                cur.execute(fcal6)
                                con.commit()    
                            
                        if req.POST["item7"] !='':
                            if itemexists(req.POST['item7']):
                                cal7 = "select stock from items where Item_Code='{}'".format(req.POST["item7"])
                                row7 = cur.execute(cal7)
                                rows7 = cur.fetchall()
                                for row7 in rows7:
                                    i = row7    
                                s7 = cur.execute("select stock from items")
                                for s7 in i:
                                    stk7 = s7
                                dif7 = int(sub7)
                                sum7 = stk7 + dif7
                                fcal7 = "update items set stock={} where Item_Code='{}'".format(sum7,req.POST["item7"])
                                cur.execute(fcal7)
                                con.commit()                                
                    
                    return render(req,'inc.html')
                
                else:
                    return render(req,'existingbillno.html') 
            else:
                return render(req,'bnc.html')
        else:
            return render(req, 'phnc.html')
    else:
        return render(req,'logintocontinue.html')
                                        #--------------------------Viewing All Invoices--------------------------------

def tempinvlist(req):
    if logincache[0] == 1:
        return render(req,'tempinvlist.html')
    else:
        return render(req,'logintocontinue.html')

def generateinvlist(req):
    if logincache[0] == 1:
        cur.execute('select * from invlisttable')
        data = cur.fetchall()
        try:
            vtop1()
            for row in data:
                file01 = open(djpathv1, mode='a+')
                for s in range(0,4):
                    if s == 0:
                        d = '<tr><td>' + str(row[s]) + '</td><td>'
                        file01.writelines(d)
                    if s == 1 or s == 2:
                        d = str(row[s]) + '</td><td>'
                        file01.writelines(d)
                    if s == 3:
                        d = str(row[s]) + '</td></tr>\n'
                        file01.writelines(d)
            file01.close()
            vbot1()
            return render(req,'temp_mysql_invlist.html')
        except:
            return render(req,'nodata.html')
    else:
        return render(req,'logintocontinue.html')
                                           #----------------------------Editing Invoices--------------------------------

def editinv(req):
    if logincache[0] == 1:
        return render(req,'editinvoice.html')
    else:
        return render(req,'logintocontinue.html')

def inveditor(req):
    b = req.POST['bill_no']          
    cur.execute('select * from customers where Bill_No = {}'.format(b))
    data = cur.fetchall()
    etop1()
    for k in data:
        file01 = open(djpathe1, mode='a+')
        file01.writelines("Customer Name: &nbsp;<input type='text' class='mi_field' name='cname' maxlength='20' value='{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(k[0]))       
        file01.writelines("Customer Ph No.: &nbsp;<input type='text' class='mi_field' name='cph' maxlength='13' value='{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(k[1]))       
        file01.writelines("Bill No.:&nbsp; <input type='text' class='mi_mi_field' name='bill_no' maxlength='7' value='{}' readonly/><br/><br/>\n".format(k[2]))
        file01.writelines("Place of Supply:&nbsp;&nbsp;&nbsp; <input type='text' class='mi_field' name='pos' maxlength='20' value='{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(k[4]))    
        file01.writelines("Customer Address: &nbsp;&nbsp;<input type='text' class='ma_field' name='cadd' maxlength='100' value='{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(k[5]))
        file01.writelines("Date:&nbsp;&nbsp; <input type='text' name='bdate' class = 'mi_mi_field' value='{}' readonly/><br/>&nbsp;<br/><br/>&nbsp;\n".format(k[3]))
        file01.writelines("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
        file01.writelines("Item Code: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Qty: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rate (in Rs.): &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tax Rate(%): &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Amount (in Rs.): <br/><br/>\n")

    cur.execute('select * from sale_no_{}'.format(b))
    d = cur.fetchall()
    s = len(d)
    cur.execute('select * from sale_no_{}'.format(b))
    for g in range(1,s+1):
        y = cur.fetchone()
        f = str(g)
        i = 'item' + f
        q= 'qty' + f
        r = 'rate' + f
        t = 'tax' + f
        am = 'amt' + f
        cal = 'cal' + f + '();'
        iq  = 'q' + f
        it = 'tar'+ f
        ir = 'r'+ f
        file01.writelines("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
        file01.writelines("<input type='text' class='item'  name='{}' value='{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(i,y[0],cal))
        file01.writelines("<input type='text' class='qty' name='{}' value='{}' onblur='{}' id = '{}'/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(q,y[1],cal,iq))
        file01.writelines("<input type='text' class='qty' name='{}' value='{}' onblur='{}' id = '{}'/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(r,y[2],cal,ir))
        file01.writelines("<input type='number' class='qty' name='{}' value='{}' onblur='{}' id = '{}'/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(t,y[3],cal,it))
        file01.writelines("<input type='text' class='amt' onblur='findTotal()' name='{}' value='{}' onblur='{}' id = '{}'/><br/><br/>\n\n".format(am,y[4],cal,am))
    file01.close()
    ebot1()
    return render (req,'edit_mysql_inv.html')

def updateinvsave(req):
    
    cur.execute('select * from sale_no_{}'.format(req.POST["bill_no"]))
    d = cur.fetchall()
    s = len(d)
    for g in range(1,s+1):
        f = str(g)
        it = 'item' + f
        q = 'qty' + f
        fed = "select Quantity from sale_no_{} where Item_Code='{}'".format(req.POST["bill_no"],req.POST[it])
        row = cur.execute(fed)
        rows = cur.fetchall()
        for row in rows:
            i = row    
            qt = cur.execute("select Quantity from sale_no_{}".format(req.POST["bill_no"]))
        for z in i:
            qt = z
        sub = req.POST[q]    
        dif = int(sub)
        if dif > qt:
            sums = dif - qt
            cal = "select stock from items where Item_Code='{}'".format(req.POST[it])
            rem = cur.execute(cal)
            rems = cur.fetchall()
            for rem in rems:
                j = rem    
                m = cur.execute("select stock from items")
            for m in j:
                stk = m
            fsum = stk - sums
            fcal = "update items set stock={} where Item_Code='{}'".format(fsum,req.POST[it])
            cur.execute(fcal)
            con.commit()
        else:
            sums = qt - dif
            cal = "select stock from items where Item_Code='{}'".format(req.POST[it])
            rem = cur.execute(cal)
            rems = cur.fetchall()
            for rem in rems:
                j = rem    
                m = cur.execute("select stock from items")
            for m in j:
                stk = m
            fsum = stk + sums
            fcal = "update items set stock={} where Item_Code='{}'".format(fsum,req.POST[it])
            cur.execute(fcal)
            con.commit()
            
               
    cur.execute('select * from sale_no_{}'.format(req.POST["bill_no"]))
    d = cur.fetchall()
    s = len(d)
    for g in range(1,s+1):
        f = str(g)
        i = 'item' + f
        q = 'qty' + f
        r = 'rate' + f
        t = 'tax' + f
        am = 'amt' + f
        cal = 'cal' + f + '();'
        iq  = 'q' + f
        it = 'tar'+ f
        ir = 'r'+ f 
        ut = "update sale_no_{} set Quantity={},Rate={},Tax={},Amount={} where Item_Code='{}'".format(req.POST["bill_no"],req.POST[q],req.POST[r],\
                                                                                                       req.POST[t],req.POST[am],req.POST[i])
        cur.execute(ut)
        con.commit()
    tb = "update invlisttable set Amount = {} where Bill_No = {}".format(req.POST["bill_amt"],req.POST["bill_no"])
    cur.execute(tb)
    con.commit()
    
    return render(req,"salesavedsuccessfully.html")
                                        #--------------------------------Exporting Invoice----------------------------------

def exportinv(req):
    if logincache[0] == 1:
        return render(req,'exportinvoice.html')
    else:
        return render(req,'logintocontinue.html')

def invexporter(req):
    b = req.POST['bill_no']          
    cur.execute('select * from customers where Bill_No = {}'.format(b))
    data = cur.fetchall()
    extop1()
    for k in data:
        file01 = open(djpathex1, mode='a+')
        file01.writelines("Customer Name: &nbsp;<input type='text' class='mi_field' name='cname' maxlength='20' value='{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(k[0]))       
        file01.writelines("Customer Ph No.: &nbsp;<input type='text' class='mi_field' name='cph' maxlength='13' value='{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(k[1]))       
        file01.writelines("Bill No.:&nbsp; <input type='text' class='mi_mi_field' name='bill_no' maxlength='7' value='{}' readonly/><br/><br/>\n".format(k[2]))
        file01.writelines("Place of Supply:&nbsp;&nbsp;&nbsp; <input type='text' class='mi_field' name='pos' maxlength='20' value='{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(k[4]))    
        file01.writelines("Customer Address: &nbsp;&nbsp;<input type='text' class='ma_field' name='cadd' maxlength='100' value='{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(k[5]))
        file01.writelines("Date:&nbsp;&nbsp; <input type='text' name='bdate' class = 'mi_mi_field' value='{}' readonly/><br/>&nbsp;<br/><br/>&nbsp;\n".format(k[3]))
        file01.writelines("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
        file01.writelines("Item Code: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Qty: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rate (in Rs.): &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tax Rate(%): &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Amount (in Rs.): <br/><br/>\n")

    cur.execute('select * from sale_no_{}'.format(b))
    d = cur.fetchall()
    s = len(d)
    cur.execute('select * from sale_no_{}'.format(b))
    for g in range(1,s+1):
        y = cur.fetchone()
        f = str(g)
        i = 'item' + f
        q= 'qty' + f
        r = 'rate' + f
        t = 'tax' + f
        am = 'amt' + f
        cal = 'cal' + f + '();'
        iq  = 'q' + f
        it = 'tar'+ f
        ir = 'r'+ f
        file01.writelines("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
        file01.writelines("<input type='text' class='item'  name='{}' value='{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(i,y[0],cal))
        file01.writelines("<input type='text' class='qty' name='{}' value='{}' onblur='{}' id = '{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(q,y[1],cal,iq))
        file01.writelines("<input type='text' class='qty' name='{}' value='{}' onblur='{}' id = '{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(r,y[2],cal,ir))
        file01.writelines("<input type='number' class='qty' name='{}' value='{}' onblur='{}' id = '{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(t,y[3],cal,it))
        file01.writelines("<input type='text' class='amt' onblur='findTotal()' name='{}' value='{}' onblur='{}' id = '{}' readonly/><br/><br/>\n\n".format(am,y[4],cal,am))
    file01.close()
    exbot1()
    return render (req,'export_inv.html')

def billing(req):
    b = req.POST['bill_no']
    cur.execute('select * from sale_no_{}'.format(b))
    d = cur.fetchall()
    s = len(d)
    cur.execute('select * from sale_no_{}'.format(b))
    ta = 0
    extop2(req.POST["filename"],req.POST["bdate"],req.POST["cname"],req.POST["cph"],req.POST["cadd"],req.POST["bill_no"])
    b = exportpath + req.POST["filename"] + '.txt'
    for g in range(1,s+1):
        y = cur.fetchone()
        f = str(g)
        i = 'item' + f
        q= 'qty' + f
        r = 'rate' + f
        t = 'tax' + f
        am = 'amt' + f
        cur.execute("select Item_name from items where Item_Code ='{}'".format(req.POST[i]))
        name = cur.fetchall()
        for n in name:
            file01 = open(b, mode='a+')
            file01.writelines('\n\t{}\t\t\t\t\t{}\t\t{}\t{}\t{}'.format(n[0],req.POST[q],req.POST[r],req.POST[t],req.POST[am]))
            ta += int(req.POST[am])
            file01.close()
    file01 = open(b, mode='a+')
    c = '\n'+'-'*120
    file01.write('{}'.format(c))
    file01.write('\n\tTotal amount:\t\t\t\t\t\t\t\tRs.{}'.format(ta))
    file01.close()
    return render (req,'ies.html')                                         
                        

#----------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                        #PURCHASE CENTRE

                                                   #Creating Purchases and Inserting into all Purchase ralated tables       

def newpurchase(req):
    if logincache[0] == 1:
        return render(req,'newpur.html')
    else:
        return render(req,'logintocontinue.html')
        
def purchase(req):
    if logincache[0] == 1:
        if len(req.POST["sph"]) == 10 and intcheck(req.POST["sph"]):
            if intcheck(req.POST['bill_no']) and unique_new_pur_no(req.POST["bill_no"]):
                try:
                    ptc = "insert into sellers(Sel_Name, Sel_Phno, Bill_No,Date,POS,Address)\
                           values('{}',{},{},'{}','{}','{}')".format(req.POST["sname"],req.POST["sph"],\
                                                                     req.POST["bill_no"],req.POST["bdate"],
                                                                     req.POST["pos"],req.POST["sadd"])     
                    cur.execute(ptc)
                    con.commit()

                    a = req.POST["bill_no"]
                    sub1 = req.POST["qty1"]
                    sub2 = req.POST["qty2"]
                    sub3 = req.POST["qty3"]
                    sub4 = req.POST["qty4"]
                    sub5 = req.POST["qty5"]
                    sub6 = req.POST["qty6"]
                    sub7 = req.POST["qty7"]

                    ct = "create table pur_no_{}(Item_Code varchar(50),Quantity integer, Rate integer, Tax integer, Amount integer)".format(a)

                    st1 = "insert into pur_no_{}(Item_Code,Quantity,Tax,Rate,Amount)\
                           values('{}',{},{},{},{})".format(a,req.POST["item1"],req.POST["qty1"],\
                                                            req.POST["tax1"],req.POST["rate1"],\
                                                            req.POST["amt1"])
                    
                    st2 = "insert into pur_no_{}(Item_Code,Quantity,Tax,Rate,Amount)\
                           values('{}',{},{},{},{})".format(a,req.POST["item2"],req.POST["qty2"],\
                                                            req.POST["tax2"],req.POST["rate2"],\
                                                            req.POST["amt2"])
                    
                    st3 = "insert into pur_no_{}(Item_Code,Quantity,Tax,Rate,Amount)\
                           values('{}',{},{},{},{})".format(a,req.POST["item3"],req.POST["qty3"],\
                                                            req.POST["tax3"],req.POST["rate3"],\
                                                            req.POST["amt3"])
                    
                    st4 = "insert into pur_no_{}(Item_Code,Quantity,Tax,Rate,Amount)\
                           values('{}',{},{},{},{})".format(a,req.POST["item4"],req.POST["qty4"],\
                                                            req.POST["tax4"],req.POST["rate4"],\
                                                            req.POST["amt4"])
                    
                    st5 = "insert into pur_no_{}(Item_Code,Quantity,Tax,Rate,Amount)\
                           values('{}',{},{},{},{})".format(a,req.POST["item5"],req.POST["qty5"],\
                                                            req.POST["tax5"],req.POST["rate5"],\
                                                            req.POST["amt5"])
                    
                    st6 = "insert into pur_no_{}(Item_Code,Quantity,Tax,Rate,Amount)\
                           values('{}',{},{},{},{})".format(a,req.POST["item6"],req.POST["qty6"],\
                                                            req.POST["tax6"],req.POST["rate6"],\
                                                            req.POST["amt6"])
                    
                    st7 = "insert into pur_no_{}(Item_Code,Quantity,Tax,Rate,Amount)\
                           values('{}',{},{},{},{})".format(a,req.POST["item7"],req.POST["qty7"],\
                                                            req.POST["tax7"],req.POST["rate7"],\
                                                            req.POST["amt7"])
                    cur.execute(ct)
                    con.commit()
                    if req.POST['item1'] != '':
                        cur.execute(st1)
                        con.commit()
                    if req.POST['item2'] != '':
                        cur.execute(st2)
                        con.commit()
                    if req.POST['item3'] != '':
                        cur.execute(st3)
                        con.commit()
                    if req.POST['item4'] != '':
                        cur.execute(st4)
                        con.commit()
                    if req.POST['item5'] != '':
                        cur.execute(st5)
                        con.commit()
                    if req.POST['item6'] != '':
                        cur.execute(st6)
                        con.commit()
                    if req.POST['item7'] != '':
                        cur.execute(st7)
                        con.commit()

                    if req.POST["item1"] !='':
                        if itemexists(req.POST['item1']):
                            cal1 = "select stock from items where Item_Code='{}'".format(req.POST["item1"])
                            row1 = cur.execute(cal1)
                            rows1 = cur.fetchall()
                            for row1 in rows1:
                                i = row1    
                            s1 = cur.execute("select stock from items")
                            for s1 in i:
                                stk1 = s1
                            dif1 = int(sub1)
                            sum1 = stk1 + dif1
                            fcal1 = "update items set stock={} where Item_Code='{}'".format(sum1,req.POST["item1"])
                            cur.execute(fcal1)
                            con.commit()
                        else:
                            raise NameError 

                    if req.POST["item2"] !='':
                        if itemexists(req.POST['item2']):
                            cal2 = "select stock from items where Item_Code='{}'".format(req.POST["item2"])
                            row2 = cur.execute(cal2)
                            rows2 = cur.fetchall()
                            for row2 in rows2:
                                i = row2    
                            s1 = cur.execute("select stock from items")
                            for s2 in i:
                                stk2 = s2
                            dif2 = int(sub2)
                            sum2 = stk2 + dif2
                            fcal2 = "update items set stock={} where Item_Code='{}'".format(sum2,req.POST["item2"])
                            cur.execute(fcal2)
                            con.commit()
                        else:
                            raise NameError 
       
                    if req.POST["item3"] !='':
                        if itemexists(req.POST['item3']):
                            cal3 = "select stock from items where Item_Code='{}'".format(req.POST["item3"])
                            row3 = cur.execute(cal3)
                            rows3 = cur.fetchall()
                            for row3 in rows3:
                                i = row3    
                            s3 = cur.execute("select stock from items")
                            for s3 in i:
                                stk3 = s3
                            dif3 = int(sub3)
                            sum3 = stk3 + dif3
                            fcal3 = "update items set stock={} where Item_Code='{}'".format(sum3,req.POST["item3"])
                            cur.execute(fcal3)
                            con.commit() 
                        else:
                            raise NameError 

                    if req.POST["item4"] !='':
                        if itemexists(req.POST['item4']):
                            cal4 = "select stock from items where Item_Code='{}'".format(req.POST["item4"])
                            row4 = cur.execute(cal4)
                            rows4 = cur.fetchall()
                            for row4 in rows4:
                                i = row4  
                            s4 = cur.execute("select stock from items")
                            for s4 in i:
                                stk4 = s4
                            dif4 = int(sub4)
                            sum4 = stk4 + dif4
                            fcal4 = "update items set stock={} where Item_Code='{}'".format(sum4,req.POST["item4"])
                            cur.execute(fcal4)
                            con.commit()
                        else:
                            raise NameError 
                            
                    if req.POST["item5"] !='':
                        if itemexists(req.POST['item5']):
                            cal5 = "select stock from items where Item_Code='{}'".format(req.POST["item5"])
                            row5 = cur.execute(cal5)
                            rows5 = cur.fetchall()
                            for row5 in rows5:
                                i = row5    
                            s5 = cur.execute("select stock from items")
                            for s5 in i:
                                stk5 = s5
                            dif5 = int(sub5)
                            sum5 = stk5 + dif5
                            fcal5 = "update items set stock={} where Item_Code='{}'".format(sum5,req.POST["item5"])
                            cur.execute(fcal5)
                            con.commit()    
                        else:
                            raise NameError 

                    if req.POST["item6"] !='':
                        if itemexists(req.POST['item6']):
                            cal6 = "select stock from items where Item_Code='{}'".format(req.POST["item6"])
                            row6 = cur.execute(cal6)
                            rows6 = cur.fetchall()
                            for row6 in rows6:
                                i = row6   
                            s6 = cur.execute("select stock from items")
                            for s6 in i:
                                stk6 = s6
                            dif6 = int(sub6)
                            sum6 = stk6 + dif6
                            fcal6 = "update items set stock={} where Item_Code='{}'".format(sum6,req.POST["item6"])
                            cur.execute(fcal6)
                            con.commit()    
                        else:
                            raise NameError 

                    if req.POST["item7"] !='':
                        if itemexists(req.POST['item7']):
                            cal7 = "select stock from items where Item_Code='{}'".format(req.POST["item7"])
                            row7 = cur.execute(cal7)
                            rows7 = cur.fetchall()
                            for row7 in rows7:
                                i = row7    
                            s7 = cur.execute("select stock from items")
                            for s7 in i:
                                stk7 = s7
                            dif7 = int(sub7)
                            sum7 = stk7 + dif7
                            fcal7 = "update items set stock={} where Item_Code='{}'".format(sum7,req.POST["item7"])
                            cur.execute(fcal7)
                            con.commit()
                        else:
                            raise NameError
                        
                    plt = "insert into purlisttable(Bill_No, Bill_Date,Amount,Sel_Name)\
                            values({},'{}',{},'{}')".format(req.POST["bill_no"],req.POST["bdate"],\
                                                           req.POST["bill_amt"],req.POST["sname"])
                    cur.execute(plt)                                                                
                    con.commit()  
                    return render(req,'purchasesavedsuccessfully.html')
                    
                except NameError:
                    cur.execute("delete from purlisttable where bill_no = {}".format(req.POST["bill_no"]))
                    con.commit()
                    cur.execute("drop table if exists pur_no_{}".format(req.POST["bill_no"]))
                    con.commit()
                    cur.execute("delete from sellers where bill_no = {}".format(req.POST["bill_no"]))
                    con.commit()
                    if req.POST["item1"] !='':
                        if itemexists(req.POST['item1']):
                            cal1 = "select stock from items where Item_Code='{}'".format(req.POST["item1"])
                            row1 = cur.execute(cal1)
                            rows1 = cur.fetchall()
                            for row1 in rows1:
                                i = row1    
                            s1 = cur.execute("select stock from items")
                            for s1 in i:
                                stk1 = s1
                            dif1 = int(sub1)
                            sum1 = stk1 - dif1
                            fcal1 = "update items set stock={} where Item_Code='{}'".format(sum1,req.POST["item1"])
                            cur.execute(fcal1)
                            con.commit()
                        
                    if req.POST["item2"] !='':
                        if itemexists(req.POST['item2']):
                            cal2 = "select stock from items where Item_Code='{}'".format(req.POST["item2"])
                            row2 = cur.execute(cal2)
                            rows2 = cur.fetchall()
                            for row2 in rows2:
                                i = row2    
                            s1 = cur.execute("select stock from items")
                            for s2 in i:
                                stk2 = s2
                            dif2 = int(sub2)
                            sum2 = stk2 - dif2
                            fcal2 = "update items set stock={} where Item_Code='{}'".format(sum2,req.POST["item2"])
                            cur.execute(fcal2)
                            con.commit()
                        
                    if req.POST["item3"] !='':
                        if itemexists(req.POST['item3']):
                            cal3 = "select stock from items where Item_Code='{}'".format(req.POST["item3"])
                            row3 = cur.execute(cal3)
                            rows3 = cur.fetchall()
                            for row3 in rows3:
                                i = row3    
                            s3 = cur.execute("select stock from items")
                            for s3 in i:
                                stk3 = s3
                            dif3 = int(sub3)
                            sum3 = stk3 - dif3
                            fcal3 = "update items set stock={} where Item_Code='{}'".format(sum3,req.POST["item3"])
                            cur.execute(fcal3)
                            con.commit() 
                        
                    if req.POST["item4"] !='':
                        if itemexists(req.POST['item4']):
                            cal4 = "select stock from items where Item_Code='{}'".format(req.POST["item4"])
                            row4 = cur.execute(cal4)
                            rows4 = cur.fetchall()
                            for row4 in rows4:
                                i = row4  
                            s4 = cur.execute("select stock from items")
                            for s4 in i:
                                stk4 = s4
                            dif4 = int(sub4)
                            sum4 = stk4 - dif4
                            fcal4 = "update items set stock={} where Item_Code='{}'".format(sum4,req.POST["item4"])
                            cur.execute(fcal4)
                            con.commit()
                            
                    if req.POST["item5"] !='':
                        if itemexists(req.POST['item5']):
                            cal5 = "select stock from items where Item_Code='{}'".format(req.POST["item5"])
                            row5 = cur.execute(cal5)
                            rows5 = cur.fetchall()
                            for row5 in rows5:
                                i = row5    
                            s5 = cur.execute("select stock from items")
                            for s5 in i:
                                stk5 = s5
                            dif5 = int(sub5)
                            sum5 = stk5 - dif5
                            fcal5 = "update items set stock={} where Item_Code='{}'".format(sum5,req.POST["item5"])
                            cur.execute(fcal5)
                            con.commit()    
                        
                    if req.POST["item6"] !='':
                        if itemexists(req.POST['item6']):
                            cal6 = "select stock from items where Item_Code='{}'".format(req.POST["item6"])
                            row6 = cur.execute(cal6)
                            rows6 = cur.fetchall()
                            for row6 in rows6:
                                i = row6   
                            s6 = cur.execute("select stock from items")
                            for s6 in i:
                                stk6 = s6
                            dif6 = int(sub6)
                            sum6 = stk6 - dif6
                            fcal6 = "update items set stock={} where Item_Code='{}'".format(sum6,req.POST["item6"])
                            cur.execute(fcal6)
                            con.commit()    
                        
                    if req.POST["item7"] !='':
                        if itemexists(req.POST['item7']):
                            cal7 = "select stock from items where Item_Code='{}'".format(req.POST["item7"])
                            row7 = cur.execute(cal7)
                            rows7 = cur.fetchall()
                            for row7 in rows7:
                                i = row7    
                            s7 = cur.execute("select stock from items")
                            for s7 in i:
                                stk7 = s7
                            dif7 = int(sub7)
                            sum7 = stk7 - dif7
                            fcal7 = "update items set stock={} where Item_Code='{}'".format(sum7,req.POST["item7"])
                            cur.execute(fcal7)
                            con.commit()                
                           
                    return render(req,'inc.html')
            else:
                return render(req,'existingbillno.html')
        else:
            return render(req, 'phnc.html')
    else:
        return render(req,'logintocontinue.html')

                                        #---------------------------Viewing All Purchases-----------------------------

def temppurlist(req):
    if logincache[0] == 1:
        return render(req,'temppurlist.html')
    else:
        return render(req,'logintocontinue.html')
        
def generatepurlist(req):
    cur.execute('select * from purlisttable')
    data = cur.fetchall()
    try:
        vtop2()
        for row in data:
            file02 = open(djpathv2, mode='a+')
            for s in range(0,4):
                if s == 0:
                    d = '<tr><td>' + str(row[s]) + '</td><td>'
                    file02.writelines(d)
                if s == 1 or s == 2:
                    d = str(row[s]) + '</td><td>'
                    file02.writelines(d)
                if s == 3:
                    d = str(row[s]) + '</td></tr>\n'
                    file02.writelines(d)
        file02.close()
        vbot2()
        return render(req,'temp_mysql_purlist.html')
    except:
        return render(req,'nodata.html')

                                             #----------------------------Editing Purchases--------------------------------

def editpur(req):
    if logincache[0] == 1:
        return render(req,'editpurchase.html')
    else:
        return render(req,'logintocontinue.html')

def pureditor(req):
    b = req.POST['bill_no']          
    cur.execute('select * from sellers where Bill_No = {}'.format(b))
    data = cur.fetchall()
    etop2()
    for k in data:
        file02 = open(djpathe2, mode='a+')
        file02.writelines("Seller Name: &nbsp;<input type='text' class='mi_field' name='sname' maxlength='20' value='{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(k[0]))       
        file02.writelines("Seller Ph No.: &nbsp;<input type='text' class='mi_field' name='sph' maxlength='13' value='{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(k[1]))       
        file02.writelines("Bill No.:&nbsp; <input type='text' class='mi_mi_field' name='bill_no' maxlength='7' value='{}' readonly/><br/><br/>\n".format(k[2]))
        file02.writelines("Place of Supply:&nbsp;&nbsp;&nbsp; <input type='text' class='mi_field' name='pos' maxlength='20' value='{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(k[4]))    
        file02.writelines("Seller Address: &nbsp;&nbsp;<input type='text' class='ma_field' name='sadd' maxlength='100' value='{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(k[5]))
        file02.writelines("Date:&nbsp;&nbsp; <input type='text' name='bdate' class = 'mi_mi_field' value='{}' readonly/><br/>&nbsp;<br/><br/>&nbsp;\n".format(k[3]))
        file02.writelines("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
        file02.writelines("Item Code: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Qty: &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rate (in Rs.): &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tax Rate(%): &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Amount (in Rs.): <br/><br/>\n")
    cur.execute('select * from pur_no_{}'.format(b))
    d = cur.fetchall()
    s = len(d)
    cur.execute('select * from pur_no_{}'.format(b))
    for g in range(1,s+1):
        y = cur.fetchone()
        f = str(g)
        i = 'item' + f
        q= 'qty' + f
        r = 'rate' + f
        t = 'tax' + f
        am = 'amt' + f
        cal = 'cal' + f + '();'
        iq  = 'q' + f
        it = 'tar'+ f
        ir = 'r'+ f
        file02.writelines("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;")
        file02.writelines("<input type='text' class='item'  name='{}' value='{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(i,y[0],cal))
        file02.writelines("<input type='text' class='qty' name='{}' value='{}' onblur='{}' id = '{}'/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(q,y[1],cal,iq))
        file02.writelines("<input type='text' class='qty' name='{}' value='{}' onblur='{}' id = '{}'/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(r,y[2],cal,ir))
        file02.writelines("<input type='number' class='qty' name='{}' value='{}' onblur='{}' id = '{}'/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;\n".format(t,y[3],cal,it))
        file02.writelines("<input type='text' class='amt' onblur='findTotal()' name='{}' value='{}' onblur='{}' id = '{}'/><br/><br/>\n\n".format(am,y[4],cal,am))
    file02.close()
    ebot2()
    return render (req,'edit_mysql_pur.html')

def updatepursave(req):

    cur.execute('select * from pur_no_{}'.format(req.POST["bill_no"]))
    d = cur.fetchall()
    s = len(d)
    for g in range(1,s+1):
        f = str(g)
        it = 'item' + f
        q = 'qty' + f
        fed = "select Quantity from pur_no_{} where Item_Code='{}'".format(req.POST["bill_no"],req.POST[it])
        row = cur.execute(fed)
        rows = cur.fetchall()
        for row in rows:
            i = row    
            qt = cur.execute("select Quantity from pur_no_{}".format(req.POST["bill_no"]))
        for z in i:
            qt = z
        sub = req.POST[q]    
        dif = int(sub)
        if dif > qt:
            sums = dif - qt
            cal = "select stock from items where Item_Code='{}'".format(req.POST[it])
            rem = cur.execute(cal)
            rems = cur.fetchall()
            for rem in rems:
                j = rem    
                m = cur.execute("select stock from items")
            for m in j:
                stk = m
            fsum = stk + sums
            fcal = "update items set stock={} where Item_Code='{}'".format(fsum,req.POST[it])
            cur.execute(fcal)
            con.commit()
        else:
            sums = qt - dif
            cal = "select stock from items where Item_Code='{}'".format(req.POST[it])
            rem = cur.execute(cal)
            rems = cur.fetchall()
            for rem in rems:
                j = rem    
                m = cur.execute("select stock from items")
            for m in j:
                stk = m
            fsum = stk - sums
            fcal = "update items set stock={} where Item_Code='{}'".format(fsum,req.POST[it])
            cur.execute(fcal)
            con.commit()
            
    cur.execute('select * from pur_no_{}'.format(req.POST["bill_no"]))
    d = cur.fetchall()
    s = len(d)
    for g in range(1,s+1):
        f = str(g)
        i = 'item' + f
        q = 'qty' + f
        r = 'rate' + f
        t = 'tax' + f
        am = 'amt' + f
        cal = 'cal' + f + '();'
        iq  = 'q' + f
        it = 'tar'+ f
        ir = 'r'+ f 
        ut = "update pur_no_{} set Quantity={},Rate={},Tax={},Amount={} where Item_Code='{}'".format(req.POST["bill_no"],req.POST[q],req.POST[r],\
                                                                                                       req.POST[t],req.POST[am],req.POST[i])
        cur.execute(ut)
        con.commit()
    tb = "update purlisttable set Amount = {} where Bill_No = {}".format(req.POST["bill_amt"],req.POST["bill_no"])
    cur.execute(tb)
    con.commit()
    return render(req,"purchasesavedsuccessfully.html")
#----------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                             #EXPENSES
                                                                    
                                                 #Creating Expenses and Inserting into all Expense realted tables

def newexp(req): 
    if logincache[0] == 1:
        return render(req,'newexp.html')
    else:
        return render(req,'logintocontinue.html')
        
def expense(req):
    if unique_new_exp_no(req.POST["ref_no"]):
        ect = "create table exp_no_{}(Exp_Name varchar(20),Ref_no varchar(20) primary key not null,Date date,Payment_Type varchar(20),Amount integer,Pay_Ref varchar(50))".format(req.POST["ref_no"])
        eit = "insert into exp_no_{}(Exp_Name,Ref_no,Date,Payment_Type,Amount,Pay_Ref)\
               values('{}','{}','{}','{}',{},'{}')".format(req.POST["ref_no"],req.POST["ename"],req.POST["ref_no"],\
                                                           req.POST["bdate"],req.POST["ptype"],req.POST["amt"],\
                                                           req.POST["pref"])
        cur.execute(ect)
        con.commit()
        cur.execute(eit)
        con.commit()

        elt = "insert into explisttable(Ref_No,Exp_Date,Amount,Payment_Type,Exp_Name)\
               values('{}','{}',{},'{}','{}')".format(req.POST["ref_no"],req.POST["bdate"],\
                                                    req.POST["amt"],req.POST["ptype"],\
                                                    req.POST["ename"])
        cur.execute(elt)
        con.commit()
        return render(req,'expsavedsuccessfully.html')
    else:
        return render(req,'existingbillno.html')

                                        #-----------------------------Viewing All Expenses--------------------------

def tempexplist(req):   
    if logincache[0] == 1:
        return render(req,'tempexplist.html')
    else:
        return render(req,'logintocontinue.html')
        
def generateexplist(req):    
    cur.execute('select * from explisttable')
    data = cur.fetchall()
    try:
        vtop3()
        for row in data:
            file03 = open(djpathv3, mode='a+') 
            for s in range(0,5):
                if s == 0:
                    d = '<tr><td>' + str(row[s]) + '</td><td>'
                    file03.writelines(d)
                if s == 1 or s == 2 or s == 3:
                    d = str(row[s]) + '</td><td>'
                    file03.writelines(d)
                if s == 4:
                    d = str(row[s]) + '</td></tr>\n'
                    file03.writelines(d)
        file03.close()
        vbot3()
        return render(req,'temp_mysql_explist.html')
    except:
        return render(req,'nodata.html')
                                                  #---------------------Editing Expenses-----------------------

def editexp(req):
    if logincache[0] == 1:
        return render(req,'editexpense.html')
    else:
        return render(req,'logintocontinue.html')
        
def expeditor(req):
    b = req.POST['ref_no']          
    cur.execute("select * from exp_no_{}".format(b))
    data = cur.fetchall()
    etop3()
    for k in data:
        file03 = open(djpathe3, mode='a+')
        file03.writelines("<center>")
        file03.writelines("Expense Name: <input type='text' class='mi_field' name='ename' value='{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;".format(k[0]))       
        file03.writelines("Ref No. : <input type='text' class='mi_field' name='ref_no' value='{}' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;".format(k[1]))       
        file03.writelines("Expense Date: <input type='date' name='bdate'  value='{}' style='border-radius:8px; border: 0; height: 35px; padding-left:5px;' readonly/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br/><br/>".format(k[2]))
        file03.writelines("Payment Type: <input type='text' class='mi_mi_field' name='ptype' value='{}' />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;".format(k[3]))    
        file03.writelines("Amount: <input type='text' class='amt' name='amt' value='{}'/><br/><br/>".format(k[4]))
        file03.writelines("Payment Reference: <input type='text' class='ma_field' name='pref' value='{}'/><br/>".format(k[5]))
    file03.close()
    ebot3()
    return render (req,'edit_mysql_exp.html')

def updateexpsave(req):
    cur.execute('select * from exp_no_{}'.format(req.POST["ref_no"]))
    d = cur.fetchall()
    s = len(d)
    ut = "update exp_no_{} set Payment_Type='{}', Amount={}, Pay_Ref='{}'".format(req.POST["ref_no"],req.POST["ptype"],req.POST["amt"],\
                                                                                                 req.POST["pref"], req.POST["ref_no"])
    cur.execute(ut)
    con.commit()
    st = "update explisttable set Amount = {} where ref_no = '{}'".format(req.POST["amt"],req.POST["ref_no"])
    cur.execute(st)
    con.commit()
    return render(req,"expsavedsuccessfully.html")

#-------------------------------------------------------------------------------------------------------------------------------------------------------------
                                                                       #STOCK MANAGEMENT

                                                                       #Adding New Item
def newitemsaving(req):
    si = "insert into items(Item_name,Item_Code,stock)\
           values('{}','{}',{})".format(req.POST["iname"],req.POST["icode"],0)
    di = "delete from items where Stock=0"

    if req.POST["iname"] and req.POST["icode"] != '':
        cur.execute(si)
        con.commit()

    else:
        cur.execute(di)
        con.commit
    return render(req,'isas.html')

                                                 #-----------------------Deleting Item------------------------

def delitem(req):
    di = "delete from items where Item_Code='{}'".format(req.POST["icode"])
    cur.execute(di)
    con.commit()
    return render(req,'ids.html')

                                                 #---------------------Viewing All Items----------------------

def showitemslist(req):
    cur.execute('select * from items')
    data = cur.fetchall()
    vtop4()
    for row in data:
        file04 = open(djpathv4, mode='a+')
        for s in range(0,3):
            if s == 0:
                d = '<tr><td>' + str(row[s]) + '</td><td>'
                file04.writelines(d)
            if s == 1:
                d = str(row[s]) + '</td><td>'
                file04.writelines(d)
            if s == 2:
                d = str(row[s]) + '</td></tr>\n'
                file04.writelines(d)
    file04.close()
    vbot4()
    return render(req,'temp_mysql_itemlistwindow.html')

#-------------------------------------------------------------------------------------------------------------------------------------------------------------  
                                                                     #Retrieving Table Codes 

view_top1 = '''
<html>
<style>
th,td {
	padding: 7px;
	border : 2px solid #f2f2f2;
}
tr:nth-child(even) {background-color: #0068a7;}
table {
	width: 100%;
	text-align: center;
	border-collapse: collapse;
}
</style>
<body bgcolor = '#0084d5' text = 'white'>
<center>
<table>
<tr><th>Bill No</th><th>Bill Date</th><th>Amount</th><th>Customer Name</th></tr>

'''

view_bottom1 = '''

</center>
</table>
</body>
</html>
'''

view_top2 = '''
<html>
<style>
th,td {
	padding: 7px;
	border : 2px solid #f2f2f2;
}
tr:nth-child(even) {background-color: #0068a7;}
table {
	width: 100%;
	text-align: center;
	border-collapse: collapse;
}
</style>
<body bgcolor = '#0084d5' text = 'white'>
<center>
<table>
<tr><th>Bill No</th><th>Bill Date</th><th>Amount</th><th>Seller Name</th></tr>

'''

view_bottom2 = '''

</center>
</table>
</body>
</html>
'''

view_top3 = '''
<html>
<style>
th,td {
	padding: 7px;
	border : 2px solid #f2f2f2;
}
tr:nth-child(even) {background-color: #0068a7;}
table {
	width: 100%;
	text-align: center;
	border-collapse: collapse;
}
</style>
<body bgcolor = '#0084d5' text = 'white'>
<center>
<table>
<tr><th>Ref No</th><th>Expense Date</th><th>Amount</th><th>Payment Type</th><th>Expense Name</th></tr>

'''

view_bottom3 = '''

</center>
</table>
</body>
</html>
'''

view_top4 = '''
<html>
<style>
th,td {
	padding: 7px;
	border : 2px solid #f2f2f2;
}
tr:nth-child(even) {background-color: #0068a7;}
table {
	width: 100%;
	text-align: center;
	border-collapse: collapse;
}
</style>
<body bgcolor = '#0084d5' text = 'white'>
<center>
<table>
<tr><th>Item</th><th>Item Code</th><th>Current Stock Remaining</th></tr>

'''

view_bottom4 = '''

</center>
</table>
</body>
</html>
'''

def vtop1():
    ishowfile = open(djpathv1, mode='w')
    ishowfile.write(view_top1)
    ishowfile.close()
def vbot1():
    ishowfile = open(djpathv1, mode='a')
    ishowfile.write(view_bottom1)
    ishowfile.close()

def vtop2():
    ishowfile = open(djpathv2, mode='w')
    ishowfile.write(view_top2)
    ishowfile.close()
def vbot2():
    ishowfile = open(djpathv2, mode='a')
    ishowfile.write(view_bottom2)
    ishowfile.close()

def vtop3():
    ishowfile = open(djpathv3, mode='w')
    ishowfile.write(view_top3)
    ishowfile.close()
    
def vbot3():
    ishowfile = open(djpathv3, mode='a')
    ishowfile.write(view_bottom3)
    ishowfile.close()    
 
def vtop4():
    ishowfile = open(djpathv4, mode='w')
    ishowfile.write(view_top4)
    ishowfile.close()
    
def vbot4():
    ishowfile = open(djpathv4, mode='a')
    ishowfile.write(view_bottom4)
    ishowfile.close()

edit_top1 = '''<html>
<body bgcolor='#b3ecec' align='center'>
<head><title>Edit Invoice</title>
<style>
#main {									/* for TURQUOISE overlay */
	margin-top: 15px;
	margin-left:20px;
	margin-right: 20px;
	background-color: #38B4C1;
	border-radius: 10px;
	text-align: center;
	padding-left: 10px;
	padding-right:10px;
	padding-top:0px;
	color: white;
	font-family: Calibri;
}

#nav_bar{
	border-radius:8px;
}

#nav_bar ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #003366;
  border-radius:8px;
  font-size: 23px;
  margin: 0;
  padding: 0;
}

#nav_bar li {
  float: left;
}

li a, .dropbtn {
  display: inline-block;
  color: #ffffff;
  text-align: center;
  text-decoration: none;
  padding: 8px;
}

li a:hover, .dropdown:hover {
  background-color: #002142;
}

#nav_bar li.dropdown {
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #0084d5;
  min-width: 160px;
  z-index: 1;
}

.dropdown-content a {
  color: white;
  padding: 8px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {background-color: #003366;}

.dropdown:hover .dropdown-content {
  display: block;
}

.save{
	background:    #0084d5;
	border-radius: 8px;
	padding:       8px 20px;
	color:         #ffffff;
	display:       inline-block;
	text-align:    center;
	text-decoration:none;
	border:0;
}

.save:hover{
	background: #002142;
	color: #ffffff;
	cursor: pointer;
}

#invoiceplace {
	background-color:#003366;
	border-radius:8px;
	color: white;
	padding: 10px;
}

.mi_field {
	width: 17%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
}
.ma_field {
	width: 33%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
}
.mi_mi_field {
	width: 12%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
}

.item{
	width: 15%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
	margin-left:2px;
}

.qty{
	width: 12%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
	margin-left:2px;
}

.amt{
	width: 14%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
	margin-left:2px;
}

.t_field{
	width: 23%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
}

.close {
	background:    #e10000;
	border-radius: 8px;
	padding:       8px 20px;
	color:         #ffffff;
	display:       inline-block;
	text-align:    center;
	text-decoration:none;
	border:0;
}

.close:hover{
	background: #ff0000;
	color: #ffffff;
	cursor: pointer;
}

input[readonly] {
	background-color: #dddddd;
	color: black;
	cursor: no-drop;
}
</style></head>
<div id='main'>
<h1 style='text-align:left; padding-top:7px; margin-bottom:2px;'>Royal Retailers Pvt. Ltd.</h1>
<div style='text-align:left;text-size:4px;margin:0px;'>SCO - 24 (1st Floor) <br>
Rajiv Chowk<br/>New Delhi<br/><br/></div>

<div id='nav_bar'>
<ul>
  <li><a href="/portal">Home</a></li>
  <li class="dropdown">
   <a href="javascript:void(0)" class="dropbtn">Invoicing</a>
    <div class="dropdown-content">
		<a href='/newsale'>Create New Invoice</a>
		<a href='/showinvoices'>View Invoice List</a>
		<a href='/editinvoice'>Edit Invoice</a>
    </div>
  </li>
  <li class="dropdown">
    <a href="javascript:void(0)" class="dropbtn">Purchase Center</a>
    <div class="dropdown-content">
		<a href='/newpurchase'>Create New Purchase</a>
		<a href='/showpurchases'>View Purchase List</a>
		<a href='/editpurchase'>Edit Purchase</a>
    </div>
  </li>
  <li class="dropdown">
    <a href="javascript:void(0)" class="dropbtn">Expenses</a>
    <div class="dropdown-content">
		<a href='/newexpense'>Create New Expense</a>
		<a href='/showexpenses'>View Expenses</a>
		<a href='/editexpense'>Edit Expenses</a>
    </div>
  </li>
	<li class='navlink'><a href="/stocks">Stock Management</a></li>
	<li class='navlink' style='float:right;'><a href="/logout">&nbsp;Logout&nbsp;</a></li>
</ul>
</div>
<br/>
<h1>Edit Invoice</h1><br/>
<div id='invoiceplace' align='left' style='padding: 15px;'>
<form action='/updateinvsave' method='POST' id='ivdet'> {%csrf_token%}
'''

edit_bot1 = '''
<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<div class='close' onclick='findTotal()'> Calculate New Total</div>
<p align='right'>Total:&nbsp;&nbsp;&nbsp;&nbsp;<input type='text' class='t_field' id='total' placeholder='0.0' name='bill_amt'/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
</br>
<input type='submit' value='Save Invoice' class='save'/></form>


    <script type="text/javascript">
function cal1() {
	var x = Number(document.getElementById('tar1').value);
	var y = x + 100;
	var z = y / 100;
	document.getElementById('amt1').value =
	(
		Number(document.getElementById('q1').value) *
		Number(document.getElementById('r1').value) *
		z
	);
}

function cal2() {
	var x = Number(document.getElementById('tar2').value);
	var y = x + 100;
	var z = y / 100;
	document.getElementById('amt2').value =
	(
		Number(document.getElementById('q2').value) *
		Number(document.getElementById('r2').value) *
		z
	);
}

function cal3() {
	var x = Number(document.getElementById('tar3').value);
	var y = x + 100;
	var z = y / 100;
	document.getElementById('amt3').value =
	(
		Number(document.getElementById('q3').value) *
		Number(document.getElementById('r3').value) *
		z
	);
}

function cal4() {
	var x = Number(document.getElementById('tar4').value);
	var y = x + 100;
	var z = y / 100;
	document.getElementById('amt4').value =
	(
		Number(document.getElementById('q4').value) *
		Number(document.getElementById('r4').value) *
		z
	);
}

function cal5() {
	var x = Number(document.getElementById('tar5').value);
	var y = x + 100;
	var z = y / 100;
	document.getElementById('amt5').value =
	(
		Number(document.getElementById('q5').value) *
		Number(document.getElementById('r5').value) *
		z
	);
}

function cal6() {
	var x = Number(document.getElementById('tar6').value);
	var y = x + 100;
	var z = y / 100;
	document.getElementById('amt6').value =
	(
		Number(document.getElementById('q6').value) *
		Number(document.getElementById('r6').value) *
		z
	);
}

function cal7() {
	var x = Number(document.getElementById('tar7').value);
	var y = x + 100;
	var z = y / 100;
	document.getElementById('amt7').value =
	(
		Number(document.getElementById('q7').value) *
		Number(document.getElementById('r7').value) *
		z
	);
}

function findTotal(){
    var arr = document.getElementsByClassName('amt');
    var tot=0;
    for(var i=0;i<arr.length;i++){
        if(parseInt(arr[i].value))
            tot += parseInt(arr[i].value);
    }
    document.getElementById('total').value = tot;
}
    </script>

</div>
</div>
</body>
</html>
'''

edit_top2 = '''<html>
<body bgcolor='#b3ecec' align='center'>
<head><title>Edit Purchase</title>
<style>
#main {									/* for TURQUOISE overlay */
	margin-top: 15px;
	margin-left:20px;
	margin-right: 20px;
	background-color: #38B4C1;
	border-radius: 10px;
	text-align: center;
	padding-left: 10px;
	padding-right:10px;
	padding-top:0px;
	color: white;
	font-family: Calibri;
}

#nav_bar{
	border-radius:8px;
}

#nav_bar ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #003366;
  border-radius:8px;
  font-size: 23px;
  margin: 0;
  padding: 0;
}

#nav_bar li {
  float: left;
}

li a, .dropbtn {
  display: inline-block;
  color: #ffffff;
  text-align: center;
  text-decoration: none;
  padding: 8px;
}

li a:hover, .dropdown:hover {
  background-color: #002142;
}

#nav_bar li.dropdown {
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #0084d5;
  min-width: 160px;
  z-index: 1;
}

.dropdown-content a {
  color: white;
  padding: 8px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {background-color: #003366;}

.dropdown:hover .dropdown-content {
  display: block;
}

.save{
	background:    #0084d5;
	border-radius: 8px;
	padding:       8px 20px;
	color:         #ffffff;
	display:       inline-block;
	text-align:    center;
	text-decoration:none;
	border:0;
}

.save:hover{
	background: #002142;
	color: #ffffff;
	cursor: pointer;
}

#invoiceplace {
	background-color:#003366;
	border-radius:8px;
	color: white;
	padding: 10px;
}

.mi_field {
	width: 17%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
}
.ma_field {
	width: 33%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
}
.mi_mi_field {
	width: 12%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
}

.item{
	width: 15%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
	margin-left:2px;
}

.qty{
	width: 12%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
	margin-left:2px;
}

.amt{
	width: 14%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
	margin-left:2px;
}

.t_field{
	width: 23%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
}

.close {
	background:    #e10000;
	border-radius: 8px;
	padding:       8px 20px;
	color:         #ffffff;
	display:       inline-block;
	text-align:    center;
	text-decoration:none;
	border:0;
}

.close:hover{
	background: #ff0000;
	color: #ffffff;
	cursor: pointer;
}

input[readonly] {
	background-color: #dddddd;
	color: black;
	cursor: no-drop;
}
</style></head>
<div id='main'>
<h1 style='text-align:left; padding-top:7px; margin-bottom:2px;'>Royal Retailers Pvt. Ltd.</h1>
<div style='text-align:left;text-size:4px;margin:0px;'>SCO - 24 (1st Floor) <br>
Rajiv Chowk<br/>New Delhi<br/><br/></div>

<div id='nav_bar'>
<ul>
  <li><a href="/portal">Home</a></li>
  <li class="dropdown">
   <a href="javascript:void(0)" class="dropbtn">Invoicing</a>
    <div class="dropdown-content">
		<a href='/newsale'>Create New Invoice</a>
		<a href='/showinvoices'>View Invoice List</a>
		<a href='/editinvoice'>Edit Invoice</a>
    </div>
  </li>
  <li class="dropdown">
    <a href="javascript:void(0)" class="dropbtn">Purchase Center</a>
    <div class="dropdown-content">
		<a href='/newpurchase'>Create New Purchase</a>
		<a href='/showpurchases'>View Purchase List</a>
		<a href='/editpurchase'>Edit Purchase</a>
    </div>
  </li>
  <li class="dropdown">
    <a href="javascript:void(0)" class="dropbtn">Expenses</a>
    <div class="dropdown-content">
		<a href='/newexpense'>Create New Expense</a>
		<a href='/showexpenses'>View Expenses</a>
		<a href='/editexpense'>Edit Expenses</a>
    </div>
  </li>
	<li class='navlink'><a href="/stocks">Stock Management</a></li>
	<li class='navlink' style='float:right;'><a href="/logout">&nbsp;Logout&nbsp;</a></li>
</ul>
</div>
<br/>
<h1>Edit Purchase</h1><br/>
<div id='invoiceplace' align='left' style='padding: 15px;'>
<form action='/updatepursave' method='POST' id='ivdet'> {%csrf_token%}
'''

edit_bot2 = '''
<br/>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<div class='close' onclick='findTotal()'> Calculate New Total</div>
<p align='right'>Total:&nbsp;&nbsp;&nbsp;&nbsp;<input type='text' class='t_field' id='total' placeholder='0.0' name='bill_amt'/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</p>
</br>
<input type='submit' value='Save Purchase' class='save'/></form>


    <script type="text/javascript">
function cal1() {
	var x = Number(document.getElementById('tar1').value);
	var y = x + 100;
	var z = y / 100;
	document.getElementById('amt1').value =
	(
		Number(document.getElementById('q1').value) *
		Number(document.getElementById('r1').value) *
		z
	);
}

function cal2() {
	var x = Number(document.getElementById('tar2').value);
	var y = x + 100;
	var z = y / 100;
	document.getElementById('amt2').value =
	(
		Number(document.getElementById('q2').value) *
		Number(document.getElementById('r2').value) *
		z
	);
}

function cal3() {
	var x = Number(document.getElementById('tar3').value);
	var y = x + 100;
	var z = y / 100;
	document.getElementById('amt3').value =
	(
		Number(document.getElementById('q3').value) *
		Number(document.getElementById('r3').value) *
		z
	);
}

function cal4() {
	var x = Number(document.getElementById('tar4').value);
	var y = x + 100;
	var z = y / 100;
	document.getElementById('amt4').value =
	(
		Number(document.getElementById('q4').value) *
		Number(document.getElementById('r4').value) *
		z
	);
}

function cal5() {
	var x = Number(document.getElementById('tar5').value);
	var y = x + 100;
	var z = y / 100;
	document.getElementById('amt5').value =
	(
		Number(document.getElementById('q5').value) *
		Number(document.getElementById('r5').value) *
		z
	);
}

function cal6() {
	var x = Number(document.getElementById('tar6').value);
	var y = x + 100;
	var z = y / 100;
	document.getElementById('amt6').value =
	(
		Number(document.getElementById('q6').value) *
		Number(document.getElementById('r6').value) *
		z
	);
}

function cal7() {
	var x = Number(document.getElementById('tar7').value);
	var y = x + 100;
	var z = y / 100;
	document.getElementById('amt7').value =
	(
		Number(document.getElementById('q7').value) *
		Number(document.getElementById('r7').value) *
		z
	);
}

function findTotal(){
    var arr = document.getElementsByClassName('amt');
    var tot=0;
    for(var i=0;i<arr.length;i++){
        if(parseInt(arr[i].value))
            tot += parseInt(arr[i].value);
    }
    document.getElementById('total').value = tot;
}
    </script>

</div>
</div>
</body>
</html>
'''

edit_top3='''
<html>
<body bgcolor='#b3ecec' align='center'>
<head><title>Edit Expense</title>
<style>
#main {									/* for TURQUOISE overlay */
	margin-top: 15px;
	margin-left:20px;
	margin-right: 20px;
	background-color: #38B4C1;
	border-radius: 10px;
	text-align: center;
	padding-left: 10px;
	padding-right:10px;
	padding-top:0px;
	color: white;
	font-family: Calibri;
}

#nav_bar{
	border-radius:8px;
}

#nav_bar ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #003366;
  border-radius:8px;
  font-size: 23px;
  margin: 0;
  padding: 0;
}

#nav_bar li {
  float: left;
}

li a, .dropbtn {
  display: inline-block;
  color: #ffffff;
  text-align: center;
  text-decoration: none;
  padding: 8px;
}

li a:hover, .dropdown:hover {
  background-color: #002142;
}

#nav_bar li.dropdown {
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #0084d5;
  min-width: 160px;
  z-index: 1;
}

.dropdown-content a {
  color: white;
  padding: 8px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {background-color: #003366;}

.dropdown:hover .dropdown-content {
  display: block;
}

.save{
	background:    #0084d5;
	border-radius: 8px;
	padding:       8px 20px;
	color:         #ffffff;
	display:       inline-block;
	text-align:    center;
	text-decoration:none;
	border:0;
}

.save:hover{
	background: #002142;
	color: #ffffff;
	cursor: pointer;
}

#invoiceplace {
	background-color:#003366;
	border-radius:8px;
	color: white;
	padding: 10px;
}

.mi_field {
	width: 17%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
}
.ma_field {
	width: 33%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
}
.mi_mi_field {
	width: 12%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
}

.item{
	width: 15%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
	margin-left:2px;
}

.qty{
	width: 12%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
	margin-left:2px;
}

.amt{
	width: 14%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
	margin-left:2px;
}

.t_field{
	width: 23%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
}

.close {
	background:    #e10000;
	border-radius: 8px;
	padding:       8px 20px;
	color:         #ffffff;
	display:       inline-block;
	text-align:    center;
	text-decoration:none;
	border:0;
}

.close:hover{
	background: #ff0000;
	color: #ffffff;
	cursor: pointer;
}

input[readonly] {
	background-color: #dddddd;
	color: black;
	cursor: no-drop;
}
</style></head>
<div id='main'>
<h1 style='text-align:left; padding-top:7px; margin-bottom:2px;'>Royal Retailers Pvt. Ltd.</h1>
<div style='text-align:left;text-size:4px;margin:0px;'>SCO - 24 (1st Floor) <br>
Rajiv Chowk<br/>New Delhi<br/><br/></div>

<div id='nav_bar'>
<ul>
  <li><a href="/portal">Home</a></li>
  <li class="dropdown">
   <a href="javascript:void(0)" class="dropbtn">Invoicing</a>
    <div class="dropdown-content">
		<a href='/newsale'>Create New Invoice</a>
		<a href='/showinvoices'>View Invoice List</a>
		<a href='/editinvoice'>Edit Invoice</a>
    </div>
  </li>
  <li class="dropdown">
    <a href="javascript:void(0)" class="dropbtn">Purchase Center</a>
    <div class="dropdown-content">
		<a href='/newpurchase'>Create New Purchase</a>
		<a href='/showpurchases'>View Purchase List</a>
		<a href='/editpurchase'>Edit Purchase</a>
    </div>
  </li>
  <li class="dropdown">
    <a href="javascript:void(0)" class="dropbtn">Expenses</a>
    <div class="dropdown-content">
		<a href='/newexpense'>Create New Expense</a>
		<a href='/showexpenses'>View Expenses</a>
		<a href='/editexpense'>Edit Expenses</a>
    </div>
  </li>
	<li class='navlink'><a href="/stocks">Stock Management</a></li>
	<li class='navlink' style='float:right;'><a href="/logout">&nbsp;Logout&nbsp;</a></li>
</ul>
</div>
<br/>
<h1>Edit Expense</h1><br/>
<div id='invoiceplace' align='left' style='padding: 15px;'>
<form action='/updateexpsave' method='POST' id='ivdet'> {%csrf_token%}
'''

edit_bot3 ='''
<br/><br/>
<input type='submit' value='Save Expense' class='save'/></form>

</div>
<br/>
</div>
</body>
</html>

'''

def etop1():
    ishowfile = open(djpathe1, mode='w')
    ishowfile.write(edit_top1)
    ishowfile.close()
    
def ebot1():
    ishowfile = open(djpathe1, mode='a')
    ishowfile.write(edit_bot1)
    ishowfile.close()

def etop2():
    pshowfile = open(djpathe2, mode='w')
    pshowfile.write(edit_top2)
    pshowfile.close()
    
def ebot2():
    pshowfile = open(djpathe2, mode='a')
    pshowfile.write(edit_bot2)
    pshowfile.close()

def etop3():
    eshowfile = open(djpathe3, mode='w')
    eshowfile.write(edit_top3)
    eshowfile.close()

def ebot3():
    eshowfile = open(djpathe3, mode='a')
    eshowfile.write(edit_bot3)
    eshowfile.close()

export_top1='''
<html>
<body bgcolor='#b3ecec' align='center'>
<head><title>Export Invoice</title>
<style>
#main {									/* for TURQUOISE overlay */
	margin-top: 15px;
	margin-left:20px;
	margin-right: 20px;
	background-color: #38B4C1;
	border-radius: 10px;
	text-align: center;
	padding-left: 10px;
	padding-right:10px;
	padding-top:0px;
	color: white;
	font-family: Calibri;
}

#nav_bar{
	border-radius:8px;
}

#nav_bar ul {
  list-style-type: none;
  margin: 0;
  padding: 0;
  overflow: hidden;
  background-color: #003366;
  border-radius:8px;
  font-size: 23px;
  margin: 0;
  padding: 0;
}

#nav_bar li {
  float: left;
}

li a, .dropbtn {
  display: inline-block;
  color: #ffffff;
  text-align: center;
  text-decoration: none;
  padding: 8px;
}

li a:hover, .dropdown:hover {
  background-color: #002142;
}

#nav_bar li.dropdown {
  display: inline-block;
}

.dropdown-content {
  display: none;
  position: absolute;
  background-color: #0084d5;
  min-width: 160px;
  z-index: 1;
}

.dropdown-content a {
  color: white;
  padding: 8px;
  text-decoration: none;
  display: block;
  text-align: left;
}

.dropdown-content a:hover {background-color: #003366;}

.dropdown:hover .dropdown-content {
  display: block;
}

.save{
	background:    #0084d5;
	border-radius: 8px;
	padding:       8px 20px;
	color:         #ffffff;
	display:       inline-block;
	text-align:    center;
	text-decoration:none;
	border:0;
}

.save:hover{
	background: #002142;
	color: #ffffff;
	cursor: pointer;
}

#invoiceplace {
	background-color:#003366;
	border-radius:8px;
	color: white;
	padding: 10px;
}

.mi_field {
	width: 17%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
}
.ma_field {
	width: 33%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
}
.mi_mi_field {
	width: 12%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
}

.item{
	width: 15%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
	margin-left:2px;
}

.qty{
	width: 12%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
	margin-left:2px;
}

.amt{
	width: 14%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
	margin-left:2px;
}

.t_field{
	width: 23%;
	height: 35px;
	border-radius: 8px;
	padding:5px;
	border:0;
}

.close {
	background:    #e10000;
	border-radius: 8px;
	padding:       8px 20px;
	color:         #ffffff;
	display:       inline-block;
	text-align:    center;
	text-decoration:none;
	border:0;
}

.close:hover{
	background: #ff0000;
	color: #ffffff;
	cursor: pointer;
}

input[readonly] {
	background-color: #dddddd;
	color: black;
	cursor: no-drop;
}
</style></head>
<div id='main'>
<h1 style='text-align:left; padding-top:7px; margin-bottom:2px;'>Royal Retailers Pvt. Ltd.</h1>
<div style='text-align:left;text-size:4px;margin:0px;'>SCO - 24 (1st Floor) <br>
Rajiv Chowk<br/>New Delhi<br/><br/></div>

<div id='nav_bar'>
<ul>
  <li><a href="/portal">Home</a></li>
  <li class="dropdown">
   <a href="javascript:void(0)" class="dropbtn">Invoicing</a>
    <div class="dropdown-content">
		<a href='/newsale'>Create New Invoice</a>
		<a href='/showinvoices'>View Invoice List</a>
		<a href='/editinvoice'>Edit Invoice</a>
    </div>
  </li>
  <li class="dropdown">
    <a href="javascript:void(0)" class="dropbtn">Purchase Center</a>
    <div class="dropdown-content">
		<a href='/newpurchase'>Create New Purchase</a>
		<a href='/showpurchases'>View Purchase List</a>
		<a href='/editpurchase'>Edit Purchase</a>
    </div>
  </li>
  <li class="dropdown">
    <a href="javascript:void(0)" class="dropbtn">Expenses</a>
    <div class="dropdown-content">
		<a href='/newexpense'>Create New Expense</a>
		<a href='/showexpenses'>View Expenses</a>
		<a href='/editexpense'>Edit Expenses</a>
    </div>
  </li>
	<li class='navlink'><a href="/stocks">Stock Management</a></li>
	<li class='navlink' style='float:right;'><a href="/logout">&nbsp;Logout&nbsp;</a></li>
</ul>
</div>
<br/>
<h1>Export Invoice</h1><br/>
<div id='invoiceplace' align='left' style='padding: 15px;'>
<form action='/billcreated' method='POST' id='ivdet'> {%csrf_token%}
'''

export_bot1 ='''
<br/><br/>
File Name to save: <input type='text' class='amt' name='filename' placeholder=' without extension' maxlength='10' required/> &nbsp;&nbsp;&nbsp;
<input type='submit' value='Export This Invoice' class='save'/></form>

</div>
<br/>
</div>
</body>
</html>

'''

export_top2='''
Royal Retailers Pvt Ltd.
SCO - 24 (1st Floor)
Rajiv Chowk
New Delhi
'''

def extop1():
    exshowfile = open(djpathex1, mode='w')
    exshowfile.write(export_top1)
    exshowfile.close()

def exbot1():
    exshowfile = open(djpathex1, mode='a+')
    exshowfile.write(export_bot1)
    exshowfile.close()

def extop2(filename,date,cname,cph,cadd,bno):
    b = exportpath + filename + '.txt'
    exshowfile = open(b, mode='w')
    exshowfile.write(export_top2)
    exshowfile.write('\nCustomer Name: {}'.format(cname))
    exshowfile.write('\nCustomer Phone: {}'.format(cph))
    exshowfile.write('\nCustomer Address: {}'.format(cadd))
    exshowfile.write('\n\nBill No.: {}'.format(bno))
    exshowfile.write('\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    exshowfile.write('\n\t\t\t\t\t    INVOICE\t\t\t\t{}'.format(date))
    exshowfile.write('\n+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    exshowfile.write('\n\tItem name\t\t\t\t\tQuantity\tRate\tTax\tAmount')
    exshowfile.close() 

def stocks(req):
    if logincache[0] == 1:
        return render(req, "stocks.html")
    else:
        return render(req, 'logintocontinue.html')

def b123(req):
    return render(req, "isas.html")

def intcheck(x):
    try:
        b = int(x)
        return True
    except:
        return False

def itemexists(x):
    cur.execute("SELECT EXISTS(SELECT stock from items WHERE Item_Code = '{}')".format(x))
    data = cur.fetchone()
    if 1 in data:
        return True
    else:
        return False

def unique_new_inv_no(x):
    cur.execute("SELECT EXISTS(SELECT * from customers where bill_no = {})".format(x))
    data = cur.fetchone()
    if 0 in data:
        return True
    else:
        return False
    
def unique_new_pur_no(x):
    cur.execute("SELECT EXISTS(SELECT * from sellers where bill_no = {})".format(x))
    data = cur.fetchone()
    if 0 in data:
        return True
    else:
        return False
    
def unique_new_exp_no(x):
    cur.execute("SELECT EXISTS(SELECT * from explisttable where ref_no = '{}')".format(x))
    data = cur.fetchone()
    if 0 in data:
        return True
    else:
        return False
