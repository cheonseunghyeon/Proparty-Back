from django.contrib import admin
from .models import Projects  # Models.py에서 정의한 모델을 import

admin.site.register(Projects)  # 모델을 관리자 페이지에 등록
