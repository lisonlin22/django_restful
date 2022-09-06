from rest_framework.response import Response
from rest_framework.views import APIView
from api.utils.serializers import *
from api.utils.filters import *
from api.utils.ModelViewSetStyle import ModelViewSetStyle
from django.core.cache import cache
from django.db.models import Sum, Count
# Create your views here.

class student_view(ModelViewSetStyle):
    """学生列表数据接口"""
    queryset = student.objects.all().order_by('id')
    serializer_class = student_serializer
    filterset_class = student_filter
    search_fields = ['student_name',]

class achievement_view(ModelViewSetStyle):
    """成绩列表数据接口"""
    queryset = achievement.objects.all().order_by('id')
    serializer_class = achievement_serializer
    filterset_class = achievement_filter
    search_fields = ['student__student_name',]

class zongfen(APIView):
    """django orm 计算实例"""
    achievements  = achievement.objects.all()
    def get(self, request, *args, **kwargs):
        # django orm
        res = self.achievements.values('student__student_name').annotate(zongfen=Sum('fraction')) # 分组查询
        return Response({
            "code": 0,
            "msg": '',
            "data": res
        })
