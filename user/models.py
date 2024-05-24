from django.db import models


class User(models.Model):
    username = models.CharField(max_length=64, verbose_name='사용자명')
    password = models.CharField(max_length=65, verbose_name='비밀번호')
    email = models.CharField(max_length=50, verbose_name="이메일", null=True)
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')

    class Meta:
        db_table = 'buptle_user'
        verbose_name = '사용자'
        verbose_name_plural = '사용자'

    def __str__(self):
        return self.username
