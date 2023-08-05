from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from django.urls import reverse
from django.template import loader
# Create your views here.


job_title = [
    "First job",
    "Second job",
    "third job"
]

job_description = [
    "First job description",
    "Second job description",
    "third job description"
]


class TempClass:
    x = 5




def hello(request):
    #template = loader.get_template('app/hello.html')
    list = ["alpha","Beta"]
    temp = TempClass()
    is_authenticated = True
    context = {"name":"django","first_list":list,"temp_object":temp,"age":27,"is_authenticated":is_authenticated}
    #return HttpResponse(template.render(context,request))
    return render(request,"app/hello.html",context)


def job_list(request):
    # list_of_jobs = "<ul>"
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     detail_url=reverse('jobs_detail',args=(job_id,))
    #     list_of_jobs += f"<li><a href='{detail_url}'>{j}</li>"
    # list_of_jobs += "</ul>"
    # return HttpResponse(list_of_jobs)
    context = {"job_title_list":job_title}
    return render(request,"app/index.html",context)

def jobDetail(request,id):
    try:    
        if id == 0 :
            return redirect(reverse('jobs_home'))
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        # return HttpResponse(return_html)
        context = {"job_title":job_title[id],"job_description":job_description[id]}
        return render(request,"app/job_detail.html",context)
    except:
        return HttpResponseNotFound()
