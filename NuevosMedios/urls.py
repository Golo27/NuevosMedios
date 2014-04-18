from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'recetas.views.inicio'),
    url(r'^recetas/$', 'recetas.views.lista_recetas'),
    url(r'^receta/nueva/$','recetas.views.nueva_receta'),
    url(r'^receta/ordenada/$','recetas.views.recetas_ABC'),
    url(r'^receta/fecha/$','recetas.views.recetas_order_fecha'),
    url(r'^ingresar/$','recetas.views.ingresar'),
    url(r'^privado/$','recetas.views.privado'),
    url(r'^usuario/nuevo/$','recetas.views.nuevo_usuario'),
    url(r'^cerrar/$', 'recetas.views.cerrar'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}
	),
)
