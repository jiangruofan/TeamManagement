from email.policy import default
from urllib import request
from django.http import HttpResponse, JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MemberSerializer
from .models import Member
from django.db import connection

# Create your views here.

class Add(APIView):
    serializer_class = MemberSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            phoneNumber = serializer.data.get('phoneNumber')
            email = serializer.data.get('email')
            queryset = Member.objects.filter(phoneNumber=phoneNumber)
            queryset1 = Member.objects.filter(email=email)
            if queryset.exists() or queryset1.exists():
                return Response({'msg': 'Member already exists.'}, status=status.HTTP_403_FORBIDDEN)
            first_name = serializer.data.get('first_name')
            last_name = serializer.data.get('last_name')
            is_admin = serializer.data.get('is_admin')
            member = Member(first_name=first_name, last_name=last_name, phoneNumber=phoneNumber, email=email, is_admin=is_admin)
            member.save()
            return Response(MemberSerializer(member).data, status=status.HTTP_201_CREATED)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)

class Get(APIView):

    def get(self, request):
        queryset = Member.objects.all()
        data = []
        for val in queryset:
            data.append(MemberSerializer(val).data)
        return Response(data, status=status.HTTP_200_OK)

class Delete(APIView):

    def delete(self, request):
        id = request.GET.get('id')
        if id:
            member = Member.objects.filter(id=id)
            if not member:
                return Response({'ID Not Found in Database': 'Invalid ID.'}, status=status.HTTP_404_NOT_FOUND)
            member[0].delete()
            return Response({'Message': 'Success'}, status=status.HTTP_200_OK)
        return Response({'Bad Request': 'ID not found in request'}, status=status.HTTP_400_BAD_REQUEST)

class Update(APIView):
    serializer_class = MemberSerializer

    def put(self, request):
        id = request.GET.get('id')
        if not id:
            return Response({'Bad Request': 'ID not found in request'}, status=status.HTTP_400_BAD_REQUEST)
        member = Member.objects.filter(id=id)
        if not member:
            return Response({'ID Not Found in Database': 'Invalid ID.'}, status=status.HTTP_404_NOT_FOUND)
        list1 = []
        query = ''
        field = ['first_name', 'last_name', 'phoneNumber', 'email', 'is_admin']
        for s in field:
            s1 = request.data.get(s)
            if s1:
                query += s + '= %s,'
                list1.append(s1)
        list1.append(str(id))

        with connection.cursor() as cursor:
            cursor.execute("UPDATE api_member SET " + query[:-1] + " WHERE id= %s", list1)

        return Response(MemberSerializer(Member.objects.filter(id=id)[0]).data, status=status.HTTP_200_OK)




        

