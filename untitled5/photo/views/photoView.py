from django.http import *
from django.views.generic import View
from ..models import PhotoModel
import os

PHOTO_PATH = './data/photo/'


class PhotoView(View):

    def get(self, request, tid):
        """
        获取照片列表
        :param request:
        :param tid:
        :return:
        """

        photo = PhotoModel.objects.filter(type=int(tid))
        alist = ['http://127.0.0.1:8000/photo/' + str(p.id) for p in photo]

        # print("////////////")

        return JsonResponse({
            "ids": alist
        })


class PhotoGet(View):

    def get(self, request, tid):
        """
        获取图片
        :param request:
        :param tid:
        :return:
        """
        photo = PhotoModel.objects.filter(id=int(tid))

        file_path = (PHOTO_PATH + '404.jpg') if not photo.exists() else photo[0].photo_path
        print(file_path)

        return FileResponse(open(file_path, 'rb'))










