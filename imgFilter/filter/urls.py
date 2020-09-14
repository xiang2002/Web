from django.urls import path,include

from filter import views
app_name = 'filter'
urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.index, name='index')
]