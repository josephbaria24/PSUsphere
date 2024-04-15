from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm, CollegeForm
from django.urls import reverse_lazy
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

class OrganizationList(ListView):
    model = Organization
    context_object_name = 'organization'
    template_name = 'org_list.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
         qs = super(OrganizationList, self).get_queryset(*args, **kwargs)
         if self.request.GET.get("q") != None:
             query = self.request.GET.get('q')
             qs = qs.filter(Q(name__icontains=query) |
                            Q(description__icontains=query))
         return qs

class OrganizationCreateView(CreateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_add.html'
    success_url = reverse_lazy('organization-list')

class OrganizationUpdateView(UpdateView):
    model = Organization
    form_class = OrganizationForm
    template_name = 'org_edit.html'
    success_url = reverse_lazy('organization-list')


class OrganizationDeleteView(DeleteView):
    model = Organization
    template_name = 'org_del.html'
    success_url = reverse_lazy('organization-list')



class OrganizationMember(ListView):
    model = OrgMember
    context_object_name = 'orgmember'
    template_name = 'org_member.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
         qs = super(OrganizationMember, self).get_queryset(*args, **kwargs)
         if self.request.GET.get("q") != None:
             query = self.request.GET.get('q')
             qs = qs.filter(Q(student__firstname__icontains=query) |
                            Q(organization__name__icontains=query))
         return qs

class OrganizationAddMember(CreateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_add.html'
    success_url = reverse_lazy('orgmember-list')


class OrganizationUpdateMember(UpdateView):
    model = OrgMember
    form_class = OrgMemberForm
    template_name = 'orgmember_edit.html'
    success_url = reverse_lazy('orgmember-list')

class OrganizationDeleteMember(DeleteView):
    model = OrgMember
    template_name = 'orgmember_del.html'
    success_url = reverse_lazy('orgmember-list')



class StudentList(ListView):
    model = Student
    context_object_name = 'students'
    template_name = 'student.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
         qs = super(StudentList, self).get_queryset(*args, **kwargs)
         if self.request.GET.get("q") != None:
             query = self.request.GET.get('q')
             qs = qs.filter(Q(student_id__icontains=query) |
                            Q(firstname__icontains=query) | Q(lastname__icontains=query))
         return qs

class StudentListAdd(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_add.html'
    success_url = reverse_lazy('students-list')


class StudentListUpdate(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student_edit.html'
    success_url = reverse_lazy('students-list')


class StudentListDelete(DeleteView):
    model = Student
    template_name = 'student_del.html'
    success_url = reverse_lazy('students-list')


class college(ListView):
    model = College
    context_object_name = 'college'
    template_name = 'college.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
         qs = super(college, self).get_queryset(*args, **kwargs)
         if self.request.GET.get("q") != None:
             query = self.request.GET.get('q')
             qs = qs.filter(Q(college_name__icontains=query))
         return qs


class collegeAdd(CreateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_add.html'
    success_url = reverse_lazy('college-list')

class collegeEdit(UpdateView):
    model = College
    form_class = CollegeForm
    template_name = 'college_edit.html'
    success_url = reverse_lazy('college-list')


class collegeDelete(DeleteView):
    model = College
    template_name = 'college_del.html'
    success_url = reverse_lazy('college-list')