from rest_framework.viewsets import ModelViewSet

from bookreaders.serializers import ReaderSerializer
from bookreaders.models import Reader


class ReaderAPI(ModelViewSet):
    queryset = Reader.objects.get_queryset()
    serializer_class = ReaderSerializer
