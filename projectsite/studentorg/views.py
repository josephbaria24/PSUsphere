from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from studentorg.models import Organization, OrgMember, Student, College, Program
from studentorg.forms import OrganizationForm, OrgMemberForm, StudentForm, CollegeForm, ProgramForm
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from typing import Any
from django.db.models.query import QuerySet
from django.db.models import Q
from django.db import connection
from django.http import JsonResponse
from django.db.models.functions import ExtractMonth
from django.db.models import Count
from django.db.models import Count
from django.http import JsonResponse
from .models import OrgMember
from datetime import datetime


@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"



class ChartView(ListView):
    template_name = 'chart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        pass




def orgMemBarChart(request):
    queryset = OrgMember.objects.values('organization__name').annotate(member_count=Count('id'))

    result = {}

    for item in queryset:
        org_name = item['organization__name']
        total_members = item['member_count']
        result[org_name] = total_members

    return JsonResponse(result)

def doughnutChart(request):
    queryset = Organization.objects.values('college__college_name').annotate(org_count=Count('id'))

    result = {}

    for item in queryset:
        college_name = item['college__college_name']
        total_orgs = item['org_count']
        result[college_name] = total_orgs

    return JsonResponse(result)


def students_per_college(request):
    queryset = Student.objects.values('program__college__college_name').annotate(student_count=Count('id'))

    result = {}

    for item in queryset:
        college_name = item['program__college__college_name']
        num_students = item['student_count']
        result[college_name] = num_students

    return JsonResponse(result)


def students_per_program(request):
    queryset = Student.objects.values('program__prog_name').annotate(student_count=Count('id'))

    result = {}

    for item in queryset:
        program_name = item['program__prog_name']
        num_students = item['student_count']
        result[program_name] = num_students

    return JsonResponse(result)









#def students_per_college(request):
    # Query data
    queryset = Student.objects.values('program__college__college_name').annotate(student_count=Count('id'))

    # Process data
    labels = []
    counts = []
    sizes = []

    for item in queryset:
        college_name = item['program__college__college_name']
        num_students = item['student_count']
        labels.append(college_name)
        counts.append(num_students)
        # Define size of bubbles based on student count
        sizes.append(num_students * 5)  # Adjust scale factor as needed

    # Prepare data for chart
    chart_data = {
        'labels': labels,
        'counts': counts,
        'sizes': sizes,
    }

    return JsonResponse(chart_data)



def studentDateJoined(request):
    with connection.cursor() as cursor:
        cursor.execute("""
    SELECT
    date_joined AS month,
    COUNT(id) AS student_count
FROM
    studentorg_orgmember
GROUP BY
    month

""")
        rows = cursor.fetchall()

    # Process data
    labels = []
    counts = []

    for row in rows:
        # Extract month and count from each row
        month = row[0]
        count = row[1]

        # Append to lists
        labels.append(month)
        counts.append(count)

    # Prepare data for chart
    chart_data = {
        'labels': labels,
        'counts': counts,
    }

    return JsonResponse(chart_data)






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






class program(ListView):
    model = Program
    context_object_name = 'program'
    template_name = 'program.html'
    paginate_by = 5




class programAdd(CreateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_add.html'
    success_url = reverse_lazy('program-list')

class programEdit(UpdateView):
    model = Program
    form_class = ProgramForm
    template_name = 'program_edit.html'
    success_url = reverse_lazy('program-list')


class programDelete(DeleteView):
    model = Program
    template_name = 'program_del.html'
    success_url = reverse_lazy('program-list')