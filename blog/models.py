from django.db import models
from django.conf import settings
from django.utils import timezone
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField(
        blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
'''
#데이터 베이스에 접속한다.
DATABASES = create_engine(settings.SQLALCHEMY_DATABASE_URL, echo = True)

# orm과의 매핑을 명시하는 함수를 선언한다.
Base = declarative_base()

class Tada(Base) :

    __tablename__ = 'tada'

    id       = Column(Integer, primary_key=True)
    name     = Column(String(50))
    fullname = Column(String(50))
    password = Column(String(50))

    def __init__(self, name, fullname, password):

        self.name     = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<Tada('%s', '%s', '%s')>" % (self.name, self.fullname, self.password)

if __name__ == '__main__':

    Base.metadata.create_all(DATABASES)

    # 세션을 만들어서 연결시킨다.
    Session = sessionmaker()
    Session.configure(bind=DATABASES)
    session = Session()

    # 위의 클래스,인스턴스 변수를 지킨 다음에
    tada = Tada('ks','ks','1111')

    # 세션에 추가를 한다.
    session.add(tada)
    session.commit()
    '''