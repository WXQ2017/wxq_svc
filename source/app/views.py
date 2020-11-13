from django.shortcuts import render, render_to_response

# Create your views here.
from django.shortcuts import render, redirect
from django.template import RequestContext


def login(request):
    error_msg = ""
    if request.method == 'POST':
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        if user == 'admin' and pwd == "admin":
            return redirect('/home')
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
