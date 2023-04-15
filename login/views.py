from django.shortcuts import render
import mysql.connector as sql
em=''
pwd=''
# Create your views here.
def loginaction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="atul@123",database='image')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="username":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from users where username='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'error.html')
        else:
            return render(request,"home.html")

    return render(request,'login_page.html')
