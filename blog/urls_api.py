from django.urls import path, include

app_name = 'blog'
urlpatterns = [
    # api
    path('blog/', include('blog.api.router')),
]
