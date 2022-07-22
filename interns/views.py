from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from interns.models import employee
from interns.serializers import employeeSerializer


class empListView(APIView):
    def get(self, request):
        emp = employee.objects.all()
        emp_serializer = employeeSerializer(emp, many=True)
        resp1 = {
            "code": 1,
            "message": "GET list success",
            "result": emp_serializer.data
        }

        return Response(data=resp1, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = employeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            resp2 = {
                "code": 1,
                "message": "POST success",
                "result": serializer.data
            }
            return Response(resp2, status=status.HTTP_200_OK)
        else:
            resp3 = {
                "code": 0,
                "message": "POST Unsuccess",
                "result": serializer.errors
            }
            return Response(resp3)


class empDetailView(APIView):

    def get(self, request, pk):
        emp = employee.objects.get(pk=pk)
        emp_serializer = employeeSerializer(emp, many=False)
        resp1 = {
            "code": 1,
            "message": " Employee Detail",
            "result": emp_serializer.data
        }
        return Response(data=resp1, status=status.HTTP_200_OK)

    def put(self, request, pk):
        emp = employee.objects.get(pk=pk)
        emp_serializer = employeeSerializer(emp, data=request.data)
        if emp_serializer.is_valid():
            emp_serializer.save()
            resp4 = {
                "code": 1,
                "message": "Updated Successfully",
                "result": emp_serializer.data
            }
            return Response(data=resp4, status=status.HTTP_200_OK)
        # return Response(emp_serializer.data)
        else:
            return Response(emp_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        emp = employee.objects.get(pk=pk)
        emp.delete()
        resp5 = {
            "code": 1,
            "message": "Deleted Successfully",
        }
        return Response(data=resp5, status=status.HTTP_200_OK)
