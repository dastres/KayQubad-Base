from django.urls import path, include

app_name = 'dastres'
urlpatterns = [
    path('', include('dastres.api.routers'))
]
