"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from api.utils.auth import Login

router = DefaultRouter()
router.register(r'student', views.student_view, basename="student")  # 向路由器中注册视图集
router.register(r'achievement', views.achievement_view, basename="achievement_view")  # 向路由器中注册视图集

app_name = 'api'
urlpatterns = [
    path("login/", Login.as_view(), name="login"), # 登录认证
    path('zongfen/', views.zongfen.as_view(), name='zongfen'),

]
urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中
