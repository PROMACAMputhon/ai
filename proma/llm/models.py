from django.db import models

# Create your models here.

class member_tb(models.Model):
    id = models.AutoField(primary_key=True)
    is_login = models.BooleanField(default=False)
    member_login_id = models.CharField(max_length=255)
    member_password = models.CharField(max_length=255)
    member_name = models.CharField(max_length=255)

    class Meta:
        db_table = 'member_tb'

class room_tb(models.Model):
    id = models.AutoField(primary_key=True)
    room_type = models.IntegerField()
    member = models.ForeignKey(member_tb, on_delete=models.CASCADE)

    class Meta:
        db_table = 'room_tb'

class chatting_tb(models.Model):
    id = models.AutoField(primary_key=True)
    answer = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    question = models.CharField(max_length=255)
    room = models.ForeignKey(room_tb, on_delete=models.CASCADE)
    class Meta:
        db_table = 'chatting_tb'