import json

from django.db import models
from django.forms.models import model_to_dict


# Create your models here.
class Student(models.Model):
    #主键自增
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    sex = models.IntegerField()
    age = models.IntegerField()
    class Meta:
         db_table ='student'
    def to_JSON1(self):
        dictionary = {}
        """
         只保留自己定义的属性
        """
        for field in self._meta.get_all_field_names():
            dictionary[field] = self.__getattribute__(field)
        return json.dumps(dictionary,indent=2)
    def to_JSON2(self):
        s_dict = model_to_dict(self)
        return json.dumps(s_dict,indent=2)
    def getMeta(self):
        return self._meta.get_all_field_names()