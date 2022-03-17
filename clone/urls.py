from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^search/', views.search_results, name = 'search_results'),
    url(r'^project/(\d+)', views.project, name = 'project'),
    url(r'^accounts/profile/(\d+)', views.profile, name = 'profile'),
    url(r'^new/project/', views.new_project, name = 'new-project'),
    url(r'^accounts/edit-profile/', views.edit_profile, name = 'edit-profile'),
    url(r'^api/profiles/$', views.ProfileList.as_view()),
    url(r'^api/projects/$', views.ProjectList.as_view()),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
