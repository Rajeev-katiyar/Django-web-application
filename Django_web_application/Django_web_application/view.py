from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.shortcuts import render
from signup.models import signdata
from django.urls import reverse 


def homepage(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        en = signdata(user_name=user_name, email=email, password=password)
        en.save()

  
        url = reverse('homelogin')

        return redirect(url)

    return render(request,"index.html")
            
            
  
def homelogin(request):
    if request.method == 'POST':
        # Get user input from the form
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Try to retrieve a user with the given email and password
            user = signdata.objects.get(email=email, password=password)

            # If a user is found, it's a successful login
            # Generate the dynamic URL based on the view's name
            url = reverse('file_uploading')

            return redirect(url)
            
            
        except signdata.DoesNotExist:
            # If no user is found, it's an incorrect login
            return render(request, "error.html")

    # Render the login form for GET requests
    return render(request, "index.html")