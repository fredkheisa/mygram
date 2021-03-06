from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.landing,name = 'landing'),
    url('^$',views.profiles_today,name='profilesToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_profiles,name = 'pastProfiles'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^picture/(\d+)',views.picture,name ='picture')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
