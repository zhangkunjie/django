from _ast import Str

from django.views.generic.detail import DetailView
from genaralview.models import Student
from django.db.models.base import Model
class StudentDetailView(DetailView):
    template_name = "student.html"
    model=Student
    def get_context_data(self, **kwargs):
        context = super(StudentDetailView, self).get_context_data(**kwargs)
        context['content'] = "单个student详细信息"
        return context