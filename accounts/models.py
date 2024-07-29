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

# -- 필드 옵션
# null -> null= true 이면 , Empty 값을 DB 에 Null로 저장
# blank -> blank= false이면 필드가 required 필드이다.
# primary_key -> 해당 필드가 primary key 임을 표시
# unique -> 해당 필드가 테이블에서 unique함을 표시
# default -> 필드의 디폴트 값을 지정 ex) models.CharField(max_length = 2, default = "WA")
# db_column -> 컬럼명은 디폴트로 필드명을 사용하는데, 만약 다르게 쓸 경우 지정
