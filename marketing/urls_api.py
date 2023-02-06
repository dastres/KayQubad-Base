from django.urls import path, include

app_name = 'marketing'
urlpatterns = [
    path('', include('marketing.api.routers'))
]
