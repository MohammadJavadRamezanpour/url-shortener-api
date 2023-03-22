from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser


from .models import Link
from .serializers import LinkSerializer

class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
    lookup_field = 'key'

    def get_serializer_context(self):
        return {"domain": self.request.META["HTTP_HOST"]}
    

    def get_permissions(self):
        if self.action in ['create', 'retrieve']:
            return [AllowAny()]
        return [IsAdminUser()]


    def retrieve(self, request, key=None):
        try:
            shortened_url = Link.objects.get(key=key)
        except Link.DoesNotExist:
            return Response({'detail': 'Shortened URL not found.'}, status=status.HTTP_404_NOT_FOUND)
        shortened_url.access_count += 1
        shortened_url.save()
        serializer = self.get_serializer(shortened_url)
        return Response(serializer.data, status=status.HTTP_200_OK)