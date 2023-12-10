import os
import json
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime

# def index(request):
#     return render(request, "commerce/index.html",{
#         "a1": auctionlist.objects.filter(active_bool = True),
#             })


def index(request):
    # 获取当前用户的登录状态
    is_user_logged_in = request.user.is_authenticated
    news_data = [{"title": "冬季流感高发，流感疫...", "img": "https://www.chinacdc.cn/yyrdgz/./202312/W020231205263905754100.jpg", "link": "https://www.chinacdc.cn/yyrdgz/./202312/t20231205_271138.html"}, {"title": "如何科学应对冬季呼吸...", "img": "https://www.chinacdc.cn/yyrdgz/./202311/W020231129277108041840.jpg", "link": "https://www.chinacdc.cn/yyrdgz/./202311/t20231129_270935.html"}, {"title": "猴痘疫情监测情况", "img": "https://www.chinacdc.cn/yyrdgz/./202307/W020230714615995831185.jpg", "link": "https://www.chinacdc.cn/yyrdgz/http://www.chinacdc.cn/jkzt/crb/zl/szkb_13037/gwjszl_13092/202311/t20231116_270634.html"}, {"title": "2023年世界慢阻肺日“...", "img": "https://www.chinacdc.cn/yyrdgz/./202311/W020231115378187723504.jpg", "link": "https://www.chinacdc.cn/yyrdgz/./202311/t20231114_270617.html"}, {"title": "全国新型冠状病毒感染...", "img": "https://www.chinacdc.cn/yyrdgz/./202301/W020230114406088376829.jpg", "link": "https://www.chinacdc.cn/yyrdgz/http://www.chinacdc.cn/jkzt/crb/zl/szkb_11803/jszl_13141/202311/t20231110_270578.html"}, {"title": "2023年“世界艾滋病日...", "img": "https://www.chinacdc.cn/yyrdgz/./202311/W020231107287125136089.jpg",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         "link": "https://www.chinacdc.cn/yyrdgz/./202311/t20231107_270525.html"}, {"title": "11.1世界流感日-预防流...", "img": "https://www.chinacdc.cn/yyrdgz/./202311/W020231101548527604336.jpg", "link": "https://www.chinacdc.cn/yyrdgz/./202311/t20231101_270426.html"}, {"title": "“时间就是大脑”，每...", "img": "https://www.chinacdc.cn/yyrdgz/./202310/W020231030422888649147.jpg", "link": "https://www.chinacdc.cn/yyrdgz/./202310/t20231030_270384.html"}, {"title": "10.14世界标准日—“执...", "img": "https://www.chinacdc.cn/yyrdgz/./202310/W020231013326013648689.jpg", "link": "https://www.chinacdc.cn/yyrdgz/./202310/t20231013_270085.html"}, {"title": "2023年中秋国庆假期健...", "img": "https://www.chinacdc.cn/yyrdgz/./202309/W020231007311325547278.jpg", "link": "https://www.chinacdc.cn/yyrdgz/./202309/t20230928_269927.html"}, {"title": "“双节”将至，预防鼠...", "img": "https://www.chinacdc.cn/yyrdgz/./202309/W020230928297183097582.jpg", "link": "https://www.chinacdc.cn/yyrdgz/./202309/t20230927_269897.html"}, {"title": "诺如病毒胃肠炎健康提示", "img": "https://www.chinacdc.cn/yyrdgz/./202309/W020230927506604985904.jpg", "link": "https://www.chinacdc.cn/yyrdgz/./202309/t20230927_269880.html"}]
    news_data = news_data[:3]
    context = {
        'is_user_logged_in': is_user_logged_in,
        'data': news_data
    }

    return render(request, 'index.html', context)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")


@login_required(login_url='login')
def profile(request):
    current_user = request.user

    # 获取用户的个人信息
    user_profile, created = UserProfile.objects.get_or_create(
        user=current_user, defaults={'age': 20, 'gender': 'male', 'class_name': '213'})

    # exercise_logs = ExerciseLog.objects.filter(user=current_user)
    exercise_logs = ExerciseLog.objects.filter(user_profile__user=current_user)

    is_user_logged_in = request.user.is_authenticated

    context = {
        'user_profile': user_profile,
        'exercise_logs': exercise_logs,  # 将用户的打卡记录传递给模板
        'is_user_logged_in': is_user_logged_in
    }

    return render(request, "info.html", context)


@require_http_methods(["GET"])
def news(request):

    current_directory = os.path.dirname(__file__)

    file_path = os.path.join(current_directory, "static/news/news_list.json")

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    return JsonResponse(data, safe=False)


@login_required(login_url='login')
def exercise_check_in(request):
    is_user_logged_in = request.user.is_authenticated
    context = {
        'is_user_logged_in': is_user_logged_in
    }
    if request.method == 'POST':
        location = request.POST.get('location')
        exercise_type = request.POST.get('exercise_type')
        exercise_duration = request.POST.get('exercise_duration')
        date_str = request.POST.get('date')
        print(date_str)
        # 将日期字符串转换为日期对象
        date = datetime.strptime(date_str, '%Y-%m-%d').date()
        print(date)
        # 获取当前用户
        # user = request.user
        user_profile = UserProfile.objects.get(user=request.user)

        # 创建 ExerciseLog 对象并保存到数据库
        ExerciseLog.objects.create(
            user_profile=user_profile,
            location=location,
            exercise_type=exercise_type,
            exercise_duration=exercise_duration,
            date=date,
        )

    return render(request, "exercise_check_in_page.html", context)
