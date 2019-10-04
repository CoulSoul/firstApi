from rest_framework import viewsets

from .models import Poll, Choice, Vote
from .serializers import PollSerializer, ChoiceSerializer, VoteSerializer
from rest_framework import filters

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    filter_backends = (DynamicSearchFilter,)
    serializer_class = PollSerializer
    
    
class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer
    
class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer