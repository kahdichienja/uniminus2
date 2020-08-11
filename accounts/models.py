from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserRegistration(models.Model):
    """Model definition for UserRegistration."""

    # TODO: Define fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    index_number_year = models.CharField(max_length=191) 
    adm_no = models.CharField(max_length=191) 
    student_name = models.CharField(max_length=191) 
    kcse_mean_grade = models.CharField(max_length = 20, blank=True, null=True) 
    other_institution_attended = models.CharField(max_length = 191, blank=True, null=True)  
    institution_qualification = models.TextField(max_length = 191, blank=True, null=True)  
    id_passport_no = models.CharField(max_length = 120, blank=True, null=True) 
    birth_cert_no = models.CharField(max_length = 120, blank=True, null=True) 
    nationality = models.CharField(max_length = 191, blank=True, null=True) 
    ethinicity = models.CharField(max_length = 120, blank=True, null=True) 
    physicaly_impaired = models.CharField(max_length = 120, blank=True, null=True) 
    physicaly_impaired_details = models.TextField(null=True, blank = True) 
    phone_number = models.CharField(max_length=191, blank=True, null=True ) 
    phone_number2 = models.CharField(max_length=191,blank=True, null=True) 
    box = models.CharField(max_length=191, blank=True, null=True) 
    postalcode = models.CharField(max_length=191, blank=True, null=True) 
    town = models.CharField(max_length=191, blank=True, null=True) 
    school = models.CharField(max_length=191, blank=True, null=True) 
    name_and_address_of_school_attended_o_level = models.CharField(max_length=191, blank=True, null=True) 
    email = models.EmailField(blank=True, null=True) 
    joined_date = models.CharField(max_length=191, blank=True, null=True) 
    gender = models.CharField(max_length=191, blank=True, null=True) 
    salutation = models.CharField(max_length=191, blank=True, null=True) 
    religion = models.CharField(max_length=191, blank=True, null=True) 
    mstatus = models.CharField(max_length=191, blank=True, null=True) 
    dob = models.CharField(max_length=191, blank=True, null=True) 
    profile_picture = models.ImageField(upload_to='UserProfiles', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Unicode representation of UserRegistration."""
        return f'{self.adm_no}'


class UserRUCF1(models.Model):
    """Model definition for UserRUCF1."""

    # TODO: Define fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f1form = models.FileField(upload_to='f1form')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Unicode representation of UserRUCF1."""
        return f'{self.user}'

class UserRUM(models.Model):
    """Model definition for UserRUM."""

    # TODO: Define fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rumform = models.FileField(upload_to='rumform')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Unicode representation of UserRUM."""
        return f'{self.user}'
class UserRUCF2(models.Model):
    """Model definition for UserRUCF2."""

    # TODO: Define fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    f2form = models.FileField(upload_to='f2form')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Unicode representation of UserRUCF2."""
        return f'{self.user}'
class UserRUCA1(models.Model):
    """Model definition for UserRUCA1."""

    # TODO: Define fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    a1form = models.FileField(upload_to='a1form')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        """Unicode representation of UserRUCA1."""
        return f'{self.user}'

class Qualifications(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    details = models.TextField(default = 'None')
    def __str__(self):
        return f'{self.user}'


class PersonalFileUpload(models.Model):
    """Model definition for PersonalFileUpload."""

    # TODO: Define fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    adm_letter = models.FileField(upload_to='admletters')
    birth_cert = models.FileField(upload_to='birthcert')
    kcse_cert = models.FileField(upload_to='kcsecert', blank=True, null=True)
    result_slip = models.FileField(upload_to='resultslip')
    national_id = models.FileField(upload_to='nationalid', blank=True, null=True)
    sec_leaving_cert = models.FileField(upload_to='leavingcert', blank=True, null=True)


    def __str__(self):
        """Unicode representation of PersonalFileUpload."""
        return f'{self.user}'



class Referee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    referee_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    telepnone = models.CharField(max_length=12, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    postalcode = models.CharField(max_length=191, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.referee_name}'