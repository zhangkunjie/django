from _ast import Str

from django.db.models.base import Model
from django.views.generic.list import ListView

from genaralview.models import Student


class StudentListlView(ListView):
    template_name = "studentList.html"
    model=Student
    def get_context_data(self, **kwargs):
        context = super(StudentListlView, self).get_context_data(**kwargs)
        context['content'] = "student列表信息"
        return context