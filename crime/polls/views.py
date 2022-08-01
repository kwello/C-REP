from django.shortcuts import render
from polls.forms import MyForm
from django.template import loader
from django.http import HttpResponse

def open(request):
    return render(request,"query.html")

def homepage(request):
    return render(request,"index.html",{})
def register(request):
    return render(request,"registration.html",{})

def setdata(request):
    if request.method=["POST"]:
        name=

'''
def openpolls(request):
    return render(request, "home.html", {'form':MyForm})

def responseform(request):
 #if form is submitted
     if request.method == 'POST':
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            name = myForm.cleaned_data['name']
            email = myForm.cleaned_data['email']
            date = myForm.cleaned_data['date']
            feedback = myForm.cleaned_data['feedback']

            context = {
            'name': name,
            'email': email,
            'date' : date,
            'feedback': feedback
            }

            template = loader.get_template('thankyou.html')

            return HttpResponse(template.render(context, request))



     else:
         form = MyForm()
         return render(request, 'responseform.html', ({'name': name , 'email': email,'date': date ,'feedback': feedback}))
'''
