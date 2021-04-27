import json

from django.utils.deprecation import MiddlewareMixin
from django.http.multipartparser import MultiPartParser

from .util import params_error


class MethodConvertMiddleware(MiddlewareMixin):
    '''
    自定义method方法
    '''

    def process_request(self, request):
        method = request.method
        '''
        判断数据类型，对数据进行封装
        '''
        # 判断是否为ajax提交方式
        if 'application/json' in request.META['CONTENT_TYPE']:
            try:
                data = json.loads(request.body.decode())
                files = None
            except Exception as e:
                return params_error({
                    'msg': '请求数据格式错误'
                })
        # 判断是否为form提交方式
        elif 'multipart/form-data' in request.META['CONTENT_TYPE']:
            data, files = MultiPartParser(
                request, request.META, request.META.upload_handlers
            ).parse()
        # 否则为get提交方式
        else:
            data = request.GET
            files = None
        # 判断前端传来的headers中是否含自定义字段
        if 'HTTP_X_METHOD' in request.META:
            # 对ajax传入的方法进行字母格式控制
            method = request.META['HTTP_X_META'].upper()
            # 给request对象赋于method属性
            setattr(request, 'method', method)
        # 判断是否有文件上传
        if files:
            setattr(request, '{method}_FILES'.format(method=method), files)
        # 将data数据添加到method中
        setattr(request, method, data)
