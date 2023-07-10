from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector

# Create your views here.


def index(request):
    if (request.method == 'POST'):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kgreddy"
        )
        mycursor = mydb.cursor()  # it establises a connection
        name = request.POST['name']
        rn = request.POST['rn']
        branch = request.POST['branch']
        email = request.POST['email']
        contact = request.POST['con']
        user = request.POST['username']
        password = request.POST['pwd']
        mycursor.execute("insert into customer(name,rollno,branch,emailid,contact) VALUES('" +
                         name+"','"+rn+"','"+branch+"','"+email+"','"+contact+"')")
        mycursor.execute("insert into user(username,password) VALUES('"+user+"','"+password+"')")
        mydb.commit()
        return render(request, 'login.html')
    else:
        return render(request, 'index.html')


def login(request):
    if (request.method == 'POST'):
        con = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='kgreddy',
        )
        cur = con.cursor()
        uname = request.POST['username']
        pwd = request.POST['password']
        cur.execute("select * from user where username='" +
uname+"' and password='"+pwd+"'")
        result = cur.fetchone()

        if (result != None):
            return render(request, 'home.html')
        else:
            return render(request, 'login.html', {'status': 'invalid credentials'})

    else:
        return render(request, 'login.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
     if (request.method == 'POST'):
        mydb1 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kgreddy"
        )
        mycurso = mydb1.cursor()  # it establises a connection
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['message']
 
        mycurso.execute("insert into contact(name,email,message) VALUES('"+name+"','"+email+"','"+msg+"')")
        mydb1.commit()
        return render(request, 'thankyou.html')
        
     else:
        return render(request, 'contact.html',{'status': 'invalid credentials'})
   


def home(request):
     if (request.method == 'POST'):
        mydb2 = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="kgreddy"
        )
        mycurs = mydb2.cursor()  # it establises a connection
        fname = request.POST['q40_menu[cc_firstName]']
        lname = request.POST['q40_menu[cc_lastName]']
        ccnum = request.POST['sublabel_cc_number']
        ccvv = request.POST['sublabel_cc_ccv']
        ccexp = request.POST['sublabel_cc_card_expiry']
 
        mycurs.execute("insert into card_details(firstname,lastname,ccnum,ccvv,ccexp) VALUES('"+fname+"','"+lname+"','"+ccnum+"','"+ccvv+"','"+ccexp+"')")
        mydb2.commit()
        return render(request, 'thankyou.html')
        
     else:
        return render(request, 'home.html')

def thankyou(request):
    return render(request, 'thankyou.html')

