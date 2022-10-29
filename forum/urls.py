from django.urls import path
from forum.views import show_reply,add_forum,main,add_reply,show_json,show_json_reply,delete_forum

app_name = 'forum'

urlpatterns = [
    #path('', all, name='all'),
    path('<str:kategori_inputuser>/', main, name='main'),
    path('discussion/<int:forum_id>/', show_reply, name='show_reply'),
    path('/addforum', add_forum, name='add_forum'),
    path('/addreply', add_reply, name='add_reply'),
    #path('/json', show_json, name='show_json'),
    path('json/<str:kategori_inputuser>/', show_json, name='show_json'),
    path('json_reply/<int:forum_id>/', show_json_reply, name='show_json_reply'),
    path('delete/<int:forum_id>', delete_forum, name='delete_forum'),
]