from django.shortcuts import render,redirect
from signup.models import signdata
from django.urls import reverse 

# Create your views here.


def signdatas(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        en = signdata(user_name=user_name, email=email, password=password)
        en.save()

  
        url = reverse('login')

        return redirect(url)

    return render(request,"signup.html")
            


