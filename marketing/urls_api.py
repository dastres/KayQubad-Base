from django.urls import path, include

app_name = 'marketing'
urlpatterns = [
    path('marketing/', include('marketing.api.routers'))
]
