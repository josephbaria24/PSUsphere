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
from django.urls import path
from studentorg.views import HomePageView, OrganizationList, OrganizationCreateView, OrganizationUpdateView, OrganizationDeleteView, OrganizationMember, OrganizationAddMember, OrganizationUpdateMember, OrganizationDeleteMember, StudentList , StudentListAdd, StudentListUpdate, StudentListDelete, college, collegeAdd, collegeEdit, collegeDelete
from studentorg import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , views.HomePageView.as_view(), name= 'home'),
    path('organization_list',OrganizationList.as_view(), name='organization-list'),
    path('organization_list/add', OrganizationCreateView.as_view(), name='organization-add'),
    path('organization_list/<pk>', OrganizationUpdateView.as_view(), name='organization-update'),
    path('organization_list/<pk>/delete', OrganizationDeleteView.as_view(), name='organization-delete'),

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


]
