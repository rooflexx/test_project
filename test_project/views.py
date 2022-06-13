from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.parsers import FormParser, JSONParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from test_project.serializers import HealthCheckSerializer

class HealthCheckView(ListAPIView):
    """Check the health of the service."""

    serializer_class = HealthCheckSerializer
    parser_classes = [JSONParser]

    @extend_schema(
        responses={201: HealthCheckSerializer(many=False)},
    )
    def get(self, request, *args, **kwargs):
        return Response({"message": "Running!!!"})
