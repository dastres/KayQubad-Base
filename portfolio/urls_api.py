from django.urls import path, include

app_name = 'portfolio'
urlpatterns = [
    path('', include('portfolio.api.routers'))
]
