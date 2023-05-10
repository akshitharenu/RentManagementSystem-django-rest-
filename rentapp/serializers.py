from rest_framework import serializers
from .models import twowheeler,customer,contact,booking
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework.exceptions import ValidationError
from django.contrib.auth import authenticate,login
# from django.utils.translation import ugettext_lazy as _

# class RegistrationSerializer(serializers.ModelSerializer):
    # cnfrmpswd=serializers.CharField(style={'input_type':'password'})
    # class Meta:
    #     model=customer
    #     fields=['name','email','phoneno','password','cnfrmpswd']
    #     # extra_kwargs={
    #     #     'password':{'write_olny': True}
    #     # }
    #     def save(self):
    #         customer=customer(
    #             email=self.validated_data['email'],
    #             name=self.validated_data['name']
    #         )
    #         password=self.validated_data['passowrd']
    #         cnfrmpswd=self.validate_data['cnfrmpswd']

    #         if password != cnfrmpswd:
    #             raise ValidationError({"password":"Password doesnot match"})
    #         customer.set_password(password)
    #         customer.save()
    #         return customer
    

    #Serializer to Register User
class RegistrationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=customer.objects.all())]
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    cnfrmpswd = serializers.CharField(write_only=True, required=True)
    class Meta:
        model = customer
        fields = ('name', 'password','email','phoneno','cnfrmpswd')
        extra_kwargs = {
        'phoneno': {'required': True},
      
            }
    def validate(self, attrs):
        if attrs['password'] != attrs['cnfrmpswd']:
            raise serializers.ValidationError(
            {"password": "Password fields didn't match."})
        return attrs
    def create(self, validated_data):
        user = customer.objects.create(
        name=validated_data['name'],
        email=validated_data['email'],
        password=validated_data['password'],
        phoneno=validated_data['phoneno']
        )
        # user.set_password(validated_data['password'])
        user.save()
        return user


# class LoginSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(read_only=True, source="customer.password")
#     class Meta:
#         model = customer
#         fields = (
#             'email',
#             'password'
#         )
       
       
        
class TwowheelerSerializer(serializers.ModelSerializer):
    class Meta:
        model=twowheeler
        fields='__all__'
    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_url(photo_url)

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=contact
        fields='__all__'


class bookingSerializer(serializers.ModelSerializer):

    
   
   
    class Meta:
       
        model=booking
        fields ='__all__'
 

    