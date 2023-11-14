from rest_framework import generics
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Projects, Postproject, Team,Coumunity, Postteam
from .serializers import ProjectSerializer, PostProjectSerializer, TeamSerializer,CoumunitySerializer, PostteamSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status

@swagger_auto_schema(
    method='GET',
    tags=["Project"],  # "Project" 태그를 추가합니다.
)
@api_view(['GET'])
def get_projects(request):
    projects = Projects.objects.all()
    serializer = ProjectSerializer(projects, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
    tags=["Project"],  # "Project" 태그를 추가합니다.
)
class ProjectList(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
@swagger_auto_schema(
    tags=["Project"],  # "Project" 태그를 추가합니다.
)
class ProjectDetail(generics.RetrieveAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer

@swagger_auto_schema(
    method='POST',  # POST 메서드에 대한 문서화 설정
    tags=["Project"],
    request_body=ProjectSerializer,  # 입력 데이터의 시리얼라이저를 지정합니다.
)
@api_view(['POST'])
def create_project(request):
    if request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='DELETE',
    tags=["Project"],  # "Project" 태그를 추가합니다.
)
@api_view(['DELETE'])
def delete_project(request, project_id):
    try:
        project = Projects.objects.get(id=project_id)
    except Projects.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@swagger_auto_schema(
    method='GET',
    tags=["Postproject"],  # "Project" 태그를 추가합니다.
)
@api_view(['GET'])
def get_Postproject(request):
    Postproject = Postproject.objects.all()
    serializer = PostProjectSerializer(Postproject, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
    tags=["Postproject"],  # "Project" 태그를 추가합니다.
)
class PostprojectList(generics.ListAPIView):
    queryset = Postproject.objects.all()
    serializer_class = PostProjectSerializer

@swagger_auto_schema(
    tags=["Postproject"],  # "Project" 태그를 추가합니다.
)
class ProjectDetail(generics.RetrieveAPIView):
    queryset =  Postproject.objects.all()
    serializer_class = PostProjectSerializer

@swagger_auto_schema(
    method='POST',  # POST 메서드에 대한 문서화 설정
    tags=["postprojects"],
    request_body=PostProjectSerializer,  # 입력 데이터의 시리얼라이저를 지정합니다.
)
@api_view(['POST'])
def create_Postproject(request):
    if request.method == 'POST':
        serializer = PostProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='DELETE',
    tags=["postprojects"],  # "Project" 태그를 추가합니다.
)
@api_view(['DELETE'])
def delete_Postproject(request, project_id):
    try:
        project = Postproject.objects.get(id=project_id)
    except Postproject.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    




    
@swagger_auto_schema(
    method='GET',
    tags=["Team"],  # "Project" 태그를 추가합니다.
)
@api_view(['GET'])
def get_Team(request):
    Postproject = Team.objects.all()
    serializer = TeamSerializer(Postproject, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
    tags=["Team"],  # "Project" 태그를 추가합니다.
)
class TeamList(generics.ListAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

@swagger_auto_schema(
    tags=["Team"],  # "Project" 태그를 추가합니다.
)
class TeamDetail(generics.RetrieveAPIView):
    queryset =  Team.objects.all()
    serializer_class = TeamSerializer

@swagger_auto_schema(
    method='POST',  # POST 메서드에 대한 문서화 설정
    tags=["team"],
    request_body=TeamSerializer,  # 입력 데이터의 시리얼라이저를 지정합니다.
)
@api_view(['POST'])
def create_Team(request):
    if request.method == 'POST':
        serializer = TeamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='DELETE',
    tags=["team"],  # "Project" 태그를 추가합니다.
)
@api_view(['DELETE'])
def delete_Team(request, project_id):
    try:
        project = Team.objects.get(id=project_id)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@swagger_auto_schema(
    method='GET',
    tags=["Coumunity"],  # "Project" 태그를 추가합니다.
)
@api_view(['GET'])
def get_Coumunity(request):
    Postproject = Coumunity.objects.all()
    serializer = CoumunitySerializer(Postproject, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
    tags=["Coumunity"],  # "Project" 태그를 추가합니다.
)
class CoumunityList(generics.ListAPIView):
    queryset = Coumunity.objects.all()
    serializer_class = CoumunitySerializer

@swagger_auto_schema(
    tags=["Coumunity"],  # "Project" 태그를 추가합니다.
)
class CoumunityDetail(generics.RetrieveAPIView):
    queryset =  Coumunity.objects.all()
    serializer_class = CoumunitySerializer

@swagger_auto_schema(
    method='POST',  # POST 메서드에 대한 문서화 설정
    tags=["community"],
    request_body=CoumunitySerializer,  # 입력 데이터의 시리얼라이저를 지정합니다.
)
@api_view(['POST'])
def create_Coumunity(request):
    if request.method == 'POST':
        serializer = CoumunitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='DELETE',
    tags=["community"],  # "Project" 태그를 추가합니다.
)
@api_view(['DELETE'])
def delete_Coumunity(request, project_id):
    try:
        project = Coumunity.objects.get(id=project_id)
    except Coumunity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    

@swagger_auto_schema(
    method='GET',
    tags=["Postteam"],  # "Project" 태그를 추가합니다.
)
@api_view(['GET'])
def get_Postteam(request):
    Postproject = Postteam.objects.all()
    serializer = PostteamSerializer(Postproject, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
    tags=["postteam"],  # "Project" 태그를 추가합니다.
)
class PostteamList(generics.ListAPIView):
    queryset = Postteam.objects.all()
    serializer_class = PostteamSerializer

@swagger_auto_schema(
    tags=["postteam"],  # "Project" 태그를 추가합니다.
)
class PostteamDetail(generics.RetrieveAPIView):
    queryset =  Postteam.objects.all()
    serializer_class = PostteamSerializer

@swagger_auto_schema(
    method='POST',  # POST 메서드에 대한 문서화 설정
    tags=["postteam"],
    request_body=PostteamSerializer,  # 입력 데이터의 시리얼라이저를 지정합니다.
)
@api_view(['POST'])
def create_Postteam(request):
    if request.method == 'POST':
        serializer = PostteamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    method='DELETE',
    tags=["postteam"],  # "Project" 태그를 추가합니다.
)
@api_view(['DELETE'])
def delete_Postteam(request, project_id):
    try:
        project = Postteam.objects.get(id=project_id)
    except Postteam.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)