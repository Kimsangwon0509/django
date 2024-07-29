from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login

# https://velog.io/@swhan9404/django%EC%9D%98-Auth-%EB%A1%9C%EA%B7%B8%EC%9D%B8-%ED%9A%8C%EC%9B%90%EA%B0%80%EC%9E%85-%EB%93%B1
# http://pythonstudy.xyz/python/article/304-Django-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8
# view.py는 데이터를 MODEl에서 가져와 가공하여, 웹페이즈 결과를 만들도록 컨트롤 하는 역활을 한다.
# views. py 안에 있는 하나의 함수 (또는 클래스)가 하나의 view를 정의한다.
# view는 http request 를 입력 parameter로 받아들이고, http response를 리턴한다.

# Create your views here.
def login(request) :
    if request.method == 'POST' :
        # data는 forms.form 두번째 인자이므로 data = 은 생략 가능
        form = AuthenticationForm(request, data = request.POST) # 먼저 request 인자를 받아야함
        if form.is_valid() :
            # 세션 CREATE/ form.get_user 는 User 객체 반환
            auth_login(request, form.get_user())
            return redirect('articles:index')
        else :
            form = AuthenticationForm()

        context = {
            'form' : form,
        }
        return render(request, 'accounts/login.html', context)

def index(request) :
    return HttpResponse("Hello, world!")
