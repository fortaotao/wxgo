from django.db import models


class PhotoModel(models.Model):

    class Meta:
        verbose_name = "照片表"
        verbose_name_plural = "照片表"

    # 照片分类
    type = models.PositiveSmallIntegerField({
        "own": 1,
        "school": 2
    })

    # 照片地址
    photo_path = models.CharField(max_length=200, default='', blank=True)


    def __str__(self):
        return "[分类] %s [地址] %s" % ("type", self.photo_path)
