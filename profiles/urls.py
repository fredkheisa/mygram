from django.conf.urls import url,include
from . import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^today/$',views.profiles_of_day,name='profilesToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_profiles,name = 'pastProfiles'),

]