from django.db import models

# Create your models here.

class student(models.Model):
    """学生列表"""
    student_name = models.CharField(max_length=20, verbose_name="学生名称",)
    student_number = models.CharField(max_length=50, verbose_name="联系电话",)
    student_address = models.CharField(max_length=200, verbose_name="联系地址", null=True, default='中国')
    student_date = models.DateField(verbose_name="出生日期", null=True, default="1999-01-01")
    class Meta:
        verbose_name = "学生列表"
        permissions = (
            ("view_student", "Can view student"),
        )

class achievement(models.Model):
    """成绩表"""
    fraction = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="成绩分数")
    subject = models.CharField(max_length=50, verbose_name="科目",)
    student = models.ForeignKey(student, verbose_name="学生ID", on_delete=models.CASCADE)
    class Meta:
        verbose_name = "成绩表"
        permissions = (
            ("view_achievement", "Can view achievement"),
        )