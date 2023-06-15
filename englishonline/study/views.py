import django.middleware.csrf
from django.http import JsonResponse
from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from .models import *
from .serializers import *


def get_csrf_token(request):
    csrf_token = django.middleware.csrf.get_token(request)
    return JsonResponse({'csrf_token': csrf_token})


class RegisterView(generics.CreateAPIView, TokenObtainPairView):
    serializer_class = UserSerializer
    model = User
    permission_classes = (AllowAny,)
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            res = {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }

            return Response({
                "user": serializer.data,
                "refresh": res["refresh"],
                "token": res["access"]
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BaseAudioView(generics.ListAPIView):
    queryset = BaseAudio.objects.all()
    serializer_class = BaseAudioSerializer


# _________ EGE _________


class Task1ViewSet(viewsets.ModelViewSet):
    queryset = Task1.objects.all()
    serializer_class = Task1Serializer


class EGETask2ViewSet(viewsets.ModelViewSet):
    queryset = Task2.objects.all()
    serializer_class = EGETask2Serializer


class EGETask3ViewSet(viewsets.ModelViewSet):
    queryset = Task3.objects.all()
    serializer_class = EGETask3Serializer


class EGETask4ViewSet(viewsets.ModelViewSet):
    queryset = Task4.objects.all()
    serializer_class = EGETask4Serializer


class EGEVariantViewSet(viewsets.ModelViewSet):
    queryset = EGEVariant.objects.all()
    serializer_class = EGEVariantSerializer

    @action(methods=['get'], detail=True)
    def tasks(self, request, pk):
        task1 = Task1.objects.get(egevariant=pk)
        task2 = Task2.objects.get(egevariant=pk)
        task3 = Task3.objects.get(egevariant=pk)
        task4 = Task4.objects.get(egevariant=pk)
        serializer1 = Task1Serializer(task1)
        serializer2 = EGETask2Serializer(task2)
        serializer3 = EGETask3Serializer(task3)
        serializer4 = EGETask4Serializer(task4)
        return Response({'tasks': [serializer1.data, serializer2.data, serializer3.data, serializer4.data]})


# _________ OGE _________


class OGETask2ViewSet(viewsets.ModelViewSet):
    queryset = Task3.objects.all()
    serializer_class = OGETask2Serializer


class OGETask3ViewSet(viewsets.ModelViewSet):
    queryset = Task4.objects.all()
    serializer_class = OGETask3Serializer


class OGEVariantViewSet(viewsets.ModelViewSet):
    queryset = OGEVariant.objects.all()
    serializer_class = OGEVariantSerializer

    @action(methods=['get'], detail=True)
    def tasks(self, request, pk):
        task1 = Task1.objects.get(ogevariant=pk)
        task2 = Task3.objects.get(ogevariant=pk)
        task3 = Task4.objects.get(ogevariant=pk)
        serializer1 = Task1Serializer(task1)
        serializer2 = OGETask2Serializer(task2)
        serializer3 = OGETask3Serializer(task3)
        return Response({'tasks': [serializer1.data, serializer2.data, serializer3.data]})


# _________ VPR _________


class VPRTask2ViewSet(viewsets.ModelViewSet):
    queryset = Task4.objects.all()
    serializer_class = VPRTask2Serializer


class VPRVariantViewSet(viewsets.ModelViewSet):
    queryset = VPRVariant.objects.all()
    serializer_class = VPRVariantSerializer

    @action(methods=['get'], detail=True)
    def tasks(self, request, pk):
        task1 = Task1.objects.get(vprvariant=pk)
        task2 = Task4.objects.get(vprvariant=pk)
        serializer1 = Task1Serializer(task1)
        serializer2 = VPRTask2Serializer(task2)
        return Response({'tasks': [serializer1.data, serializer2.data]})


class EGEPopularityViewSet(viewsets.ModelViewSet):
    queryset = EGEPopularity.objects.all()
    serializer_class = EGEPopularitySerializer


class OGEPopularityViewSet(viewsets.ModelViewSet):
    queryset = OGEPopularity.objects.all()
    serializer_class = OGEPopularitySerializer


class VPRPopularityViewSet(viewsets.ModelViewSet):
    queryset = VPRPopularity.objects.all()
    serializer_class = VPRPopularitySerializer