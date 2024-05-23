from django.shortcuts import render
import datetime
def home(request):
    dict = {"name" : 'omor', 'age' : 20,'text' : "i'm 20 years old\n and i also teen now",'date' : datetime.datetime.now(),'value':"",
            'lOfDict':[
                {'name' : 'omor','age' : 20,'class' : 14},
                {'name' : 'abubakar','age' : 23,'class' : 11},
                {'name' : 'nadim','age' : 22,'class' : 14}
            ],'title' : '<','file' : 123456789,'time' : datetime.datetime.now(),'var':['staes', ['Kansas', ['Lawrence', 'Topeka'], 'Illinois']]}
    return render(request,'index.html',dict)
# Create your views here.
