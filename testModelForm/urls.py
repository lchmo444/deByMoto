from django.conf import settings
from django.conf.urls import patterns, url
from django.conf.urls.static import static

from testModelForm.views import DataListView
from testModelForm.views import AddDataView

from testModelForm import views

urlpatterns = patterns('',

    url(r'^$',
        DataListView.as_view(),
        name='index'
    ),
    url(r'^addData/$',
        AddDataView.as_view(),
        name='adddata'
    ),

    url(r'^delData/(?P<delid>\d+)/$',
        views.delData,
        name='deletedata'
    ),

) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
