# 관리자 권한을 가지는 사용자가 퀴즈 모델을 관리할 수 있도록 설정하는 파일
from django.contrib import admin
from .models import Quiz

# Register your models here.
admin.site.register(Quiz)   