from django.db import models

class Student_de(models.Model):
    status_choice = (
        (0, '上线'),
        (1, '下线'),
    )
    status = models.IntegerField(choices=status_choice, default=1, verbose_name='状态')
    name = models.CharField(max_length=32)
    salary = models.CharField(max_length=32, verbose_name='薪资')
    company = models.CharField(max_length=32, verbose_name='就业单位')
    img = models.ImageField(verbose_name='头像', upload_to='./static/pic')

    class Meta:
        db_table = 'student_de'
        verbose_name = '学生'

    def __str__(self):
        return self.name

class Student(models.Model):
    status_choice = (
        (0, '上线'),
        (1, '下线'),
    )
    status = models.IntegerField(choices=status_choice, default=1,verbose_name='状态')
    name = models.CharField(max_length=32,verbose_name='姓名',unique=True)
    img = models.ImageField(verbose_name='头像',upload_to='./static/pic')
    company = models.CharField(max_length=32,verbose_name='就业单位')
    detail = models.TextField(verbose_name='详细信息')
    salary = models.CharField(max_length=32,verbose_name='薪资')

    class Meta:
        db_table = 'student'
        verbose_name = '学生(详细)'
    def __str__(self):
        return self.name

class News(models.Model):
    status_choice = (
        (0, '上线'),
        (1, '下线'),
    )
    status = models.IntegerField(choices=status_choice, default=1, verbose_name='状态')
    name = models.CharField(max_length=32,verbose_name='标题')
    detail = models.TextField(verbose_name='详情')

    class Meta:
        db_table = 'news'
        verbose_name = '公告'
    def __str__(self):
        return self.name

class Bxslider(models.Model):
    status_choice = (
        (0,'上线'),
        (1,'下线'),
    )
    status = models.IntegerField(choices=status_choice,default=1)
    name = models.CharField(max_length=32,unique=True)
    href = models.CharField(max_length=256,verbose_name='跳转地址')
    img = models.ImageField(upload_to='./static/imag',verbose_name='图片')
    create_time = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'bxsilder'
        verbose_name = '轮播图'

    def __str__(self):
        return self.name

class Course(models.Model):
    status_choice = (
        (0, '上线'),
        (1, '下线'),
    )
    status = models.IntegerField(choices=status_choice, default=1,verbose_name='状态')
    name = models.CharField(max_length=32, unique=True,verbose_name='名称')
    icon = models.ImageField(upload_to='./static/icon',verbose_name='图标')
    summary = models.CharField(max_length=32,verbose_name='摘要')

    class Meta:
        db_table = 'course'
        verbose_name = '课程'

    def __str__(self):
        return self.name

class Level(models.Model):
    name = models.CharField(max_length=32, verbose_name='名称')

    class Meta:
        db_table = 'level'
        verbose_name = '等级'

    def __str__(self):
        return self.name

class Video(models.Model):
    status_choice = (
        (0,'上线'),
        (1,'下线'),
    )
    status = models.IntegerField(choices=status_choice,verbose_name='状态',default=1)
    level = models.ForeignKey(Level,on_delete=models.DO_NOTHING)
    classification = models.ForeignKey('Classification',null=True,blank=True,on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=32,verbose_name='名称')
    href = models.CharField(max_length=256,verbose_name='播放地址')
    img = models.ImageField(verbose_name='封面',upload_to='./static/icon')
    summary = models.CharField(verbose_name='摘要',max_length=32)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'video'
        verbose_name = '视频'

    def __str__(self):
        return self.name

class Classification(models.Model):
    title = models.CharField(max_length=32,verbose_name='名称')

    class Meta:
        db_table = 'classification'
        verbose_name = '分类'

    def __str__(self):
        return self.title

class Direction(models.Model):
    name = models.CharField(max_length=32,verbose_name='名称')
    classification = models.ManyToManyField(Classification)

    class Meta:
        db_table = 'direction'
        verbose_name = '方向'

    def __str__(self):
        return self.name

class Recruit(models.Model):
    status_choice = (
        (0, '上线'),
        (1, '下线'),
    )
    status = models.IntegerField(choices=status_choice, default=1, verbose_name='状态')
    name = models.CharField(max_length=32,verbose_name='题目')
    salary = models.CharField(max_length=64,verbose_name='薪酬')

    class Meta:
        db_table = 'recruit'
        verbose_name = '招聘信息'

    def __str__(self):
        return self.name

class Teacher(models.Model):
    status_choice = (
        (0, '上线'),
        (1, '下线'),
    )
    status = models.IntegerField(choices=status_choice, default=1, verbose_name='状态')
    name = models.CharField(max_length=32,verbose_name='名字')
    img = models.ImageField(verbose_name='头像', upload_to='./static/pic')
    summary = models.CharField(max_length=64,verbose_name='摘要')
    detail = models.CharField(max_length=256,verbose_name='详细')

    class Meta:
        db_table = 'teacher'
        verbose_name = '教师'

    def __str__(self):
        return self.name

class Imgs(models.Model):
    title = models.CharField(max_length=16,verbose_name='标题')
    src = models.ImageField(verbose_name='头像', upload_to='./static/jzx')

    class Meta:
        db_table = 'imgs'
        verbose_name = '照片'

    def __str__(self):
        return self.title
