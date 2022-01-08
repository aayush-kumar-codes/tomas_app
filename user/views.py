from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status

from . import serializers
from . import models


class RegisterView(APIView):
    """ User Registeration view """

    def post(self, request):

        # check for required fields
        if not request.data.get('id_number'):
            return Response(data={"error": "true", "message": "id_number is a required field"})
        if not request.data.get('job'):
            return Response(data={"error": "true", "message": "job is a required field"})
        if not request.data.get('address'):
            return Response(data={"error": "true", "message": "address is a required field"})
        if not request.data.get('city'):
            return Response(data={"error": "true", "message": "city is a required field"})

        
        serializer = serializers.RegisterSerializer(data=request.data)

        # if data is valid, create user
        if serializer.is_valid():
            user = serializer.save(password=make_password(request.data.get('password')))

            if not user:
                return Response(data={"error": "true", "details": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
                
            Token.objects.create(user=user)

            return Response(data={"error": "false", "message": "registration successful!"})

        else:
            return Response(data = {"error": True, "errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    """ User Login View """

    def post(self, request):
        email = request.data.get('email')

        # check if email exists
        try:
            models.NewUser.objects.get(email=email)
        except:
            return Response(data={"error": "true", "message": "user with this email doesn't exists."}, status=status.HTTP_404_NOT_FOUND)
 
        # authenticate user's email and password
        user = authenticate(
            email=email, password=request.data.get("password")
        )

        # If authentication is successful return the token
        if user is not None:
            try:
                token = Token.objects.get(user_id=user.id)
            except:
                token = Token.objects.create(user=user)
            return Response({"key": token.key, "error": "false", "message": "Login Successful"})
        else:
            data = {
                "error": "true",
                "field": "password",
                "message": "This password is incorrect, please try again",
            }

            return Response(data, status=status.HTTP_401_UNAUTHORIZED)
