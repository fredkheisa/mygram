from django.conf.urls import url,include
from . import views

urlpatterns=[
    url('^$',views.profiles_today,name='profilesToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_profiles,name = 'pastProfiles'),

]