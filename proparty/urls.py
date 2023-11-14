
from django.contrib import admin
from django.urls import include, path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views
from .views import get_projects, create_project, delete_project

schema_view = get_schema_view(
   openapi.Info(
      title="ProParty API ",
      default_version='v1',
      description="졸업 작품 api",
      terms_of_service="https://www.google.com/policies/terms/",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("admin/", admin.site.urls),
    path('api/postprojects/list/', views.PostprojectList.as_view(), name='postproject-list'),
    path('api/postprojects/<int:pk>/', views.ProjectDetail.as_view(), name='postproject-detail'),
    path('api/postprojects/create/', views.create_Postproject, name='create_Postproject'),
    path('api/postprojects/delete/<int:project_id>/', views.delete_Postproject, name='delete_Postproject'),
    path('api/team/', views.TeamList.as_view(), name='team-list'),
    path('api/team/<int:team_id>/', views.TeamDetail.as_view(), name='team-detail'),
    path('api/create_team/', views.create_Team, name='create_team'),
    path('api/delete_team/<int:team_id>/', views.delete_Team, name='delete_team'),
    path('api/community/', views.CoumunityList.as_view(), name='community-list'),
    path('api/community/<int:community_id>/', views.CoumunityDetail.as_view(), name='community-detail'),
    path('api/community/create/', views.create_Coumunity, name='create-community'),
    path('api/community/delete/<int:community_id>/', views.delete_Coumunity, name='delete-community'),
    path('api/postteam/list/', views.PostteamList.as_view(), name='postteam-list'),
    path('api/postteam/detail/<int:team_id>/', views.PostteamDetail.as_view(), name='postteam-detail'),
    path('api/postteam/create/', views.create_Postteam, name='create-postteam'),
    path('api/postteam/delete/<int:team_id>/', views.delete_Postteam, name='delete-postteam'),
   path('api/', include([
      path('Project/', views.ProjectList.as_view(), name='project-list'),
      path('Project/<int:pk>/', views.ProjectDetail.as_view(), name='project-detail'),
      path('create_project/', create_project, name='create-project'),
      path('delete_project/<int:project_id>/', delete_project, name='delete-project'),
   ]))
]
