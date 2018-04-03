# !/usr/bin/env python3
# -*- coding:utf-8 -*-
from tornado import web ,ioloop,httpserver
from create_qr_code import get_code_by_str





    #把数据落地--写一个csv文件/存储到数据库
SIGN_FILE_HANDLER = open('sign.csv','a')
SIGN_FILE_HANDLER.write('姓名,职业,年龄\n')



    #业务部分--返回什么数据
class MainPageHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('index.html')


    #生成二维码
class CodeHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        img_io_obj = get_code_by_str('http://www.baidu.com')
        self.write(img_io_obj.getvalue()) #得到二维码图像二进制数据

    #签到模块
class SignHandler(web.RequestHandler):
    def get(self,*args,**kwargs):
        self.render('sign.html')

    def post(self, *args, **kwargs):
        name = self.get_argument('name')
        job = self.get_argument('job')
        age = self.get_argument('age')
        time = self.get_argument('time')
        # print(name,job,age)
        #写CSV文件
        SIGN_FILE_HANDLER.write('%s,%s,%s,%s,\n' % (name,job,age,time))
        SIGN_FILE_HANDLER.flush()
        self.write("签到成功")

    #路由---分发任务(请求什么数据)

application = web.Application([(r"/index",MainPageHandler),
                               (r"/code",CodeHandler),
                               (r"/sign",SignHandler),
                               ])

if __name__ == '__main__':
    #socket服务----总服务台
    http_server = httpserver.HTTPServer(application)
    http_server.listen(9995)
    ioloop.IOLoop.current().start()

