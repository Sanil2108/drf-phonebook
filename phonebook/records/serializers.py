from rest_framework import serializers
from records.models import Contact

from authentication.serializers import UserSerializer

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = ['owner', 'phone', 'name']