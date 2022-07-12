import json

from rest_framework.generics import ListAPIView, GenericAPIView, get_object_or_404
from api.models import Employee
from api.serializers import EmployeeSerializer, RegistrationSerializer
from rest_framework import filters
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response


class EmployeeListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'surname', 'name', 'patronymic', 'position',
        'employment_date', 'salary'
    ]

    ordering_fields = [
        'position', 'employment_date', 'salary'
    ]


class RegistrationApiView(GenericAPIView):
    serializer_class = RegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(GenericAPIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class EmployeeApiCreateView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        data = json.loads(self.request.body)
        serializer = EmployeeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeApiUpdateView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer

    def put(self, request, *args, **kwargs):
        employee_id = get_object_or_404(Employee, pk=self.kwargs.get('pk'))
        data = json.loads(self.request.body)
        serializer = EmployeeSerializer(employee_id, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class EmployeeDetailApiView(GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        employee_id = get_object_or_404(Employee, pk=self.kwargs.get('pk'))
        serializer = EmployeeSerializer(employee_id)
        return Response(serializer.data)
