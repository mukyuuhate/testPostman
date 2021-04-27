import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect

from app01.models import User


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
        # req = json.loads(request.body)
        # account = req['account']
        # password = req['password']
        account = request.POST.get('account', None)
        password = request.POST.get('password', None)

        user = User.objects.get(uaccount=account)

        # 模拟判断用户时候存在于数据库的功能
        if password == user.upassword:
            # 登录成功
            result = {
                "msg": 'post接口响应成功\n登录成功!',
                "account": account,
                "password": password,
            }

            # return render(request, 'home.html', {'account': account})
            # return HttpResponse('post接口响应成功\n登录成功, 欢迎回来 杨恒宇 \n    账号信息: ' + account + '\n    '
            #                     + '密码：' + password)
            return JsonResponse(result)

        else:
            # 这是账号密码不对的时候
            # return render(request, 'login.html', {'msg': '账号或密码有误,请检查后登录'})
            # return HttpResponse('post接口响应成功\n但你登录失败了 \n    当前输入的账号信息: ' + account + '\n    '
            #                     + '当前输入的密码密码: ' + password)
            result = {
                "msg": 'post接口响应成功\n登录失败!',
                "account": account,
                "password": password,
            }
            return JsonResponse(result)

    else:
        # 这是GET请求, 则响应到客户端

        account = request.GET.get('account')
        password = request.GET.get('password')

        # 判断account是否存在
        if account:
            # 登录成功
            user = User.objects.get(uaccount=account)
            if (user.upassword == password):
                # return render(request, 'home.html', {'account': account})
                # return HttpResponse('get接口响应成功\n登录成功, 欢迎回来 杨恒宇 \n    账号信息: ' + account + '\n    '
                #                     + '密码: ' + password)
                result = {
                    "msg": 'get接口响应成功\n登录成功!',
                    "account": account,
                    "password": password,
                }
                return JsonResponse(result)

            else:
                # 这是账号密码不对的时候
                # return render(request, 'login.html', {'msg': '账号或密码有误,请检查后登录'})
                # return HttpResponse('get接口响应成功\n但你登录失败了 \n    当前输入的账号信息: ' + account + '\n    '
                #                     + '当前输入的密码密码: ' + password)
                result = {
                    "msg": 'get接口响应成功\n登录失败!',
                    "account": account,
                    "password": password,
                }
                return JsonResponse(result)


# 安全退出的功能
def logout(request):
    # 重定向得到登录页面
    return redirect('/app01/login/')


# 添加账号
def addUser(request):
    if request.POST:
        # 接收数据
        uaccount = request.POST.get('account', None)
        upassword = request.POST.get('password', None)
        if User.objects.filter(uaccount=uaccount):
            result = {
                "msg": '账号已存在',
            }
            return JsonResponse(result)
            # return render(request, 'addUser.html', {'msg': '账号已存在'})
        else:
            # 添加到数据库
            User.objects.create(uaccount=uaccount, upassword=upassword)

            return showUser(request)
    else:
        return render(request, 'addUser.html')


# 删除账号
def deleteUser(request, id):
    User.objects.filter(userno=id).delete()
    return redirect('/app01/showUser')


# 查询所有账号信息
def showUser(request):
    # 首先从数据库中获取所有数据
    userList = User.objects.all()

    # 把数据集合响应到前端
    context = dict()
    context['userList'] = userList

    return render(request, 'showUser.html', context)


# 准备更新部门信息
def preUpdateUserById(request, id):
    # 在数据库查询指定id的信息
    obj = User.objects.get(userno=id)

    context = dict()
    context['user'] = obj

    return render(request, 'updateUser.html', context)


# 更新账号信息
def updateUser(request):
    if request.POST:
        # 接收参数
        userno = request.POST.get('userno', None)
        uaccount = request.POST.get('uaccount', None)
        upassword = request.POST.get('upassword', None)

        # 更新到数据库
        User.objects.filter(userno=userno).update(uaccount=uaccount, upassword=upassword)

        return showUser(request)

