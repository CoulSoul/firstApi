from rest_framework.routers import DefaultRouter
from .apiviews import PollViewSet, ChoiceViewSet, VoteViewSet


router = DefaultRouter()
router.register('polls', PollViewSet, base_name='polls'),
router.register('choice', ChoiceViewSet, base_name='choice'),
router.register('vote', VoteViewSet, base_name='vote'),


urlpatterns = [
    # ...
]

urlpatterns += router.urls