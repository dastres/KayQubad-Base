from django.urls import path, include

app_name = 'project'
urlpatterns = [
    path('', include('project.api.routers'))
]
