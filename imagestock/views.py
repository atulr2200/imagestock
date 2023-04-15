
from ast import Param
import re

from django.db.models import sql
from django.http import HttpResponse,Http404
import mysql.connector
from myapp.models import *
from django.shortcuts import render
from django.shortcuts import redirect
from django.conf import settings
import os
import django

def loginaction(request):
    
    return render(request,"login.html")

def home(request):

    return redirect("home/")

def show_home_page(request):

    cats=Category.objects.all()
    images=Image.objects.all()
    data={'images': images, 'cats': cats}

    return render(request, "home.html", data)


def show_category_page(request,cid):

    cats=Category.objects.all()

    cat1=Category.objects.get(pk=cid)


    images=Image.objects.filter(cat=cat1)
    data={'images': images, 'cats': cats}
    return render(request, "home.html", data),


   


#def imgview(request):

 #   return render(request,"image_view.html"),

def search(request):
    query=request.GET['query']

    if query=='':
        
        return render(request,'error.html')
    else:
        
        allpost =Image.objects.filter(title__icontains=query)
        gh=Image.objects.filter( description__icontains=query)
        params= {'allpost':allpost,'gh':gh}
        return render(request,'search.html',params)

fn=''
ln=''
em=''
pwd=''
# Create your views here.
def signaction(request):
    global fn,l,em,pwd
    if request.method=='POST':
        m=sql.connect(host="localhost:3306",user="root",passwd="atul@123",database='image')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="insert into users Values('{}','{}','{}','{}')".format(fn,ln,em,pwd)
        cursor.execute(c)
        m.commit()

    return render(request,'sigin.html')
 
def dat_a(request):
     mydb=mysql.connector.connect(host="localhost" , user="root", passwd="atul@123",database="airline")
     mycurser= mydb. cursor()
     mycurser.execute("select * from user")
     for i in mycurser:
            i;
     return render(request,'sig.html' )
    

        