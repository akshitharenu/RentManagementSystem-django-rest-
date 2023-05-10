from django.shortcuts import render
from .serializers import TwowheelerSerializer,RegistrationSerializer,ContactSerializer,bookingSerializer
    
from .models import twowheeler,customer,booking
from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework.response import Response
# from rest_framework.parsers import JSONParser 
from django.contrib.auth import authenticate,login
from rest_framework import status
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
# import json
# Create your views here.
@api_view(['POST','GET'])
def twowheeler_list(request):
    # if request.method=='POST':
    #     twowheeler_data=JSONParser().parse(request)
    #     twowheeler_serializer=TwowheelerSerializer(data=twowheeler)
    #     if twowheeler_serializer.is_valid():
    #         twowheeler_serializer.save()
    #         return Response(twowheeler_serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     
     if request.method == 'POST':
        serializer = TwowheelerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     elif request.method == 'GET':
        twowheelers = twowheeler.objects.all()
        serializer = TwowheelerSerializer(twowheelers, many=True,context={"request":request})
        return Response(serializer.data)

@api_view(['GET','POST'])       
def twowheeler_detail(request,pk):
    if request.method=='GET':
        datas=twowheeler.objects.get(id=pk)
        serializer = TwowheelerSerializer(datas)
        return JsonResponse(serializer.data)
      
    elif request.method=='POST':
        rent=twowheeler.objects.get(id=pk)
        serializer = TwowheelerSerializer(instance=rent,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            # return JsonResponse({"error":1,"msg":"valid registration"})
@api_view(['DELETE',])
def delete(request,pk):
    if request.method=='DELETE':
        rent=twowheeler.objects.get(id=pk)
        rent.delete()
        return JsonResponse({"msg":"deleted successfuly"})

@api_view(['GET'])
def getdata(request):
    if request.method=='GET':
      
        twowheelers = twowheeler.objects.all()
        serializer = TwowheelerSerializer(twowheelers, many=True,context={"request":request})
        return Response(serializer.data)



@api_view(['POST',])

def register(request):
    if request.method=='POST':
        serializer=RegistrationSerializer(data=request.data)
        # data={}
        if serializer.is_valid():
            email=request.POST['email']
            
            send_mail(
                    subject='registered',
                    message='thanks for registering',
                    from_email = settings.EMAIL_HOST_USER,
                    recipient_list = [email,],
                    fail_silently = False,)
            serializer.save()        
            return JsonResponse({
                    "result":0,
                    "msg":"registration successfully"
                
             
                })
            
            # data['serializer']='successfully registered'
            # data['email']=customer.email
            # data['name']=customer.name
        else:
            return JsonResponse({
                        "result":1,
                        "msg":"invalid registration"

                    })
        # return Response(data)

@api_view(['POST'])
def login(request):
    
    if request.method=='POST':
        email = request.data.get('email') if 'email' in request.data else None
        password = request.data.get('password') if 'password' in request.data else None
    
        if not email:
            return Response({"success":False, 'response': {'message': 'Invalid email.'}},
                        status=status.HTTP_400_BAD_REQUEST)
        elif not password:
            return Response({"success":False,'response': {'message': 'Invalid password.'}},
                        status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = customer.objects.get(email=email)
        except:
            return Response({"success":False,'code':500,'response':{'message':'Incorrect User Credentials!'}}
                        )
       

        try:
            password = customer.objects.get(password=password)
        except customer.DoesNotExist as e:
            return Response({"success":False,'code':500,'response':{'message':'Sorry! password wrong!'}}
                        )
                        
        user = authenticate(email=user,password=password)
        return JsonResponse({
            "success":True,
            'code':200,
            'response':{'message': 'login successfully!'},
               
                
            })
        
        
        

@api_view(['POST',])
def contacts(request):
    if request.method=='POST':
        serializer=ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['POST',])
def viewbook(request):
    if request.method == 'POST':
       
        book_serializer = bookingSerializer(data=request.data)
        if book_serializer.is_valid(raise_exception=True):
            book_serializer.save()
            return Response({'success':True,'response':{'message':'booked successfully'}}) 
            