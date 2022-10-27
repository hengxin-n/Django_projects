# -*- coding: utf-8 -*-
# @time: 2022/9/14 21:18
# Author:Answer
# @File: forms.py
# @Software: PyCharm
from django import forms

from .models import Topic,Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text': ''}
        widgets = {'text':forms.Textarea(attrs={'cols': 80})}