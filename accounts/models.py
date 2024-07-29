from django.db import models

# Create your models here.
class user(models.Model) :
    name = models.CharField(max_length=100)
    email = models.EmailField

# -- 필드 타입
# 모델의 필드에는 다양한 타입이 있음 ( https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types ) 참고
# CharField -> 제한된 문자열 필드 타입
# TextFile -> 대용량 문자열을 갖는 필드
# IntegerField -> 32 비트 정수형 필드
# BooleanField -> true/ false
# DateTimeField -> 날짜와 시간을 갖는 필드, 날짜만은 DateField, 시간만은 TimeField
# DecimalField -> 소숫점을 갖는 decimal
# BinartField -> 바이너리 데이타
# FileField -> 파일 필드
# ImageField -> 파일 필드의 파생클래스로 이미지 파일 체크
# UUIDField -> UUID 저장 필드