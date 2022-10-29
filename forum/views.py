from datetime import datetime
from django.shortcuts import render,redirect
from forum.models import ForumUMKM, Replies
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.core import serializers

def show_json(request,kategori_inputuser):
    if kategori_inputuser == "semua":
        data = ForumUMKM.objects.all().order_by('-time')
        return HttpResponse(serializers.serialize("json", data))

    elif kategori_inputuser == "makanan":
        data = ForumUMKM.objects.filter(kategori=kategori_inputuser).order_by('-time')
        return HttpResponse(serializers.serialize("json", data))

    elif kategori_inputuser == "pakaian":
        data = ForumUMKM.objects.filter(kategori=kategori_inputuser).order_by('-time')
        return HttpResponse(serializers.serialize("json", data))

def main(request,kategori_inputuser):
    data = ""
   
    if kategori_inputuser == "semua":
        data = ForumUMKM.objects.all()
        content={'data':data, 'list_category':["semua","makanan","pakaian"],'selected_cat':"semua"}
        return render(request, "front.html", content)

    elif kategori_inputuser == "makanan":
        data = ForumUMKM.objects.filter(kategori=kategori_inputuser)
        content={'data':data, 'list_category':["semua","makanan","pakaian"],'selected_cat':"makanan"}
        return render(request, "front.html", content)

    elif kategori_inputuser == "pakaian":
        data = ForumUMKM.objects.filter(kategori=kategori_inputuser)
        content={'data':data, 'list_category':["semua","makanan","pakaian"],'selected_cat':"pakaian"}
        return render(request, "front.html", content)

def add_forum(request):
    if request.method == 'POST':
        user = request.user
        title = request.POST.get('title')
        discussion = request.POST.get('message')
        category = request.POST.get('category')
        #inget ubah user-nya
        forum = ForumUMKM(user=0,title=title,discussion=discussion,kategori=category)
        forum.save()
        return redirect('/forum/semua')
    return HttpResponseNotFound()

def show_reply(request, forum_id):
    forum = ForumUMKM.objects.filter(id=forum_id).first()
    reply = Replies.objects.filter(forum=forum)
    content = {'forum': forum, 'reply':reply}
    return render(request, "discuss.html", content)

def show_json_reply(request,forum_id):
    this_forum = ForumUMKM.objects.filter(id=forum_id).first()
    data = Replies.objects.filter(forum=this_forum)
    return HttpResponse(serializers.serialize("json", data))

def add_reply(request):
    if request.method == "POST":
        print(request.POST)
        user = request.user
        discussion = request.POST.get('message')
        forum = int(request.POST.get('repforum'))
        #inget ubah user-nya jadi user=user
        this_forum = ForumUMKM.objects.filter(id=forum).first()
        reply = Replies(user=1, discussion=discussion,forum=this_forum)
        reply.save()
        return redirect('/forum/discussion/{}'.format(forum))
    return HttpResponseNotFound()

#admin only
def delete_forum(request, forum_id):
    forum = ForumUMKM.objects.get(pk=forum_id)
    forum.delete()
    forum = ForumUMKM.objects.all()
    return HttpResponseRedirect('/forum/semua')