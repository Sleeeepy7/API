
from django.urls import path
from .views import *

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('service', ServiceApi, basename='users')

urlpatterns = router.urls

# urlpatterns = [
#     path('service/', ServiceList.as_view()),
#     path('service/<int:pk>/', ServiceDetail.as_view()),
# ]
