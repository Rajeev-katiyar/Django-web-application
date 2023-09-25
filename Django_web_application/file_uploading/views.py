

from django.shortcuts import render, redirect
from .models import img_uploader


# Create your views here.
def mainuploader(request):
    message = None  # Initialize the message variable

    if request.method == "POST":
        uploaded_file = request.FILES.get('file')
        if uploaded_file:
            try:
                # Process and save the file
                new_file = img_uploader(imageFile=uploaded_file)
                new_file.save()
                message = "File uploaded successfully!"  # Set success message
            except:
               pass  # Set error message

    files = img_uploader.objects.all()
    context = {
        'files': files,
        'message': message,  # Add the message to the context
    }

    return render(request, "file_upload.html", context)
