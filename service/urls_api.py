from django.urls import path, include

app_name = 'service'
urlpatterns = [
    path('service/', include('service.api.router'))
]
