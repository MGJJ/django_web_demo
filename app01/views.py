from django.shortcuts import render
from django.http import JsonResponse
from app01 import models

def home(request):
    new_list = models.News.objects.all()
    coures_list = models.Course.objects.all()
    stu_list = models.Student.objects.all()
    recruit_list = models.Recruit.objects.all()
    stud_list = models.Student_de.objects.all()

    return render(
        request,'home.html',
        {
            'new_list':new_list,
            'coures_list':coures_list,
            'stu_list':stu_list,
            'recruit_list':recruit_list,
            'stud_list':stud_list,
        }
    )

def question(request):
    return render(request,'question.html')

def about(request):
    return render(request,'about.html')

def teacher(request):
    tea_list = models.Teacher.objects.all()
    return render(
        request,
        'teacher.html',
        {'tea_list':tea_list}
    )

def student(request):
    return render(request,'student.html')

def get_stu(request):
    nid = request.GET.get('nid')
    stu_list = models.Imgs.objects.filter(id__gt = nid).values('id','title','src')
    stu_list = list(stu_list)
    ret = {
        'status':True,
        'data':stu_list
    }
    return JsonResponse(ret)

def video(request,*args,**kwargs):
    con = {}
    for k, v in kwargs.items():
        temp = int(v)
        kwargs[k] = temp


    direction_id = kwargs.get('direction_id')
    classification_id = kwargs.get('classification_id')
    level_id = kwargs.get('level_id')

    direction_list = models.Direction.objects.all()

    level_list = models.Level.objects.all()

    if  direction_id == 0:
        class_list = models.Classification.objects.all()
        if classification_id == 0:
            pass
        else:
            con['classification_id'] = classification_id
    else:
        direction_obj = models.Direction.objects.filter(id=direction_id).first()
        class_list = direction_obj.classification.all()
        v = direction_obj.classification.all().values_list()
        if not v:
            classification_id_list = []
        else:
            classification_id_list = list(zip(*v))[0]
        if classification_id == 0:
            con['classification_id__in'] = classification_id_list
        else:
            if classification_id in classification_id_list:
                con['classification_id'] = classification_id
            else:
                con['classification_id__in'] = classification_id_list

    if level_id == 0:
        pass
    else:
        con['level_id'] = level_id

    vi_list = models.Video.objects.filter(**con)
    return render(
        request,'video.html',
        {
            'vi_list':vi_list,
            'class_list':class_list,
            'level_list':level_list,
            'direction_list':direction_list,
            'kwargs':kwargs,
        }
    )
