from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response

from .serializer import GetUserSerializer, UserCreateSerializer, BlockedIPSerializer
from .models import MyUser as User, BlockedIP


class GetUser(generics.RetrieveAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = GetUserSerializer
    queryset = User.objects.all()
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        serializer = GetUserSerializer(self.get_object())
        return Response(serializer.data)


class GetUsers(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = GetUserSerializer
    queryset = User.objects.all()


class CreateUser(generics.CreateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = UserCreateSerializer

    def post(self, request, format=None):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class UpdateUser(generics.UpdateAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    lookup_field = "id"

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = UserCreateSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )


class DeleteUser(generics.DestroyAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = GetUserSerializer
    queryset = User.objects.all()
    lookup_field = "id"

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BlockedIPCreateAPIView(generics.CreateAPIView):
    serializer_class = BlockedIPSerializer
    queryset = BlockedIP.objects.all()
