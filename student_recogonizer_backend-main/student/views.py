from django.http import JsonResponse
from django.shortcuts import render
from .models import Image
from django.http import HttpResponse
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from backend_logic import face_features_extraction

def getRoutes(request):
        # if request.method == 'POST':
        #     form = ImageUploadForm(request.POST, request.FILES)
        # if form.is_valid():
        #     form.save()
        #     return redirect('index')
        # else:
        #     form = ImageUploadForm()
        # print(request)
        routes =  {
            'student_recogonizer' : 'welcome'
        }
        
        return JsonResponse(routes, safe=False)

def showImages(request):
    data = Image.objects.all()
    context = {
        'data' : data
    }
    return render(request,"display.html", context)

def uploadFile(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        print("file recieved")
        # Process the uploaded file here
        path = default_storage.save('tmp/test.jpg', ContentFile(uploaded_file.read()))
        tmp_file = os.path.join(settings.MEDIA_ROOT, path)
        faceDetection = face_features_extraction.FaceFeatureExtraction()
        face_name = faceDetection.detectFace(tmp_file)
        print(f"register no is {face_name}")

        return JsonResponse([{"name" : face_name}],safe=False)
    else:
        print("file not recieved")
        return HttpResponse('Invalid request method')
