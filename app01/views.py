from django.http import HttpResponse
from django.shortcuts import render, redirect

# 进入到主页
def index(request):
    return render(request, 'index.html')


# 进入到home页面
def home(request):
    # 获取session中的登录用户
    account = request.session.get('account', None)
    # [测试] 打印输出该用户
    print('account: {0}'.format(account))

    # 判读使用获取到了用户信息
    if not account:
        # 这是没有用户登录, 则跳转到登录页
        return redirect('/app01/login/')
    else:
        # 获取到了登录用户, 则跳转到home页面
        return render(request, 'home.html', {'account': account})


# 登录功能
def login(request):
    # 判断是否是post请求
    if request.POST:
        # 获取用户信息
        account = request.POST.get('account', None)
        password = request.POST.get('password', None)

        # 模拟判断用户时候存在于数据库的功能
        if account == 'mukyuuhate' and password == '123':
            # 登录成功

            # return render(request, 'home.html', {'account': account})
            return HttpResponse('post接口响应成功\n登录成功, 欢迎回来 杨恒宇 \n    账号信息: ' + account + '\n    '
                                + '密码：' + password)

        else:
            # 这是账号密码不对的时候
            # return render(request, 'login.html', {'msg': '账号或密码有误,请检查后登录'})
            return HttpResponse('post接口响应成功\n但你登录失败了 \n    当前输入的账号信息: ' + account + '\n    '
                                + '当前输入的密码密码: ' + password)

    else:
        # 这是GET请求, 则响应到客户端

        account = request.GET.get('account')
        password = request.GET.get('password')

        # 判断account是否存在
        if account == 'mukyuuhate' and password == '123':
            # 登录成功
            # return render(request, 'home.html', {'account': account})
            return HttpResponse('get接口响应成功\n登录成功, 欢迎回来 杨恒宇 \n    账号信息: ' + account + '\n    '
                                + '密码: ' + password)

        else:
            # 这是账号密码不对的时候
            # return render(request, 'login.html', {'msg': '账号或密码有误,请检查后登录'})
            return HttpResponse('get接口响应成功\n但你登录失败了 \n    当前输入的账号信息: ' + account + '\n    '
                                + '当前输入的密码密码: ' + password)


# 安全退出的功能
def logout(request):

    # 重定向得到登录页面
    return redirect('/app01/login/')