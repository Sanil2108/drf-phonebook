from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from authentication.models import User

from records.models import Contact
from records.serializers import ContactSerializer

class ContactView(APIView):

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
            return Response(ContactSerializer(Contact.objects.get(pk = request.GET['pk'])).data)
        else:
            return Response(status = status.HTTP_403_FORBIDDEN)

    def post(self, request):
        if self.is_request_authentic(request):
            contact_serializer = ContactSerializer(data = request.data)
            print(contact_serializer)
            if contact_serializer.is_valid():
                contact_serializer.save()
                return Response(contact_serializer.data, status = status.HTTP_201_CREATED)
            else:
                return Response(status = status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status = status.HTTP_403_FORBIDDEN)