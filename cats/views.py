from rest_framework import viewsets
from rest_framework.response import Response

from cats.models import SpyCat, Mission, Target
from cats.serializers import SpyCatSerializer, MissionSerializer, TargetSerializer


class SpyCatViewSet(viewsets.ModelViewSet):
    queryset = SpyCat.objects.all()
    serializer_class = SpyCatSerializer

    def create(self, request, *args, **kwargs):
        # Validate the request data before proceeding
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # If the breed is valid, proceed with saving the cat
            serializer.save()
            return Response(serializer.data, status=201)  # Created
        else:
            # If validation fails, return the errors with a bad request status
            return Response(serializer.errors, status=400)


class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer


class TargetViewSet(viewsets.ModelViewSet):
    queryset = Target.objects.all()
    serializer_class = TargetSerializer
