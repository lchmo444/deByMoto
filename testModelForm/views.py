# -*- coding: utf-8 -*-


from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import FormView

from testModelForm.models import TestData
from testModelForm.forms import AddDataForm

from django.http import HttpResponseNotFound, HttpResponseRedirect

class DataListView(ListView):
    template_name = 'dataList.html'
    model = TestData

    def get_context_data(self, **kwargs):
        context = super(DataListView, self).get_context_data(**kwargs)
        context['dlist'] = self.model.objects.all()
        return context

class AddDataView(FormView):
    success_url = "/testModel"
    template_name = 'addData.html'
    form_class = AddDataForm

    def form_valid(self, form):
        sg = form.save()
        print sg.__dict__

        messages.info( self.request, "successfully added" )
        return super(AddDataView, self).form_valid(form)


def delData(request, delid):
    try:
        model = TestData
        deletingObject = model.objects.get(id=delid)
        deletingObject.delete()

        return HttpResponseRedirect("/testModel/")
    except:
        return HttpResponseNotFound(u'<h1>잘못된 접근입니다.</h1>')