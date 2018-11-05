from django.conf.urls import url
from booktest import views

# 引入视图模块
urlpatterns = [
    # 配置首页url
    url(r"^$", views.index),
    # 配置详细页url， \d+表示多个数字，小括号用于取值
    url(r"^(\d+)/$", views.detail)
]