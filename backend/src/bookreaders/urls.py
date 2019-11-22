from django.urls import path, include
from rest_framework import routers

from bookreaders.viewsets import ReaderAPI
from bookreaders.views import some_streaming_csv_view

router = routers.DefaultRouter()

router.register('reader', ReaderAPI, basename='reader')

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('csv', some_streaming_csv_view)
    # path(
    #     'api/v1/api-auth/',
    #     include('rest_framework.urls', namespace='rest_framework')
    # ),
]
