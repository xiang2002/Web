from django.urls import path,include

from filter import views
app_name = 'filter'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index, name='index'),
    path("logout/", views.logout, name="logout"),
    path("del/", views.delete, name="delete"),
    path("move/", views.move, name="move"),
    path("save/", views.save, name="save"),
]