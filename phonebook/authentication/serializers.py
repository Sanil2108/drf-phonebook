from rest_framework import serializers
from authentication.models import User

# from records.serializers import ContactSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

# class AllContactsSerializer(serializers.Serializer):
#     contacts = ContactSerializer(many = True)

#     def create(self, validated_data):
