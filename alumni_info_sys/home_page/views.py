from asyncio.windows_events import NULL
from atexit import register
from email import message
import email
from email.policy import default
import imp
from multiprocessing.spawn import import_main_path
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from home_page.models import Reg_student, Reg_alumni, Profile, Education, Coaching, Consultancy, Residencial, Flight, All, Admin, AppliedClg, Resetpass
from . import models
from django.http import HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from .helpers import send_forget_password_mail_alumni
from .helpers import send_forget_password_mail_user
from .helpers import send_admin_reg_mail
from .helpers import send_alumni_reg_mail
import uuid
from django.contrib.auth.hashers import make_password


# Create your views here.

def home(request):
    return render(request, "home_page.html")

def register_student(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        collage_id = request.POST['collage_id']
        email = request.POST['email']
        password = request.POST['password']

        two=collage_id[:2]

        if(two!="AL"):
            if User.objects.filter(username=collage_id).exists():
                messages.info(request,'Collage id already taken')
                return redirect('register_student')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
                return redirect('register_student')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=collage_id, email=email, password=password)
                user.save()
                reg_stu = Reg_student(first_name=first_name, last_name=last_name,collage_id=collage_id, email=email,password=password)
                reg_stu.save()
                return render(request, "loginform_student.html")

        else:
            messages.info(request,'collage id is invalid')
            return render(request,"signupform_student.html")
        
    else:
        return render(request, "signupform_student.html")

def student_dashboard(request):
    if request.method == 'POST':
        username = request.POST.get('collage_id','')
        password = request.POST.get('password','')

        two=username[:2]
        user = auth.authenticate(username=username, password=password)
        
        if(two!="AL"):
            if user is not None:
                auth.login(request, user)
                request.session['collage_id'] = username
                request.session['password'] = password
                pro=Profile.objects.all()
                reg=Reg_alumni.objects.all()
                return render(request, "all_details.html",{'pro':pro, 'reg':reg})
        
            else:
                messages.info(request,'Invalid credencials')
                return render(request, "loginform_student.html")

        else:
            messages.info(request,'Invalid credencials')
            return render(request, "loginform_student.html")
        
    else:
        return render(request, "loginform_student.html")

def register_alumni(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        collage_id = request.POST['collage_id']
        email = request.POST['email']
        password = request.POST['password']
        sem = request.POST.get('sem','')

        two=collage_id[:2]
        
        if(two=="AL"):

            if User.objects.filter(username=collage_id).exists():
                messages.info(request,'Collage id already taken')
                return redirect('register_alumni')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
                return redirect('register_alumni')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=collage_id, email=email, password=password)
                user.save()
                reg_alu = Reg_alumni(first_name=first_name, last_name=last_name,collage_id=collage_id, email=email, password=password, sem=sem)
                reg_alu.save()

                profile = Profile(collage_id_id=collage_id)
                profile.save()
               
                education = Education(collage_id_id=collage_id)
                education.save()

                appliedclg = AppliedClg(collage_id_id=collage_id)
                appliedclg.save()

                coaching = Coaching(collage_id_id=collage_id)
                coaching.save()

                consultancy = Consultancy(collage_id_id=collage_id)
                consultancy.save()

                residencial = Residencial(collage_id_id=collage_id)
                residencial.save()

                flight = Flight(collage_id_id=collage_id)
                flight.save()

                alll = All(collage_id_id=collage_id)
                alll.save()
                # if sem=='on':
                return render(request, "loginform_alumni.html")
                # else:
                    # return render(request, "loginform_student.html")
            
        else:
            messages.info(request,"collage id is incorrect")
            return render(request, "signupform_alumni.html")

            
        
    else:
        return render(request, "signupform_alumni.html")

def base(request):
    if request.method == 'POST':
        username = request.POST.get('collage_id','')
        password = request.POST.get('password','')

        user = auth.authenticate(username=username, password=password)
       
        if user is not None:
            auth.login(request, user)
            request.session['collage_id'] = username

            row_exists = Profile.objects.filter(collage_id_id = username).exists()
            
            if row_exists:
                pass
            else:
                profile = Profile(collage_id_id=username)
                profile.save()
               
                education = Education(collage_id_id=username)
                education.save()

                appliedclg = AppliedClg(collage_id_id=username)
                appliedclg.save()

                coaching = Coaching(collage_id_id=username)
                coaching.save()

                consultancy = Consultancy(collage_id_id=username)
                consultancy.save()

                residencial = Residencial(collage_id_id=username)
                residencial.save()

                flight = Flight(collage_id_id=username)
                flight.save()

                alll = All(collage_id_id=username)
                alll.save()

            pro = Profile.objects.get(collage_id_id = username)
            edu = Education.objects.get(collage_id_id = username)
            appclg = AppliedClg.objects.get(collage_id_id=username)
            coach = Coaching.objects.get(collage_id_id = username)
            consult = Consultancy.objects.get(collage_id_id = username)
            res = Residencial.objects.get(collage_id_id = username)
            fli = Flight.objects.get(collage_id_id = username)

            return render(request, "base.html", {'clg_id':username, 'pro':pro, 'edu':edu,'appclg':appclg, 'coach':coach,'consult':consult, 'res':res, 'fli':fli})
        
        else:
            messages.info(request,'Invalid credencials')
            return render(request, "loginform_alumni.html")
        
    else:
        return render(request, "loginform_alumni.html")

def alumni_dashboard(request):
    if request.method == 'POST':
        username = request.POST.get('collage_id','')
        password = request.POST.get('password','')

        pro = Profile.objects.filter(collage_id_id=username)
        
        user = auth.authenticate(username=username, password=password)
        # user1 = Reg_alumni.objects.filter(collage_id=user)

        two=username[:2]
        
        if(two=="AL"):
                
            if user is not None:
                auth.login(request, user)
                request.session['collage_id'] = username
                # reg_id = Reg_alumni.objects.filter(collage_id = username)
                return render(request, "profile.html", {'pro':pro[0]})
        
            else:
                messages.info(request,'Invalid credencials')
                return render(request, "loginform_alumni.html")
        
        else:
             messages.info(request,'Invalid credencials')
             return render(request, "loginform_alumni.html")
      
    else:
        return render(request, "loginform_alumni.html")
            

def delete_account_student(request):
    collage_id = request.session.get('collage_id')

    del_auth = User.objects.get(username = collage_id)
    del_stu = Reg_student.objects.get(collage_id = collage_id)

    del_auth.delete()
    del_stu.delete()
    del request.session['collage_id']
    return render(request, "home_page.html")

def delete_account_alumni(request):
    collage_id = request.session.get('collage_id')
    del_pro = Profile.objects.get(collage_id_id = collage_id)
    del_edu = Education.objects.get(collage_id_id = collage_id)
    del_appclg = AppliedClg.object.get(collage_id_id = collage_id)
    del_coa = Coaching.objects.get(collage_id_id = collage_id)
    del_con = Consultancy.objects.get(collage_id_id = collage_id)
    del_res = Residencial.objects.get(collage_id_id = collage_id)
    del_fli = Flight.objects.get(collage_id_id = collage_id)

    del_reg = Reg_alumni.objects.get(collage_id = collage_id)
    del_all = All.objects.get(collage_id_id = collage_id)
    del_auth = User.objects.get(username = collage_id)


    del_pro.delete()
    del_edu.delete()
    del_appclg.delete()
    del_coa.delete()
    del_con.delete()
    del_res.delete()
    del_fli.delete()

    del_reg.delete()
    del_all.delete()
    del_auth.delete()

    return render(request, "home_page.html")

def logout_student(request):
    del request.session['collage_id']
    del request.session['password']
    return render(request, "loginform_student.html")

def logout_alumni(request):
    del request.session['collage_id']
    return render(request, "loginform_alumni.html")

# -----------------------------------------------------alumni form start---------------------------------

def profile(request):
    collage_id = request.session.get('collage_id')
    pro = Profile.objects.filter(collage_id_id = collage_id)
    return render(request, "profile.html", {'pro':pro[0]})

def education(request):
    collage_id = request.session.get('collage_id')

    pro = Profile.objects.filter(collage_id_id = collage_id)
    edu = Education.objects.filter(collage_id_id = collage_id)

    alumni_sem = Reg_alumni.objects.filter(collage_id = collage_id).values('sem')
    al_sem = alumni_sem[0]
    al = al_sem['sem']
    if al=="on":
        messages.info(request,'You are in sem 6. So, you cannot fill this form.')
        return render(request, "profile.html", {'pro':pro[0]})
    else:
        return render(request, "education.html",{'edu':edu[0]})

def appliedClg(request):
    collage_id = request.session.get('collage_id')

    pro = Profile.objects.filter(collage_id_id = collage_id)
    appClg = AppliedClg.objects.filter(collage_id_id = collage_id)

    alumni_sem = Reg_alumni.objects.filter(collage_id = collage_id).values('sem')
    al_sem = alumni_sem[0]
    al = al_sem['sem']
    if al=="on":
        messages.info(request,'You are in sem 6. So, you cannot fill this form.')
        return render(request, "profile.html",{'pro':pro[0]})
    else:
        return render(request, "applied_collage.html",{'appClg':appClg[0]})

def coaching(request):
    collage_id = request.session.get('collage_id')

    coach = Coaching.objects.filter(collage_id_id = collage_id)

    return render(request, "coaching.html", {'coach':coach[0]})

def consultancy(request):
    collage_id = request.session.get('collage_id')

    con = Consultancy.objects.filter(collage_id_id = collage_id)

    return render(request, "consultancy.html",{'con':con[0]})

def residencial(request):
    collage_id = request.session.get('collage_id')

    pro = Profile.objects.filter(collage_id_id = collage_id)
    res = Residencial.objects.filter(collage_id_id = collage_id)
    alumni_sem = Reg_alumni.objects.filter(collage_id = collage_id).values('sem')

    al_sem = alumni_sem[0]
    al = al_sem['sem']
    if al=="on":
        messages.info(request,'You are in sem 6. So, you cannot fill this form.')
        return render(request, "profile.html", {'pro':pro[0]})
    else:
        return render(request, "residencial.html", {'res':res[0]})

def flight(request):
    collage_id = request.session.get('collage_id')

    pro = Profile.objects.filter(collage_id_id = collage_id)
    fli = Flight.objects.filter(collage_id_id = collage_id)
    alumni_sem = Reg_alumni.objects.filter(collage_id = collage_id).values('sem')

    al_sem = alumni_sem[0]
    al = al_sem['sem']
    if al=="on":
        messages.info(request,'You are in sem 6. So, you cannot fill this form.')
        return render(request, "profile.html",{'pro':pro[0]})
    else:
        return render(request, "flight.html", {'fli':fli[0]})

def profile_form(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name','')
        email = request.POST.get('email','')
        branch= request.POST.get('branch','')
        passout_year= request.POST.get('passout_year')
        gender= request.POST.get('gender','')
        permanent_address= request.POST.get('permanent_address','')
        home_town= request.POST.get('home_town','')

        collage_id = request.session.get('collage_id')
        
        profile_row_exists = Profile.objects.filter(collage_id_id = collage_id).exists()

        if profile_row_exists:
            Profile.objects.filter(collage_id_id = collage_id).update(full_name=full_name, email=email,branch=branch,passout_year=passout_year,gender=gender,permanent_address=permanent_address,home_town=home_town)
            All.objects.filter(collage_id_id = collage_id).update(full_name=full_name, email=email,branch=branch,passout_year=passout_year,gender=gender,permanent_address=permanent_address,home_town=home_town)
            pro = Profile.objects.filter(collage_id_id = collage_id)
        else:
            profile = Profile(full_name=full_name, email=email,branch=branch,passout_year=passout_year,gender=gender,permanent_address=permanent_address,home_town=home_town,collage_id_id=collage_id)
            profile.save()
            pro = Profile.objects.filter(collage_id_id = collage_id)
        return render(request,"profile.html",{'clg_id':collage_id, 'pro':pro[0]})
       
    else:
        return render(request,"profile.html")

def education_form(request):
    if request.method == 'POST':
        gre = request.POST.get('gre','')
        toefl = request.POST.get('toefl','')
        ielts = request.POST.get('ielts','')
        cpi6 = request.POST.get('cpi6','')
        cpi7 = request.POST.get('cpi7','')
        backlog6 = request.POST.get('backlog6','')
        backlog7 = request.POST.get('backlog7','')
        collage = request.POST.get('collage','')
        collage_country = request.POST.get('collage_country','')
        collage_city = request.POST.get('collage_city','')
        collage_branch = request.POST.get('collage_branch','')

        collage_id = request.session.get('collage_id')

        education_row_exists = Education.objects.filter(collage_id_id = collage_id).exists()

        if education_row_exists:
            Education.objects.filter(collage_id_id = collage_id).update(gre=gre, toefl=toefl, ielts=ielts, cpi6=cpi6, cpi7=cpi7, backlog6=backlog6, backlog7=backlog7, collage=collage, collage_country=collage_country, collage_city=collage_city, collage_branch=collage_branch)
            All.objects.filter(collage_id_id = collage_id).update(gre=gre, toefl=toefl, ielts=ielts, cpi6=cpi6, cpi7=cpi7, backlog6=backlog6, backlog7=backlog7, collage=collage, collage_country=collage_country, collage_city=collage_city, collage_branch=collage_branch)
            edu = Education.objects.filter(collage_id_id = collage_id)
        else:
            education = Education(gre=gre, toefl=toefl, ielts=ielts, cpi6=cpi6, cpi7=cpi7, backlog6=backlog6, backlog7=backlog7, collage=collage, collage_country=collage_country, collage_city=collage_city, collage_branch=collage_branch, collage_id_id=collage_id)
            education.save()
            edu = Education.objects.filter(collage_id_id = collage_id)
        return render(request,"education.html",{'clg_id':collage_id, 'edu':edu[0]})

    else:
        return render(request,"education.html")

def appliedClg_form(request):
    if request.method == 'POST':
        country1 = request.POST.get('country1','')
        c1_clg1 = request.POST.get('c1_clg1','')
        c1_sn1 = request.POST.get('c1_sn1','')
        c1_c1 = request.POST.get('c1_c1','')
        c1_af1 = request.POST.get('c1_af1','')
        c1_cf1 = request.POST.get('c1_cf1','')
        c1_cn1 = request.POST.get('c1_cn1','')
        c1_gre1 = request.POST.get('c1_gre1','')
        c1_toefl1 = request.POST.get('c1_toefl1','')
        c1_ielts1 = request.POST.get('c1_ielts1','')

        c1_clg2 = request.POST.get('c1_clg2','')
        c1_sn2 = request.POST.get('c1_sn2','')
        c1_c2 = request.POST.get('c1_c2','')
        c1_af2 = request.POST.get('c1_af2','')
        c1_cf2 = request.POST.get('c1_cf2','')
        c1_cn2 = request.POST.get('c1_cn2','')
        c1_gre2 = request.POST.get('c1_gre2','')
        c1_toefl2 = request.POST.get('c1_toefl2','')
        c1_ielts2 = request.POST.get('c1_ielts2','')

        c1_clg3 = request.POST.get('c1_clg3','')
        c1_sn3 = request.POST.get('c1_sn3','')
        c1_c3 = request.POST.get('c1_c3','')
        c1_af3 = request.POST.get('c1_af3','')
        c1_cf3 = request.POST.get('c1_cf3','')
        c1_cn3 = request.POST.get('c1_cn3','')
        c1_gre3 = request.POST.get('c1_gre3','')
        c1_toefl3 = request.POST.get('c1_toefl3','')
        c1_ielts3 = request.POST.get('c1_ielts3','')

        country2 = request.POST.get('country2','')
        c2_clg1 = request.POST.get('c2_clg1','')
        c2_sn1 = request.POST.get('c2_sn1','')
        c2_c1 = request.POST.get('c2_c1','')
        c2_af1 = request.POST.get('c2_af1','')
        c2_cf1 = request.POST.get('c2_cf1','')
        c2_cn1 = request.POST.get('c2_cn1','')
        c2_gre1 = request.POST.get('c2_gre1','')
        c2_toefl1 = request.POST.get('c2_toefl1','')
        c2_ielts1 = request.POST.get('c2_ielts1','')

        c2_clg2 = request.POST.get('c2_clg2','')
        c2_sn2 = request.POST.get('c2_sn2','')
        c2_c2 = request.POST.get('c2_c2','')
        c2_af2 = request.POST.get('c2_af2','')
        c2_cf2 = request.POST.get('c2_cf2','')
        c2_cn2 = request.POST.get('c2_cn2','')
        c2_gre2 = request.POST.get('c2_gre2','')
        c2_toefl2 = request.POST.get('c2_toefl2','')
        c2_ielts2 = request.POST.get('c2_ielts2','')

        c2_clg3 = request.POST.get('c2_clg3','')
        c2_sn3 = request.POST.get('c2_sn3','')
        c2_c3 = request.POST.get('c2_c3','')
        c2_af3 = request.POST.get('c2_af3','')
        c2_cf3 = request.POST.get('c2_cf3','')
        c2_cn3 = request.POST.get('c2_cn3','')
        c2_gre3 = request.POST.get('c2_gre3','')
        c2_toefl3 = request.POST.get('c2_toefl3','')
        c2_ielts3 = request.POST.get('c2_ielts3','')
        

        collage_id = request.session.get('collage_id')

        appliedClg_row_exists = AppliedClg.objects.filter(collage_id_id = collage_id).exists()

        if appliedClg_row_exists:
            AppliedClg.objects.filter(collage_id_id = collage_id).update(country1=country1, c1_clg1=c1_clg1, c1_state1=c1_sn1, c1_city1=c1_c1, c1_appfees1=c1_af1, c1_coursefees1=c1_cf1, c1_course1=c1_cn1, c1_gre1=c1_gre1, c1_toefl1=c1_toefl1, c1_ielts1=c1_ielts1, c1_clg2=c1_clg2, c1_state2=c1_sn2, c1_city2=c1_c2, c1_appfees2=c1_af2, c1_coursefees2=c1_cf2, c1_course2=c1_cn2, c1_gre2=c1_gre2, c1_toefl2=c1_toefl2, c1_ielts2=c1_ielts2, c1_clg3=c1_clg3, c1_state3=c1_sn3, c1_city3=c1_c3, c1_appfees3=c1_af3, c1_coursefees3=c1_cf3, c1_course3=c1_cn3, c1_gre3=c1_gre3, c1_toefl3=c1_toefl3, c1_ielts3=c1_ielts3,country2=country2, c2_clg1=c2_clg1, c2_state1=c2_sn1, c2_city1=c2_c1, c2_appfees1=c2_af1, c2_coursefees1=c2_cf1, c2_course1=c2_cn1, c2_gre1=c2_gre1, c2_toefl1=c2_toefl1, c2_ielts1=c2_ielts1, c2_clg2=c2_clg2, c2_state2=c2_sn2, c2_city2=c2_c2, c2_appfees2=c2_af2, c2_coursefees2=c2_cf2, c2_course2=c2_cn2, c2_gre2=c2_gre2, c2_toefl2=c2_toefl2, c2_ielts2=c2_ielts2, c2_clg3=c2_clg3, c2_state3=c2_sn3, c2_city3=c2_c3, c2_appfees3=c2_af3, c2_coursefees3=c2_cf3, c2_course3=c2_cn3, c2_gre3=c2_gre3, c2_toefl3=c2_toefl3, c2_ielts3=c2_ielts3)
            All.objects.filter(collage_id_id = collage_id).update(country1=country1, c1_clg1=c1_clg1, c1_state1=c1_sn1, c1_city1=c1_c1, c1_appfees1=c1_af1, c1_coursefees1=c1_cf1, c1_course1=c1_cn1, c1_gre1=c1_gre1, c1_toefl1=c1_toefl1, c1_ielts1=c1_ielts1, c1_clg2=c1_clg2, c1_state2=c1_sn2, c1_city2=c1_c2, c1_appfees2=c1_af2, c1_coursefees2=c1_cf2, c1_course2=c1_cn2, c1_gre2=c1_gre2, c1_toefl2=c1_toefl2, c1_ielts2=c1_ielts2, c1_clg3=c1_clg3, c1_state3=c1_sn3, c1_city3=c1_c3, c1_appfees3=c1_af3, c1_coursefees3=c1_cf3, c1_course3=c1_cn3, c1_gre3=c1_gre3, c1_toefl3=c1_toefl3, c1_ielts3=c1_ielts3,country2=country2, c2_clg1=c2_clg1, c2_state1=c2_sn1, c2_city1=c2_c1, c2_appfees1=c2_af1, c2_coursefees1=c2_cf1, c2_course1=c2_cn1, c2_gre1=c2_gre1, c2_toefl1=c2_toefl1, c2_ielts1=c2_ielts1, c2_clg2=c2_clg2, c2_state2=c2_sn2, c2_city2=c2_c2, c2_appfees2=c2_af2, c2_coursefees2=c2_cf2, c2_course2=c2_cn2, c2_gre2=c2_gre2, c2_toefl2=c2_toefl2, c2_ielts2=c2_ielts2, c2_clg3=c2_clg3, c2_state3=c2_sn3, c2_city3=c2_c3, c2_appfees3=c2_af3, c2_coursefees3=c2_cf3, c2_course3=c2_cn3, c2_gre3=c2_gre3, c2_toefl3=c2_toefl3, c2_ielts3=c2_ielts3)
            appClg = AppliedClg.objects.filter(collage_id_id = collage_id)
        else:
            appliedClg = AppliedClg(country1=country1, c1_clg1=c1_clg1, c1_state1=c1_sn1, c1_city1=c1_c1, c1_appfees1=c1_af1, c1_coursefees1=c1_cf1, c1_course1=c1_cn1, c1_gre1=c1_gre1, c1_toefl1=c1_toefl1, c1_ielts1=c1_ielts1, c1_clg2=c1_clg2, c1_state2=c1_sn2, c1_city2=c1_c2, c1_appfees2=c1_af2, c1_coursefees2=c1_cf2, c1_course2=c1_cn2, c1_gre2=c1_gre2, c1_toefl2=c1_toefl2, c1_ielts2=c1_ielts2, c1_clg3=c1_clg3, c1_state3=c1_sn3, c1_city3=c1_c3, c1_appfees3=c1_af3, c1_coursefees3=c1_cf3, c1_course3=c1_cn3, c1_gre3=c1_gre3, c1_toefl3=c1_toefl3, c1_ielts3=c1_ielts3,country2=country2, c2_clg1=c2_clg1, c2_state1=c2_sn1, c2_city1=c2_c1, c2_appfees1=c2_af1, c2_coursefees1=c2_cf1, c2_course1=c2_cn1, c2_gre1=c2_gre1, c2_toefl1=c2_toefl1, c2_ielts1=c2_ielts1, c2_clg2=c2_clg2, c2_state2=c2_sn2, c2_city2=c2_c2, c2_appfees2=c2_af2, c2_coursefees2=c2_cf2, c2_course2=c2_cn2, c2_gre2=c2_gre2, c2_toefl2=c2_toefl2, c2_ielts2=c2_ielts2, c2_clg3=c2_clg3, c2_state3=c2_sn3, c2_city3=c2_c3, c2_appfees3=c2_af3, c2_coursefees3=c2_cf3, c2_course3=c2_cn3, c2_gre3=c2_gre3, c2_toefl3=c2_toefl3, c2_ielts3=c2_ielts3, collage_id_id=collage_id)
            appliedClg.save()
            appClg = AppliedClg.objects.filter(collage_id_id = collage_id)
        return render(request,"applied_collage.html",{'clg_id':collage_id, 'appClg':appClg[0]})

    else:
        return render(request,"applied_collage.html")

def coaching_form(request):
    if request.method == 'POST':
        gre_course_name = "GRE"
        gre_center_name = request.POST.get('gre_center_name','')
        gre_center_city = request.POST.get('gre_center_city','')
        gre_course_fees = request.POST.get('gre_course_fees','')
        gre_feedback = request.POST.get('gre_feedback','')

        toefl_course_name = "TOEFL"
        toefl_center_name = request.POST.get('toefl_center_name','')
        toefl_center_city = request.POST.get('toefl_center_city','')
        toefl_course_fees = request.POST.get('toefl_course_fees','')
        toefl_feedback = request.POST.get('toefl_feedback','')

        ielts_course_name = "IELTS"
        ielts_center_name = request.POST.get('ielts_center_name','')
        ielts_center_city = request.POST.get('ielts_center_city','')
        ielts_course_fees = request.POST.get('ielts_course_fees','')
        ielts_feedback = request.POST.get('ielts_feedback','')

        other_course_name = request.POST.get('other_course_name','')
        other_center_name = request.POST.get('other_center_name','')
        other_center_city = request.POST.get('other_center_city','')
        other_course_fees = request.POST.get('other_course_fees','')
        other_feedback = request.POST.get('other_feedback','')

        collage_id = request.session.get('collage_id')

        coaching_row_exists = Coaching.objects.filter(collage_id_id = collage_id).exists()

        if coaching_row_exists:
            Coaching.objects.filter(collage_id_id = collage_id).update(course_name_gre=gre_course_name, center_name_gre=gre_center_name, center_city_gre=gre_center_city, coaching_fees_gre=gre_course_fees, feedback_gre=gre_feedback, course_name_toefl=toefl_course_name, center_name_toefl=toefl_center_name, center_city_toefl=toefl_center_city, coaching_fees_toefl=toefl_course_fees, feedback_toefl=toefl_feedback, course_name_ielts=ielts_course_name, center_name_ielts=ielts_center_name, center_city_ielts=ielts_center_city, coaching_fees_ielts=ielts_course_fees, feedback_ielts=ielts_feedback, course_name_other=other_course_name, center_name_other=other_center_name, center_city_other=other_center_city, coaching_fees_other=other_course_fees, feedback_other=other_feedback)
            All.objects.filter(collage_id_id = collage_id).update(course_name_gre=gre_course_name, center_name_gre=gre_center_name, center_city_gre=gre_center_city, coaching_fees_gre=gre_course_fees, feedback_gre=gre_feedback, course_name_toefl=toefl_course_name, center_name_toefl=toefl_center_name, center_city_toefl=toefl_center_city, coaching_fees_toefl=toefl_course_fees, feedback_toefl=toefl_feedback, course_name_ielts=ielts_course_name, center_name_ielts=ielts_center_name, center_city_ielts=ielts_center_city, coaching_fees_ielts=ielts_course_fees, feedback_ielts=ielts_feedback, course_name_other=other_course_name, center_name_other=other_center_name, center_city_other=other_center_city, coaching_fees_other=other_course_fees, feedback_other=other_feedback)
            coach = Coaching.objects.filter(collage_id_id = collage_id)
        else:
            coaching = Coaching(course_name_gre=gre_course_name, center_name_gre=gre_center_name, center_city_gre=gre_center_city, coaching_fees_gre=gre_course_fees, feedback_gre=gre_feedback, course_name_toefl=toefl_course_name, center_name_toefl=toefl_center_name, center_city_toefl=toefl_center_city, coaching_fees_toefl=toefl_course_fees, feedback_toefl=toefl_feedback, course_name_ielts=ielts_course_name, center_name_ielts=ielts_center_name, center_city_ielts=ielts_center_city, coaching_fees_ielts=ielts_course_fees, feedback_ielts=ielts_feedback, course_name_other=other_course_name, center_name_other=other_center_name, center_city_other=other_center_city, coaching_fees_other=other_course_fees, feedback_other=other_feedback, collage_id_id=collage_id)
            coaching.save()
            coach = Coaching.objects.filter(collage_id_id = collage_id)
        return render(request,"coaching.html",{'clg_id':collage_id, 'coach':coach[0]})

    else:
        return render(request,"coaching.html")

def consultancy_form(request):
    if request.method == 'POST':
        service_name = request.POST.get('service_name','')
        service_city = request.POST.get('service_city','')
        service_center_addr = request.POST.get('service_center_addr','')
        service_number = request.POST.get('service_number','')
        service_fees = request.POST.get('service_fees','')
        consulting_country = request.POST.get('consulting_country','')

        collage_id = request.session.get('collage_id')

        consultancy_row_exists = Consultancy.objects.filter(collage_id_id = collage_id).exists()

        if consultancy_row_exists:
            Consultancy.objects.filter(collage_id_id = collage_id).update(service_name=service_name, service_city=service_city, service_address=service_center_addr, service_number=service_number, service_fees=service_fees, consulting_countries=consulting_country)
            All.objects.filter(collage_id_id = collage_id).update(service_name=service_name, service_city=service_city, service_address=service_center_addr, service_number=service_number, service_fees=service_fees, consulting_countries=consulting_country)
            con = Consultancy.objects.filter(collage_id_id = collage_id)
        else:
            consultancy = Consultancy(service_name=service_name, service_city=service_city, service_address=service_center_addr, service_number=service_number, service_fees=service_fees, consulting_countries=consulting_country, collage_id_id=collage_id)
            consultancy.save()
            con = Consultancy.objects.filter(collage_id_id = collage_id)
        return render(request,"consultancy.html",{'clg_id':collage_id,'con':con[0]})

    else:
        return render(request,"consultancy.html")

def residencial_form(request):
    if request.method == 'POST':
        res_country = request.POST.get('res_country','')
        res_state = request.POST.get('res_state','')
        res_city = request.POST.get('res_city','')
        res_address = request.POST.get('res_address','')
        res_rent = request.POST.get('res_rent','')
        res_utility_exp = request.POST.get('res_utility_exp','')
        res_monthly_exp = request.POST.get('res_monthly_exp','')
        useful_things = request.POST.get('useful_things','')

        collage_id = request.session.get('collage_id')

        res_row_exists = Residencial.objects.filter(collage_id_id = collage_id).exists()

        if res_row_exists:
            Residencial.objects.filter(collage_id_id = collage_id).update(res_country=res_country, res_state=res_state, res_city=res_city, res_address=res_address, res_rent=res_rent, res_utility_exp=res_utility_exp, res_monthly_exp=res_monthly_exp, useful_things=useful_things)
            All.objects.filter(collage_id_id = collage_id).update(res_country=res_country, res_state=res_state, res_city=res_city, res_address=res_address, res_rent=res_rent, res_utility_exp=res_utility_exp, res_monthly_exp=res_monthly_exp, useful_things=useful_things)
            res = Residencial.objects.filter(collage_id_id = collage_id)
        else:
            residencial = Residencial(res_country=res_country, res_state=res_state, res_city=res_city, res_address=res_address, res_rent=res_rent, res_utility_exp=res_utility_exp, res_monthly_exp=res_monthly_exp, useful_things=useful_things, collage_id_id=collage_id)
            residencial.save()
            res = Residencial.objects.filter(collage_id_id = collage_id)
        return render(request,"residencial.html",{'clg_id':collage_id, 'res':res[0]})

    else:
        return render(request,"residencial.html")

def flight_form(request):
    if request.method == 'POST':
        flight_name = request.POST.get('flight_name','')
        site_name = request.POST.get('site_name','')
        airport_exp = request.POST.get('airport_exp','')
        # mode = request.POST.get('mode','')
        fron_where = request.POST.get('fron_where','')
        to_where = request.POST.get('to_where','')
        leave_over_place = request.POST.get('leave_over_place','')
        leave_over_time = request.POST.get('leave_over_time','')

        collage_id= request.POST.get('collage_id','')

        collage_id = request.session.get('collage_id')

        flight_row_exists = Flight.objects.filter(collage_id_id = collage_id).exists()

        if flight_row_exists:
            Flight.objects.filter(collage_id_id = collage_id).update(flight_name=flight_name, site_name=site_name, airport_exp=airport_exp, from_where=fron_where, to_where=to_where, leave_over_place=leave_over_place, leave_over_time=leave_over_time)
            All.objects.filter(collage_id_id = collage_id).update(flight_name=flight_name, site_name=site_name, airport_exp=airport_exp, from_where=fron_where, to_where=to_where, leave_over_place=leave_over_place, leave_over_time=leave_over_time)
            fli = Flight.objects.filter(collage_id_id = collage_id)
        else:
            flight = Flight(flight_name=flight_name, site_name=site_name, airport_exp=airport_exp, from_where=fron_where, to_where=to_where, leave_over_place=leave_over_place, leave_over_time=leave_over_time,collage_id_id=collage_id)
            flight.save()
            fli = Flight.objects.filter(collage_id_id = collage_id)
        return render(request,"flight.html",{'clg_id':collage_id, 'fli':fli[0]})
       
    else:
        return render(request,"flight.html")

#------------------------------------------------------alumni form end----------------------------------------------------

def all_details(request):
    pro=Profile.objects.all()
    reg=Reg_alumni.objects.all()
    return render(request,"all_details.html",{'pro':pro, 'reg':reg})

def search_alumni(request):
    return render(request,"search_alumni.html")

def search(request):
    if request.method == 'POST':
        search_country = request.POST.get('search_country','')
        search_branch = request.POST.get('search_branch','')
        passout_year = request.POST.get('passout_year','')
        collage = request.POST.get('collage','')

        if ((search_country == '') & (search_branch == '') & (passout_year == '') & (collage == '')):
            return render(request,"search_alumni.html")
        
        elif ((search_country == '') & (search_branch == '') & (passout_year == '')):
            search_all = All.objects.filter(collage = collage)
            return render(request,"search_alumni.html",{'all' : search_all})

        elif ((search_country == '') & (search_branch == '') & (collage == '')):
            search_all = All.objects.filter(passout_year = passout_year)
            return render(request,"search_alumni.html",{'all' : search_all})

        elif ((search_country == '') & (search_branch == '')):
            search_all = (All.objects.filter(collage = collage) & All.objects.filter(passout_year = passout_year))
            return render(request,"search_alumni.html",{'all' : search_all})

        elif ((search_country == '') & (passout_year == '') & (collage == '')):
            search_all = All.objects.filter(branch = search_branch)
            return render(request,"search_alumni.html",{'all' : search_all})

        elif ((search_country == '') & (passout_year == '')):
            search_all = (All.objects.filter(branch = search_branch) & All.objects.filter(collage = collage))
            return render(request,"search_alumni.html",{'all' : search_all})

        elif ((search_country == '') & (collage == '')):
            search_all = (All.objects.filter(branch = search_branch) & All.objects.filter(passout_year = passout_year))
            return render(request,"search_alumni.html",{'all' : search_all})

        elif (search_country == ''):
            search_all = (All.objects.filter(branch = search_branch) & All.objects.filter(passout_year = passout_year) & All.objects.filter(collage = collage))
            return render(request,"search_alumni.html",{'all' : search_all})
    
        elif ((search_branch == '') & (passout_year == '') & (collage == '')):
            search_all = All.objects.filter(collage_country = search_country)
            return render(request,"search_alumni.html",{'all' : search_all})
        
        elif ((search_branch == '') & (passout_year == '')):
            search_all = All.objects.filter(collage = collage)
            return render(request,"search_alumni.html",{'all' : search_all})

        elif ((search_branch == '') & (collage == '')):
            search_all = (All.objects.filter(collage_country = search_country) & All.objects.filter(passout_year = passout_year))
            return render(request,"search_alumni.html",{'all' : search_all})

        elif (search_branch == ''):
            search_all = (All.objects.filter(collage_country = search_country) & All.objects.filter(passout_year = passout_year) & All.objects.filter(collage = collage))
            return render(request,"search_alumni.html",{'all' : search_all})

        elif ((passout_year == '') & (collage == '')):
            search_all = (All.objects.filter(collage_country = search_country) & All.objects.filter(branch = search_branch))
            return render(request,"search_alumni.html",{'all' : search_all})

        elif (passout_year == ''):
            search_all = (All.objects.filter(collage_country = search_country) & All.objects.filter(branch = search_branch) & All.objects.filter(collage = collage))
            return render(request,"search_alumni.html",{'all' : search_all})

        elif (collage == ''):
            search_all = (All.objects.filter(collage_country = search_country) & All.objects.filter(branch = search_branch) & All.objects.filter(passout_year = passout_year))
            return render(request,"search_alumni.html",{'all' : search_all})

        else:
            search_all = (All.objects.filter(collage_country = search_country) & All.objects.filter(branch = search_branch) & All.objects.filter(passout_year = passout_year) & All.objects.filter(collage = collage))
            return render(request,"search_alumni.html",{'all' : search_all})



def more_details(request, clgid): 
    # clg_id = request.GET
    # details_id = clg_id.get("id", "0")
    details=All.objects.filter(collage_id=clgid)
    reg=Reg_alumni.objects.filter(collage_id=clgid)

    pro=Profile.objects.filter(collage_id_id=clgid)
    edu=Education.objects.filter(collage_id_id=clgid)
    app=AppliedClg.objects.filter(collage_id_id=clgid)
    coa=Coaching.objects.filter(collage_id_id=clgid)
    con=Consultancy.objects.filter(collage_id_id=clgid)
    res=Residencial.objects.filter(collage_id_id=clgid)
    fli=Flight.objects.filter(collage_id_id=clgid)

    return render(request,"more_details.html",{'alld':details[0], 'reg':reg[0], 'pro':pro[0], 'edu':edu[0], 'app':app[0], 'coa':coa[0], 'con':con[0], 'res':res[0], 'fli':fli[0]})
    
# ------------------------------------admin------------------------------------------
def adminlogin(request):
    return render(request, "loginform_admin.html")

def admin_page(request):
    if request.method == 'POST':
        admin_email = request.POST.get('admin_email','')
        admin_password = request.POST.get('admin_password','')

        user = auth.authenticate(username=admin_email, password=admin_password)

        if user is not None:
            auth.login(request, user)
            adminn = Admin.objects.get(admin_email = admin_email)
            request.session['email'] = admin_email
            return render(request, "profile_admin.html",{'admin':adminn})
        
        else:
            messages.info(request,'Invalid credencials')
            return render(request, "loginform_admin.html")
        
    else:
        return render(request,"loginform_admin.html")
    # return render(request,"profile_admin.html")


def profile_admin(request):
    curr_admin_email=request.session.get('email')
    adminn=Admin.objects.filter(admin_email=curr_admin_email)

    return render(request,"profile_admin.html", {'admin':adminn})

def change_password(request):
    return render(request,"change_pass_ad.html")

def new_admin(request):
    return render(request,"new_admin.html")
    
def add_alumni(request):
    return render(request,"add_alumni.html")

def manage_alumni(request):
    pro=Profile.objects.all()
    reg=Reg_alumni.objects.all()

    return render(request,"manage_alumni.html",{'pro':pro, 'reg':reg})    

def update_profile(request):
    if request.method == 'POST':
        adminFirstName = request.POST.get('adminFirstName','')
        adminLastName = request.POST.get('adminLastName','')
        adminEmail = request.POST.get('adminEmail','')
        adminNo = request.POST.get('adminNo','')
        
        curr_admin_email=request.session.get('email')

        Admin.objects.filter(admin_email = curr_admin_email).update(admin_first_name=adminFirstName, admin_last_name=adminLastName, admin_email=adminEmail, admin_number=adminNo)
        User.objects.filter(username=curr_admin_email).update(username=adminEmail, first_name=adminFirstName, last_name=adminLastName, email=adminEmail)
        request.session['email'] = adminEmail
        adminn=Admin.objects.filter(admin_email=curr_admin_email)
        messages.info(request,'Profile Updated')
        return render(request, "profile_admin.html",{'admin':adminn})
    else:
        return render(request, "profile_admin.html",{'admin':adminn})

def add_admin(request):
    if request.method == 'POST':
        admin_first_name = request.POST.get('admin_first_name','')
        admin_last_name = request.POST.get('admin_last_name','')
        admin_email = request.POST.get('admin_email','')
        admin_no = request.POST.get('admin_no','')
        add_admin_pass = request.POST.get('add_admin_pass','')
        add_admin_conPass = request.POST.get('add_admin_conPass','')

        curr_admin_email = request.session.get('email')

        if User.objects.filter(email=admin_email).exists():
            messages.info(request,'Email id already taken')
            return render(request, "new_admin.html")

        elif(add_admin_pass != add_admin_conPass):
            messages.info(request,'New passwords does not match')
            return render(request, "new_admin.html")

        else:
            user = User.objects.create_user(first_name=admin_first_name, last_name=admin_last_name, email=admin_email, password=add_admin_pass, username=admin_email)
            user.save()
            add_ad = Admin(admin_first_name=admin_first_name, admin_last_name=admin_last_name, admin_email=admin_email,admin_number=admin_no,admin_password=add_admin_pass)
            add_ad.save()
            send_admin_reg_mail(admin_email,add_admin_pass)
            messages.info(request,'New Admin Added successfully')
            return render(request, "new_admin.html")
    else:
        return render(request, "new_admin.html")

def update_password(request):
    if request.method == 'POST':
        oldpass = request.POST['adminCurrPass']
        newpass = request.POST['adminNewPass']
        cnewpass = request.POST['adminConPass']

        admin_email = request.session.get('email')

        u = User.objects.get(username=admin_email)
        if not check_password(oldpass, u.password):
            messages.info(request,'current password is incorrect')
            return render(request, 'change_pass_ad.html')

        elif(newpass != cnewpass):
            messages.info(request,'New passwords does not match')
            # return render(request, 'admin_page.html')
            return render(request, "change_pass_ad.html")

        else:
            # user = User.objects.get(username=request.session['email'])
            # user.set_password(newpass)
            # user.save()
            user_pass = make_password(newpass)
            User.objects.filter(username = admin_email).update(password=user_pass)
            # adminchangepass = Admin.objects.get(admin_email=request.session['email'])
            # adminchangepass.admin_password = newpass
            Admin.objects.filter(admin_email = admin_email).update(admin_password=newpass)
            messages.info(request,'Password changed successfully')
            return render(request, "change_pass_ad.html")

    else:
        return render(request, "change_pass_ad.html")

def admin_logout(request):
    del request.session['email']
    return render(request, 'home_page.html')

def admin_add_alumni(request):
    if request.method == 'POST':
        first_name = request.POST['addFirst_name']
        last_name = request.POST['addLast_name']
        collage_id = request.POST['addCollage_id']
        email = request.POST['addEmail']
        password = request.POST['addPassword']
        sem = request.POST.get('addSem','')

        two=collage_id[:2]
        
        if(two=="AL"):

            if User.objects.filter(username=collage_id).exists():
                messages.info(request,'Collage id already taken')
                return render(request, 'add_alumni.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already taken')
                return render(request, 'add_alumni.html')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=collage_id, email=email, password=password)
                user.save()
                reg_alu = Reg_alumni(first_name=first_name, last_name=last_name,collage_id=collage_id, email=email, password=password, sem=sem)
                reg_alu.save()

                profile = Profile(collage_id_id=collage_id)
                profile.save()
                
                education = Education(collage_id_id=collage_id)
                education.save()

                appliedclg = AppliedClg(collage_id_id=collage_id)
                appliedclg.save()

                coaching = Coaching(collage_id_id=collage_id)
                coaching.save()

                consultancy = Consultancy(collage_id_id=collage_id)
                consultancy.save()

                residencial = Residencial(collage_id_id=collage_id)
                residencial.save()

                flight = Flight(collage_id_id=collage_id)
                flight.save()

                all = All(collage_id_id=collage_id)
                all.save()
                send_alumni_reg_mail(email,password)
                messages.info(request,'New Alumni Added successfully')
                return render(request, "add_alumni.html")
                # else:
                    # return render(request, "loginform_student.html")

        else:
            messages.info(request,"collage id is incorrect")
            return render(request, "add_alumni.html")
        
    else:
        # return HttpResponseRedirect('/adminprofile',{'pro':pro, 'reg':reg})
        return render(request, "add_alumni.html")

def admin_manage_alumni(request):
    pro=Profile.objects.all()
    reg=Reg_alumni.objects.all()
    return render(request, 'admin_page.html',{'pro':pro, 'reg':reg})

def delete_alumni(request,del_id):
    # if request.method == 'POST':
        pro=Profile.objects.all()
        reg=Reg_alumni.objects.all()
        print("id")
        # clg_id = request.GET
        # log.debug(clg_id)
        # del_id = clg_id.get("id", "0")

        # admin_email = request.session.get('email')
        pro=Profile.objects.all()
        reg=Reg_alumni.objects.all()
        # adminn=Admin.objects.filter(admin_email=admin_email)

        del_pro = Profile.objects.get(collage_id_id = del_id)
        del_edu = Education.objects.get(collage_id_id = del_id)
        del_appclg = AppliedClg.objects.get(collage_id_id = del_id)
        del_coa = Coaching.objects.get(collage_id_id = del_id)
        del_con = Consultancy.objects.get(collage_id_id = del_id)
        del_res = Residencial.objects.get(collage_id_id = del_id)
        del_fli = Flight.objects.get(collage_id_id = del_id)

        del_reg = Reg_alumni.objects.get(collage_id = del_id)
        del_all = All.objects.get(collage_id_id = del_id)
        del_auth = User.objects.get(username = del_id)


        del_pro.delete()
        del_edu.delete()
        del_appclg.delete()
        del_coa.delete()
        del_con.delete()
        del_res.delete()
        del_fli.delete()

        del_reg.delete()
        del_all.delete()
        del_auth.delete()

        messages.info(request,'Profile deleted successfully')
        return redirect('http://127.0.0.1:8000/manage_alumni',{'pro':pro, 'reg':reg})

    # else:
    #     return render(request, 'admin_page.html')

#-----------------------expand div-------------------------

def userpage(request):
    if request.method == 'POST':
        pro=Profile.objects.all()
        return render(request, 'user_page.html', {'pro':pro})
    else:
        return render(request,"user_page2.html")

def userpageredir(request):
    cur_user_clgid = request.session['collage_id']
    user = Reg_student.objects.get(collage_id = cur_user_clgid)

    pro=Profile.objects.all()

    context = {
        'user': user
    }
    # return redirect("http://127.0.0.1:8000/student_page", context, {'pro':pro})
    return render(request, 'user_page.html', context, {'pro':pro})

 #--------------------------------------------------forgot password-------------------------------
def reset_password(request, token):
    context = {}

    profile_obj = Resetpass.objects.filter(forget_password_token=token)
    return render(request, 'reset_password.html')

def forgot_password_alumni(request):
    return render(request, 'forgot_password_alumni.html')

def forgot_password_user(request):
    return render(request, 'forgot_password_user.html')

def email_link_alumni(request):
    if request.method == 'POST':
    
        alumni_email = request.POST.get('alumni_email') 

        if not Reg_alumni.objects.filter(email = alumni_email).first():
           messages.info(request,'No user found with this email Id')
           return render(request,'forgot_password_alumni.html') 
        
        request.session['alumni_email'] = alumni_email
        request.session['f_email'] = alumni_email

        user_obj = Reg_alumni.objects.get(email=alumni_email)
        token = str(uuid.uuid4())
        print(alumni_email)
        print(token)
        send_forget_password_mail_alumni(alumni_email, token)
        messages.info(request,'An email is sent.')
        return render(request,'forgot_password_alumni.html') 
    
    else:
        return render(request,'forgot_password_alumni.html')

def email_link_user(request):
    if request.method == 'POST':
        user_email = request.POST.get('user_email') 
        if not Reg_student.objects.filter(email = user_email).first():
           messages.info(request,'No user found with this email Id')
           return render(request,'forgot_password_user.html') 
        
        request.session['user_email'] = user_email
        request.session['f_email'] = user_email
        user_obj = Reg_student.objects.get(email=user_email)
        token = str(uuid.uuid4())
        send_forget_password_mail_user(user_email, token)
        messages.info(request,'An email is sent.')
        return render(request,'forgot_password_user.html') 
    
    else:
        return render(request,'forgot_password_user.html')

def new_password(request):
    if request.method == 'POST':
        reset_pass = request.POST['reset_pass']
        reset_con_pass = request.POST['reset_con_pass']

        f_email = request.session.get('f_email')
        # u = User.objects.get(username=alumni_email)

        if(reset_pass != reset_con_pass):
            messages.info(request,'New passwords does not match')
            return render(request, 'reset_password.html')
            # return redirect("http://127.0.0.1:8000/alumni_dashboard")

        else:
            # User.password = make_password(reset_pass)
            user_pass = make_password(reset_pass)
            print(user_pass)
            # User.save()
            User.objects.filter(email = f_email).update(password=user_pass)
            if Reg_alumni.objects.filter(email = f_email).exists():
                print("if email")
                Reg_alumni.objects.filter(email = f_email).update(password=reset_pass)
                messages.info(request,'Password changed successfully')
                return render(request, 'loginform_alumni.html')
            else:
                print("else email")
                Reg_student.objects.filter(email = f_email).update(password=reset_pass)
                messages.info(request,'Password changed successfully')
                return render(request, 'loginform_student.html')

    else:
        return render(request, 'profile.html')
