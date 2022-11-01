from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate  # add this
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from app.form import LoginForm
from django.http import HttpResponse
from app.models import *
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from PIL import Image

import base64
import json
import time
import numpy as np


@csrf_exempt
def homepage(request):
    if request.method == 'POST' and request.FILES['image']:
        upload = request.FILES['image']
        fss = FileSystemStorage()

        name = str(datetime.fromtimestamp(time.time())) + ".jpg"
        user = str(request.user)

        img = Image.open(upload)
        img1 = np.asarray(img)
        print(img1)

        file = fss.save(name, upload)
        file_url = fss.url(file)

        img = ImageModel.create(name, file, user)
        img.save()
        return render(request, 'homepage.html', {'file_url': file_url})

    return render(request, 'homepage.html')


def success(request):
    return HttpResponse('successfully uploaded')


@csrf_exempt
def login_request(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect(homepage)
            else:
                messages.error(request, "Invalid username or password.")
    form = LoginForm(request.POST)
    return render(request=request, template_name="login.html", context={"login_form": form})


@csrf_exempt
def get_result(request):
    if request.method == "POST":
        data = request.POST.get("data")
        print(data)
        return HttpResponse(json.dumps({"a": 1}),
                            content_type='application/json')

    return render(request=request, template_name="login.html")

