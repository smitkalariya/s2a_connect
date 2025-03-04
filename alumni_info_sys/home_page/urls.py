from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register_student',views.register_student,name='register_student'),
    path('student_dashboard',views.student_dashboard,name='student_dashboard'),
    path('register_alumni',views.register_alumni,name='register_alumni'),
    path('alumni_dashboard',views.alumni_dashboard,name='alumni_dashboard'),
    path('delete_account_student',views.delete_account_student,name='delete_account_student'),
    path('delete_account_alumni',views.delete_account_alumni,name='delete_account_alumni'),
    path('logout_student',views.logout_student,name='logout_student'),
    path('logout_alumni',views.logout_alumni,name='logout_alumni'),
    # path('student_page',views.student_page,name='student_page'),
    path('more_details/<str:clgid>',views.more_details,name='more_details'),
    
    path('reset_password/<token>/',views.reset_password,name='reset_password'),
    path('forgot_password_alumni',views.forgot_password_alumni,name='forgot_password_alumni'),
    path('forgot_password_user',views.forgot_password_user,name='forgot_password_user'),
    path('email_link_alumni',views.email_link_alumni,name='email_link_alumni'),
    path('new_password',views.new_password,name='new_password'),
    path('email_link_user',views.email_link_user,name='email_link_user'),

    path('profile',views.profile,name='profile'),
    path('education',views.education,name='education'),
    path('appliedClg',views.appliedClg,name='appliedClg'),
    path('coaching',views.coaching,name='coaching'),
    path('consultancy',views.consultancy,name='consultancy'),
    path('residencial',views.residencial,name='residencial'),
    path('flight',views.flight,name='flight'),

    path('profile_form',views.profile_form,name='profile_form'),
    path('education_form',views.education_form,name='education_form'),
    path('appliedClg_form',views.appliedClg_form,name='appliedClg_form'),
    path('coaching_form',views.coaching_form,name='coaching_form'),
    path('consultancy_form',views.consultancy_form,name='consultancy_form'),
    path('residencial_form',views.residencial_form,name='residencial_form'),
    path('flight_form',views.flight_form,name='flight_form'),

    path('base', views.base,name="base"),

    path('search',views.search,name='search'),
    path('userpage',views.userpage,name='userpage'),
    path('all_details',views.all_details,name='all_details'),
    path('search_alumni',views.search_alumni,name='search_alumni'),

    path('adminlogin',views.adminlogin,name='adminlogin'),
    path('admin_page',views.admin_page,name='admin_page'),
    path('add_admin',views.add_admin,name='add_admin'),
    path('userpageredir',views.userpageredir,name='userpageredir'),

    path('profile_admin',views.profile_admin,name='profile_admin'),
    path('change_password',views.change_password,name='change_password'),
    path('new_admin',views.new_admin,name='new_admin'),
    path('add_alumni',views.add_alumni,name='add_alumni'),
    path('manage_alumni',views.manage_alumni,name='manage_alumni'),
    
    path('update_profile',views.update_profile,name='update_profile'),
    path('update_password',views.update_password,name='update_password'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('admin_add_alumni',views.admin_add_alumni,name='admin_add_alumni'),
    path('admin_manage_alumni',views.admin_manage_alumni,name='admin_manage_alumni'),
    path('delete_alumni/<str:del_id>',views.delete_alumni,name='delete_alumni'),
    # path('adminprofile',views.adminprofile,name='adminprofile'),
    # path('changepassword',views.changepassword,name='changepassword'),
    # path('redir',views.redir,name='redir'),


]