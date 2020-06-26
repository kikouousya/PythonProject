
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, render
import re

class CheckPermission(MiddlewareMixin):
    """
    用户权限校验中间件
    """
    def process_request(self, request):
        current_url = request.path_info
        permission_urls = request.session.get('permission_list')
        print('current_rul permission_urls: ',current_url, permission_urls)
        while 1:
            if current_url == '/login/':
                break
            if not permission_urls:
                return HttpResponse('please login first')
            for each_url in permission_urls:
                if re.match("^%s$" % each_url, current_url):  # 用正则来匹配这个地址, 同时需要增加起始和终止符
                    break
            else:
                return HttpResponse('500 forbidden')

