from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
import json
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import models
from . import serializers

@api_view(['GET', 'POST']) # comment this and next line out to see json
# # @permission_classes([IsAuthenticated])
def create_account(request):
    if request.method == 'GET':
        data = models.Neighbor.objects.all() # change data variable name
        serializer = serializers.NeighborSerializer(data, many=True)
        return Response({'neighbors' : serializer.data})
    elif request.method == 'POST':
        serializer = serializers.NeighborSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'neighbors' : serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# django wednesday's example...
@api_view(['POST'])
@permission_classes([IsAuthenticated])
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