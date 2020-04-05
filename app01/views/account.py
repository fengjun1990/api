from rest_framework.views import APIView,Response
from app01.utils.md5 import md5
from app01.models import *
import json,re

def get_random_str(user):
    """
    通过时间和md5 生成token值
    :param user:
    :return:
    """
    import hashlib,time
    ctime=str(time.time())

    md5=hashlib.md5(bytes(user,encoding="utf8"))
    md5.update(bytes(ctime,encoding="utf8"))

    return md5.hexdigest()

class LoginView(APIView):
    """用户登录接口
       url:http://127.0.0.1:8000/api/v1/login/
    """
    authentication_classes = [] # 不需要token认证
    def post(self, request,*args,**kwargs):
        user = request.data.get('user')
        pwd = request.data.get('pwd')
        obj = User.objects.filter(name=user, pwd=pwd).first()
        ret = {'code':1000, 'msg':'登录成功'}
        if obj:
            token_str = get_random_str(obj.name)
            Token.objects.update_or_create(user_id=obj.id, defaults={'token':token_str})
            ret['token']=token_str
        else:
            ret['code']=1001
            ret['msg']='用户名或密码错误'


        return Response(json.dumps(ret, ensure_ascii=False))
        # return Response(ret) # 返回一个字典

class RegView(APIView):
    """用户注册接口"""
    authentication_classes = []  # 不需要token认证
    def ret_meg(self,code, msg):
        """
        返回状态码
        :param code:
        :param msg:
        :return:
        """
        ret = {'code': None, 'msg': None}
        ret['code'] = code
        ret['msg'] = msg
        return ret

    def post(self, request, *args, **kwargs):
        # 判断用户信息是否输入完整
        reg_list = []
        for k in request.data:
            reg_list.append(k)

        list_len=len(reg_list)
        if list_len != 5:
            obj=self.ret_meg('1001', '输入的用户信息不完整！')
            return Response(obj)

        # 判断用户信息
        # 1. 用户名是否存在
        user = request.data.get('user')
        obj_user = register.objects.filter(user=user).first()
        if obj_user:
            obj = self.ret_meg('1002', '用户已注册！')
            return Response(obj)

        #2. 密码是否为包含大小写字母和数字
        pwd = request.data.get('pwd')
        if not re.match("^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])).*$", pwd):
            obj = self.ret_meg('1003', '密码必须包含大小写字母和数字!')
            return Response(obj)

        # 3. 密码是否为包含大小写字母和数字
        re_pwd = request.data.get('re_pwd')
        if not re.match("^(?:(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])).*$", re_pwd):
            obj = self.ret_meg('1004', '密码必须包含大小写字母和数字!')
            return Response(obj)

        # 4. 两次输入的密码是否一致
        if not pwd == re_pwd:
            obj = self.ret_meg('1005', '两次输入的密码不一致！')
            return Response(obj)

        # 5. 检查号码长度
        phone_num = request.data.get('phone_num')
        if not len(phone_num) == 11:
            obj = self.ret_meg('1006', '电话号码长度不对！')
            return Response(obj)

        #6.检查邮箱格式
        mail = request.data.get('mail')
        if not '@163.com' in mail:
            obj = self.ret_meg('1007', '邮箱格式不对！')
            return Response(obj)

        # 把数据插入到数据库
        pwd_md5 = md5(pwd)  # 对密码进行md5加密
        reg = register.objects.create(user=user, pwd=pwd_md5, phone_num=phone_num,mail=mail)
        if reg:
            obj = self.ret_meg('1000', '用户注册成功！')
            return Response(obj)
        else:
            obj = self.ret_meg('1008', '用户注册失败成功！')
        return Response(obj)



















