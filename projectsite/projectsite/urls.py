"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from studentorg.views import HomePageView, ChartView, orgMemBarChart, studentDateJoined,doughnutChart,students_per_college,students_per_program,OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView, OrganizationMember, OrganizationAddMember, OrganizationUpdateMember, OrganizationDeleteMember, StudentList , StudentListAdd, StudentListUpdate, StudentListDelete, college, collegeAdd, collegeEdit, collegeDelete, program,programAdd, programEdit, programDelete
from studentorg import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.HomePageView.as_view(), name= 'home'),
    path('organization_list',OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'),
    re_path(r'^login/$', auth_views.LoginView.as_view(
        template_name='login.html'), name='login'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),

    path('org_member', OrganizationMember.as_view(), name='orgmember-list'),
    path('org_member/add', OrganizationAddMember.as_view(), name='orgmember-add'),
    path('org_member/<pk>', OrganizationUpdateMember.as_view(), name='orgmember-update'),
    path('org_member/<pk>/delete', OrganizationDeleteMember.as_view(), name='orgmember-delete'),
    
    path('student', StudentList.as_view(), name='students-list'),
    path('student/add', StudentListAdd.as_view(), name='students-add'),
    path('student/<pk>', StudentListUpdate.as_view(), name='students-update'),
    path('student/<pk>/delete', StudentListDelete.as_view(), name='students-delete'),

    path('college', college.as_view(), name='college-list'),
    path('college/add', collegeAdd.as_view(), name='college-add'),
    path('college/<pk>', collegeEdit.as_view(), name='college-update'),
    path('college/<pk>/delete', collegeDelete.as_view(), name='college-delete'),

    path('program', program.as_view(), name='program-list'),
    path('program/add', programAdd.as_view(), name='program-add'),
    path('program/<pk>', programEdit.as_view(), name='program-update'),
    path('program/<pk>/delete', programDelete.as_view(), name='program-delete'),

    path('dashboard_chart', ChartView.as_view(), name='dashboard-chart'),
    path('barChart/', orgMemBarChart, name='chart'),
    path('doughnutChart/', doughnutChart, name='chart'),
    path('students_per_college/', students_per_college, name='chart'),
    #path('bubbleChart/', students_per_college, name='chart'),
    path('myRadarChart/', studentDateJoined, name='chart'),
    path('polarChart/', students_per_program, name='chart'),
]
