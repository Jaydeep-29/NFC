from django.shortcuts import redirect, render
from nfc_web.forms import LoginForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from nfc_app.models import NFC_Details


# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                 login(request, user)
                 nfc_details = NFC_Details.objects.all()
                 return render(request, "nfc.html", {"nfc_details": nfc_details,})
            else:    
                msg = 'Invalid credentials' 
                     
        else:
            msg = 'Error validating the form'   
            #return redirect("/") 
    return render(request, "accounts/login.html", {"form": form,})

@login_required(login_url="/login_view/")
def nfc(request):
    print("---------nfc called--------")
    if request.method == "GET":
        nfc_details = NFC_Details.objects.all()
        return render(request,'nfc.html', {'nfc_details':nfc_details,})
    else:
        return redirect('/')