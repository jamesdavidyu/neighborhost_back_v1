from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from . import serializers

def create_account(request):
    data = models.Neighbor.objects.all()
    serializer = serializers.NeighborSerializer(data, many=True)
    return JsonResponse({'neighbors' : serializer.data})

# Create your views here.
def login_neighbor(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] # is this the same even when connected to React?
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was an error logging in. Please try again."))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', {})