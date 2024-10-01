from django.shortcuts import render
from .forms import BookingForm,RegistrationForm,CleanersForm, Contactform

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    form = Contactform()
    if request.method == "POST":
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
    context = {"form":form}
    return render(request,"contact.html",context)

def register(request):
    form1 = RegistrationForm()
    if request.method == 'POST':
        form1 = RegistrationForm(request.POST)
        if form1.is_valid():
            form1.save()
    
    form2 = CleanersForm()
    if request.method == 'POST':
        form2 = CleanersForm(request.POST)
        if form2.is_valid():
            form2.save()
    context = {'form1':form1,'form2':form2}
    return render(request, "register.html",context)

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)
    