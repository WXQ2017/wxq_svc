from django.shortcuts import render, render_to_response

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse

def login(request):
    error_msg = ""
    if request.method == 'POST':
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        # return render(request, 'login.html', {
        #     'error_msg': User.objects.all() // 查询所有auth_user表结果
        # })
        if user and pwd:
            c = User.objects.filter(username=user, password=pwd).count()  # 根据某个条件查询
            if c == 1:
                # return HttpResponse('登录成功')
                return redirect('/home')
            else:
                error_msg = '用户名或密码错误!'
        else:
            error_msg = '想进去没门!!'
    return render(request, 'login.html', {'error_msg': error_msg})

USER_INFO = []
def home(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        s = request.POST.get('sex')
        a = request.POST.get('age')
        temp = {'username': u, 'sex': s, 'age': a}
        USER_INFO.append(temp)
    return render(request, 'home.html', {'user_info': USER_INFO})