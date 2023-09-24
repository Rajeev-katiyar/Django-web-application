from django.shortcuts import render,redirect
from signup.models import signdata

# Create your views here.

def loginaction(request):
    if request.method == 'POST':
        # Get user input from the form
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            # Try to retrieve a user with the given email and password
            user = signdata.objects.get(email=email, password=password)

            # If a user is found, it's a successful login
            return render(request, "file_upload.html", {'user': user})
        except signdata.DoesNotExist:
            # If no user is found, it's an incorrect login
            return render(request, "error.html")

    # Render the login form for GET requests
    return render(request, "login.html")






