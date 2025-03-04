from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Reg_student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    collage_id = models.CharField(primary_key=True,max_length=10)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=10)
    class Meta:
        db_table="Reg_student"

class Reg_alumni(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    collage_id = models.CharField(primary_key=True,max_length=12)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=10)
    sem = models.CharField(max_length=6, default=False)
    # forget_password_token = models.CharField(max_length=100)
    class Meta:
        db_table="Reg_alumni"
    
class Profile(models.Model):
    full_name= models.CharField(max_length=50)
    email= models.EmailField(max_length=50)
    collage_id= models.ForeignKey('Reg_alumni',on_delete=models.CASCADE,null=True, default=None)
    branch= models.CharField(max_length=50)
    passout_year= models.CharField(max_length=10)
    gender=models.CharField(max_length=6)
    permanent_address= models.TextField()
    home_town= models.CharField(max_length=100)

    class Meta:
        db_table="Profile"

class Education(models.Model):
    gre=models.CharField(max_length=10)
    toefl=models.CharField(max_length=10)
    ielts=models.CharField(max_length=10)
    cpi6=models.CharField(max_length=10)
    cpi7=models.CharField(max_length=10)
    backlog6=models.CharField(max_length=10)
    backlog7= models.CharField(max_length=10)
    collage=models.CharField(max_length=50)
    collage_country=models.CharField(max_length=20)
    collage_city=models.CharField(max_length=20)
    collage_branch=models.CharField(max_length=50)
    collage_id= models.ForeignKey('Reg_alumni',on_delete=models.CASCADE, null=True, default=None)
    class Meta:
        db_table="Education"


class AppliedClg(models.Model):
    country1=models.CharField(max_length=30)
    c1_clg1=models.CharField(max_length=50)
    c1_state1=models.CharField(max_length=30)
    c1_city1=models.CharField(max_length=30)
    c1_appfees1=models.CharField(max_length=30)
    c1_coursefees1=models.CharField(max_length=30)
    c1_course1=models.CharField(max_length=30)
    c1_gre1=models.CharField(max_length=10)
    c1_toefl1=models.CharField(max_length=10)
    c1_ielts1=models.CharField(max_length=10)

    c1_clg2=models.CharField(max_length=50)
    c1_state2=models.CharField(max_length=30)
    c1_city2=models.CharField(max_length=30)
    c1_appfees2=models.CharField(max_length=30)
    c1_coursefees2=models.CharField(max_length=30)
    c1_course2=models.CharField(max_length=30)
    c1_gre2=models.CharField(max_length=10)
    c1_toefl2=models.CharField(max_length=10)
    c1_ielts2=models.CharField(max_length=10)

    c1_clg3=models.CharField(max_length=50)
    c1_state3=models.CharField(max_length=30)
    c1_city3=models.CharField(max_length=30)
    c1_appfees3=models.CharField(max_length=30)
    c1_coursefees3=models.CharField(max_length=30)
    c1_course3=models.CharField(max_length=30)
    c1_gre3=models.CharField(max_length=10)
    c1_toefl3=models.CharField(max_length=10)
    c1_ielts3=models.CharField(max_length=10)

    country2=models.CharField(max_length=30)
    c2_clg1=models.CharField(max_length=50)
    c2_state1=models.CharField(max_length=30)
    c2_city1=models.CharField(max_length=30)
    c2_appfees1=models.CharField(max_length=30)
    c2_coursefees1=models.CharField(max_length=30)
    c2_course1=models.CharField(max_length=30)
    c2_gre1=models.CharField(max_length=10)
    c2_toefl1=models.CharField(max_length=10)
    c2_ielts1=models.CharField(max_length=10)

    c2_clg2=models.CharField(max_length=50)
    c2_state2=models.CharField(max_length=30)
    c2_city2=models.CharField(max_length=30)
    c2_appfees2=models.CharField(max_length=30)
    c2_coursefees2=models.CharField(max_length=30)
    c2_course2=models.CharField(max_length=30)
    c2_gre2=models.CharField(max_length=10)
    c2_toefl2=models.CharField(max_length=10)
    c2_ielts2=models.CharField(max_length=10)

    c2_clg3=models.CharField(max_length=50)
    c2_state3=models.CharField(max_length=30)
    c2_city3=models.CharField(max_length=30)
    c2_appfees3=models.CharField(max_length=30)
    c2_coursefees3=models.CharField(max_length=30)
    c2_course3=models.CharField(max_length=30)
    c2_gre3=models.CharField(max_length=10)
    c2_toefl3=models.CharField(max_length=10)
    c2_ielts3=models.CharField(max_length=10)
    collage_id= models.ForeignKey('Reg_alumni',on_delete=models.CASCADE, null=True, default=None)

    class Meta:
        db_table="AppliedClg"

class Coaching(models.Model):
    course_name_gre=models.CharField(max_length=50)
    center_name_gre=models.CharField(max_length=50)
    center_city_gre=models.CharField(max_length=50)
    coaching_fees_gre=models.CharField(max_length=10)
    feedback_gre=models.TextField()

    course_name_toefl=models.CharField(max_length=50)
    center_name_toefl=models.CharField(max_length=50)
    center_city_toefl=models.CharField(max_length=50)
    coaching_fees_toefl=models.CharField(max_length=10)
    feedback_toefl=models.TextField()

    course_name_ielts=models.CharField(max_length=50)
    center_name_ielts=models.CharField(max_length=50)
    center_city_ielts=models.CharField(max_length=50)
    coaching_fees_ielts=models.CharField(max_length=10)
    feedback_ielts=models.TextField()

    course_name_other=models.CharField(max_length=50)
    center_name_other=models.CharField(max_length=50)
    center_city_other=models.CharField(max_length=50)
    coaching_fees_other=models.CharField(max_length=10)
    feedback_other=models.TextField()
    collage_id= models.ForeignKey('Reg_alumni',on_delete=models.CASCADE, null=True, default=None)
    class Meta:
        db_table="Coaching"

class Consultancy(models.Model):
    service_name= models.CharField(max_length=50)
    service_city= models.CharField(max_length=20)
    service_address=models.TextField()
    service_number=models.CharField(max_length=15)
    service_fees=models.CharField(max_length=10)
    consulting_countries=models.TextField()
    collage_id= models.ForeignKey('Reg_alumni',on_delete=models.CASCADE, null=True, default=None)
    class Meta:
        db_table="Consultancy"

class Residencial(models.Model):
    res_country= models.CharField(max_length=50)
    res_state= models.CharField(max_length=50)
    res_city= models.CharField(max_length=50)
    res_address= models.TextField()
    res_rent=models.CharField(max_length=50)
    res_utility_exp=models.CharField(max_length=50)
    res_monthly_exp=models.CharField(max_length=50)
    useful_things=models.TextField()
    collage_id= models.ForeignKey('Reg_alumni',on_delete=models.CASCADE, null=True, default=None)
    class Meta:
         db_table="Residencial"

class Flight(models.Model):
    flight_name = models.CharField(max_length=50)
    site_name = models.CharField(max_length=100)
    airport_exp = models.CharField(max_length=30)
    # flight_mode=models.CharField(max_length=6)
    from_where = models.CharField(max_length=30)
    to_where = models.CharField(max_length=30)
    leave_over_place = models.CharField(max_length=30)
    leave_over_time = models.CharField(max_length=30)
    collage_id= models.ForeignKey('Reg_alumni',on_delete=models.CASCADE, null=True, default=None)
    class Meta:
        db_table="Flight"

class All(models.Model):
    full_name= models.CharField(max_length=30)
    email= models.EmailField(max_length=15)
    branch= models.CharField(max_length=15)
    passout_year= models.CharField(max_length=4)
    gender=models.CharField(max_length=6)
    permanent_address= models.TextField(max_length=130)
    home_town= models.CharField(max_length=15)

    gre=models.CharField(max_length=5)
    toefl=models.CharField(max_length=5)
    ielts=models.CharField(max_length=5)
    cpi6=models.CharField(max_length=5)
    cpi7=models.CharField(max_length=5)
    backlog6=models.CharField(max_length=3)
    backlog7= models.CharField(max_length=3)
    collage=models.CharField(max_length=20)
    collage_country=models.CharField(max_length=15)
    collage_city=models.CharField(max_length=15)
    collage_branch=models.CharField(max_length=15)

    country1=models.CharField(max_length=15)
    c1_clg1=models.CharField(max_length=20)
    c1_state1=models.CharField(max_length=15)
    c1_city1=models.CharField(max_length=15)
    c1_appfees1=models.CharField(max_length=6)
    c1_coursefees1=models.CharField(max_length=7)
    c1_course1=models.CharField(max_length=15)
    c1_gre1=models.CharField(max_length=5)
    c1_toefl1=models.CharField(max_length=5)
    c1_ielts1=models.CharField(max_length=5)

    c1_clg2=models.CharField(max_length=20)
    c1_state2=models.CharField(max_length=15)
    c1_city2=models.CharField(max_length=15)
    c1_appfees2=models.CharField(max_length=6)
    c1_coursefees2=models.CharField(max_length=7)
    c1_course2=models.CharField(max_length=15)
    c1_gre2=models.CharField(max_length=5)
    c1_toefl2=models.CharField(max_length=5)
    c1_ielts2=models.CharField(max_length=5)

    c1_clg3=models.CharField(max_length=20)
    c1_state3=models.CharField(max_length=15)
    c1_city3=models.CharField(max_length=15)
    c1_appfees3=models.CharField(max_length=6)
    c1_coursefees3=models.CharField(max_length=7)
    c1_course3=models.CharField(max_length=15)
    c1_gre3=models.CharField(max_length=5)
    c1_toefl3=models.CharField(max_length=5)
    c1_ielts3=models.CharField(max_length=5)

    country2=models.CharField(max_length=20)
    c2_clg1=models.CharField(max_length=15)
    c2_state1=models.CharField(max_length=15)
    c2_city1=models.CharField(max_length=15)
    c2_appfees1=models.CharField(max_length=6)
    c2_coursefees1=models.CharField(max_length=7)
    c2_course1=models.CharField(max_length=15)
    c2_gre1=models.CharField(max_length=5)
    c2_toefl1=models.CharField(max_length=5)
    c2_ielts1=models.CharField(max_length=5)

    c2_clg2=models.CharField(max_length=20)
    c2_state2=models.CharField(max_length=15)
    c2_city2=models.CharField(max_length=15)
    c2_appfees2=models.CharField(max_length=6)
    c2_coursefees2=models.CharField(max_length=7)
    c2_course2=models.CharField(max_length=15)
    c2_gre2=models.CharField(max_length=5)
    c2_toefl2=models.CharField(max_length=5)
    c2_ielts2=models.CharField(max_length=5)

    c2_clg3=models.CharField(max_length=20)
    c2_state3=models.CharField(max_length=15)
    c2_city3=models.CharField(max_length=15)
    c2_appfees3=models.CharField(max_length=6)
    c2_coursefees3=models.CharField(max_length=7)
    c2_course3=models.CharField(max_length=15)
    c2_gre3=models.CharField(max_length=5)
    c2_toefl3=models.CharField(max_length=5)
    c2_ielts3=models.CharField(max_length=5)

    course_name_gre=models.CharField(max_length=15)
    center_name_gre=models.CharField(max_length=10)
    center_city_gre=models.CharField(max_length=15)
    coaching_fees_gre=models.CharField(max_length=6)
    feedback_gre=models.TextField(max_length=60)

    course_name_toefl=models.CharField(max_length=15)
    center_name_toefl=models.CharField(max_length=10)
    center_city_toefl=models.CharField(max_length=15)
    coaching_fees_toefl=models.CharField(max_length=6)
    feedback_toefl=models.TextField(max_length=60)

    course_name_ielts=models.CharField(max_length=15)
    center_name_ielts=models.CharField(max_length=10)
    center_city_ielts=models.CharField(max_length=15)
    coaching_fees_ielts=models.CharField(max_length=6)
    feedback_ielts=models.TextField(max_length=60)

    course_name_other=models.CharField(max_length=15)
    center_name_other=models.CharField(max_length=10)
    center_city_other=models.CharField(max_length=15)
    coaching_fees_other=models.CharField(max_length=6)
    feedback_other=models.TextField(max_length=60)

    service_name= models.CharField(max_length=15)
    service_city= models.CharField(max_length=15)
    service_address=models.TextField(max_length=60)
    service_number=models.CharField(max_length=14)
    service_fees=models.CharField(max_length=5)
    consulting_countries=models.TextField(max_length=50)
                         
    res_country= models.CharField(max_length=15)
    res_state= models.CharField(max_length=15)
    res_city= models.CharField(max_length=15)
    res_address= models.TextField(max_length=50)
    res_rent=models.CharField(max_length=5)
    res_utility_exp=models.CharField(max_length=5)
    res_monthly_exp=models.CharField(max_length=6)
    useful_things=models.TextField(max_length=80)

    flight_name = models.CharField(max_length=15)
    site_name = models.CharField(max_length=15)
    airport_exp = models.CharField(max_length=5)
    from_where = models.CharField(max_length=15)
    to_where = models.CharField(max_length=15)
    leave_over_place = models.CharField(max_length=15)
    leave_over_time = models.CharField(max_length=15)

    collage_id= models.ForeignKey('Reg_alumni',on_delete=models.CASCADE,null=True, default=None)

    class Meta:
        db_table="All"

class Admin(models.Model):
    admin_first_name = models.CharField(max_length=20)
    admin_last_name = models.CharField(max_length=20)
    admin_email = models.EmailField(primary_key=True,max_length=50)
    admin_number = models.CharField(max_length=15)
    admin_password = models.CharField(max_length=10)
    class Meta:
        db_table="Admin"

class Resetpass(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    forget_password_token = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table="Resetpass"

    def __str__(self):
        return self.user.username
                         