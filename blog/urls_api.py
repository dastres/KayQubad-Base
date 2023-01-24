from django.urls import path, include

urlpatterns = [
    # api
    path('blog/', include('blog.api.router')),
]
