from django.shortcuts import render, HttpResponse, redirect

from rbac.models import *


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    if request.method == "POST":
        username = request.POST.get('username')
        psw = request.POST.get('psw')
        user_obj = UserInfo.objects.filter(name=username, password=psw).first()
        if not user_obj:
            return render(request, 'login.html', {'msg': '用户名或密码错误'})
        else:
            # auth.login(request, user_obj)

            # 获取当前用户的所有权限, 放入session
            permission_queryset = user_obj.roles.filter(permissions__isnull=False).values_list(
                'permissions__url').distinct()  # 去重
            permission_list = [i[0] for i in permission_queryset]
            print('permission_list', permission_list)
            request.session['permission_list'] = permission_list
            return redirect('/customer/list/')
