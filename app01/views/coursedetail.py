from rest_framework.viewsets import ModelViewSet,ViewSetMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from app01.serial import *
from app01.models import *

class CourseDetailView(ModelViewSet):
    def list(self, request, *args, **kwargs):
        ret = {'code':1000, 'data':None}
        try:
            obj=CourseDetail.objects.all()
            ser=CourseDetailSerializers(instance=obj, many=True)
            ret['date']=ser.data
        except Exception as e:
            ret['code']=1001
            ret['error']='获取课程详情失败'

        return Response(ret)

    def retrieve(self, request, *args, **kwargs):
        ret = {'code': 1000, 'data': None}
        pk=kwargs.get('pk')
        obj=CourseDetail.objects.filter(id=pk).first()
        if obj:
            ser=CourseDetailSerializers(instance=obj, many=False)
            ret['data']=ser.data
        else:
            ret['code']=1001
            ret['error']="用户信息未查找到！"

        return Response(ret)

class CourseView(APIView):
    def get(self, request, *args, **kwargs):
        """
        课程列表接口
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code':1000, 'data':None}
        try:
            obj_data=Course.objects.all()
            ser = CourseSerializers(instance=obj_data, many=True)
            ret['data']=ser.data
        except Exception as e:
            ret['code']=1001
            ret['error']='获取课程失败'

        return  Response(ret)



