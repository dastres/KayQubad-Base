from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns_api_v1 = [
    path('', include('blog.urls_api'), name='main_blog'),
    path('', include('accounts.urls_api'), name='main_accounts'),
    path('', include('project.urls_api'), name='main_project'),
    path('', include('portfolio.urls_api'), name='main_portfolio'),
    path('', include('page.urls_api'), name='main_page'),
    path('', include('forms.urls_api'), name='main_forms'),
    path('', include('marketing.urls_api'), name='main_marketing'),
    path('', include('dastres.urls_api'), name='main_dastres'),
    path('', include('service.urls_api'), name='main_service'),

]

urlpatterns = i18n_patterns(
    # urls admin
    # path('admin/', admin.site.urls, name="admin_urls"),

    # urls drf_spectacular
    path('', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/v1/schema/', SpectacularAPIView.as_view(api_version='v1'), name='schema'),
    path('api/v1/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

    # urls api
    path('api/v1/', include(urlpatterns_api_v1), name="api_urls"),

    # urls CkEditor
    path('ckeditor/', include('ckeditor_uploader.urls'), name="CKEditor_URL"),

)

# _______________________________ Static Config __________________________________________
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
