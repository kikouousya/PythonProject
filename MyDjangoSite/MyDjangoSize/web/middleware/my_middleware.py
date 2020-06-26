
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, render


class CheckPermission(MiddlewareMixin):
    """
    用户权限校验中间件
    """
    def process_requeset(self, request):
        current_url = request.path_info
        permission_urls = request.settion.get('permission_list')
        print('current_rul permission_urls: ',current_url, permission_urls)
        while 1:
            if current_url == '/login/':
                break
            if not permission_urls:
                return HttpResponse('please login first')
            if current_url not in permission_urls:
                return HttpResponse('500 forbidden')

