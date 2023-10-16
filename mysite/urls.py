from django.conf import settings
from django.conf.urls import url
from django.urls import path,include
from django.conf.urls.static import static

from mysite.album import views



urlpatterns = [
    # url(r'^$', views.photo_list, name='photo_list'),
    path('', views.success, name = 'success'),
    path('inpaint/', views.inpaint, name = 'inpaint'),
    path('red/', views.redphoto_list, name = 'red'),
    path('blue/', views.bluephoto_list, name = 'blue'),
    path('green/', views.greenphoto_list, name = 'green'),
    path('yellow/', views.yellowphoto_list, name = 'yellow'),
    path('orange/', views.orangephoto_list, name = 'orange'),
    path('grey/', views.greyphoto_list, name = 'grey'),
    path('cyan/', views.cyanphoto_list, name = 'cyan'),
    path('purple/', views.purplephoto_list, name = 'purple'),
    path('none/', views.nonephoto_list, name = 'none'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
 
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

