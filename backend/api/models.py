from django.db import models

# Create your models here.
class Item(models.Model):
   
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    address = models.TextField(default='', blank=True)
    email = models.EmailField()
    contact_no = models.CharField(max_length=15)
    birthday = models.DateField(default='2000-01-01', blank=True)

    employment_status = models.CharField(max_length=100, blank=True)
    name_ext = models.CharField(max_length=10, blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, blank=True)
    sex = models.CharField(max_length=10, blank=True)
    civil_status = models.CharField(max_length=20, blank=True)
    height_m = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    blood_type = models.CharField(max_length=10, blank=True)
    gsis_no = models.CharField(max_length=20, blank=True)
    pagibig_no = models.CharField(max_length=20, blank=True)
    philhealth_no = models.CharField(max_length=20, blank=True)
    sss_no = models.CharField(max_length=20, blank=True)
    tin_no = models.CharField(max_length=20, blank=True)
    agency_em = models.CharField(max_length=100, blank=True)
    citizenship = models.CharField(max_length=50, blank=True)
    residential_house_no = models.CharField(max_length=10, blank=True)
    residential_street = models.CharField(max_length=100, blank=True)
    residential_subd = models.CharField(max_length=100, blank=True)
    residential_brgy = models.CharField(max_length=100, blank=True)
    residential_city = models.CharField(max_length=100, blank=True)
    residential_province = models.CharField(max_length=100, blank=True)
    residential_zipcode = models.CharField(max_length=10, blank=True)
    permanent_house_no = models.CharField(max_length=10, blank=True)
    permanent_street = models.CharField(max_length=100, blank=True)
    permanent_subd = models.CharField(max_length=100, blank=True)
    permanent_brgy = models.CharField(max_length=100, blank=True)
    permanent_city = models.CharField(max_length=100, blank=True)
    permanent_province = models.CharField(max_length=100, blank=True)
    permanent_zipcode = models.CharField(max_length=10, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    mobile_number = models.CharField(max_length=20, blank=True)
    spouse_surname = models.CharField(max_length=100, blank=True)
    spouse_first_name = models.CharField(max_length=100, blank=True)
    spouse_middle_name = models.CharField(max_length=100, blank=True)
    spouse_name_ext = models.CharField(max_length=10, blank=True)
    spouse_occupation = models.CharField(max_length=100, blank=True)
    spouse_employer = models.CharField(max_length=100, blank=True)
    spouse_business_address = models.CharField(max_length=200, blank=True)
    spouse_telephone = models.CharField(max_length=20, blank=True)
    elementary_education = models.CharField(max_length=200, blank=True)
    secondary_education = models.CharField(max_length=200, blank=True)
    father_surname = models.CharField(max_length=100, blank=True)
    father_first_name = models.CharField(max_length=100, blank=True)
    father_middle_name = models.CharField(max_length=100, blank=True)
    father_name_ext = models.CharField(max_length=10, blank=True)
    mother_surname = models.CharField(max_length=100, blank=True)
    mother_first_name = models.CharField(max_length=100, blank=True)
    mother_middle_name = models.CharField(max_length=100, blank=True)
   
    
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    
