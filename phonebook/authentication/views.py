from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from authentication.models import User
from authentication.serializers import UserSerializer

from records.serializers import ContactSerializer

class UserDetail(APIView):
    def get(self, request):
        return Response(UserSerializer(User.objects.get(email=request.GET['email'])).data)

    def post(self, request):
        user_serializer = UserSerializer(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response(user_serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializers.error, status = status.HTTP_400_BAD_REQUEST)

class AllContactsView(APIView):

    def is_request_authentic(self, request):
        email = request.META.get('HTTP_EMAIL')
        password = request.META.get('HTTP_PASSWORD')

        if User.objects.all().filter(email = email).exists():
            user = User.objects.get(email = email)
            if (user.password == password):
                return True
            else:
                return False
        else:
            return False

    def get(self, request):
        if self.is_request_authentic(request):
            user = User.objects.all().filter(email = request.META.get('HTTP_EMAIL')).get()
            allContacts = list(user.contacts.filter())

            return Response(ContactSerializer(allContacts, many = True).data)
        else:
            return Response(status = status.HTTP_403_FORBIDDEN)

# @csrf_exempt
# @api_view(['POST'])
# def create_user(request):
#     user_serializer = UserSerializer(data=request.data)
#     if user_serializer.is_valid():
#         user_serializer.save()
#         return Response(user_serializer.data, status = status.HTTP_201_CREATED)
#     return Response(serializers.error, status = status.HTTP_400_BAD_REQUEST)


