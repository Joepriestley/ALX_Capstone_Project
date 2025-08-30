from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
# Create your models here


class Departement(models.Model):
    DEPARTMENT_CHOICES=[
        ('choir', 'Choir'),
        ('minister_sherpherd', 'Minister Sherpherd'),
        ('media', 'Media'),
        ('organisatio_usher', 'Organisation & Usher'),
        ('outreach_visitation', 'Outreach & Visitation'),
        ('kitchen', 'Kitchen'),
        ('drama_team', 'Drama Team'),
    ]
    name=models.CharField(max_length=225,choices=DEPARTMENT_CHOICES, default='choir')
    leader = models.ForeignKey('Member', on_delete=models.SET_NULL, null=True, blank=True, related_name='leading_departments')
    
class Member(models.Model):
    
    STATUS_CHOICES=[
        ('pastor', 'Pastor'),
        ('elder', 'Elder'),
        ('leader', 'Leader'),
        ('worker', 'Worker'),
        ('n_member', 'Normal Member'),
        ('seeker', 'Seeker'),
        ('newcomer', 'New-comer'),
        ('visitor', 'Visitor'),
    ]
    first_name = models.CharField(max_length=100,null=True, blank=True)
    middle_name = models.CharField(max_length=100,null=True, blank=True)
    last_name = models.CharField(max_length=100,null=True, blank=True)
    phone = PhoneNumberField(null=True,blank=True, verbose_name="Phone Number")
    country =CountryField(blank_label=("Select Country"),null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    birth_date =models.DateField(null=True, blank=True)
    date_joined= models.DateTimeField(auto_now_add=True,null=True)
    last_updated=models.DateTimeField(auto_now=True) #Updates every time record is saved
    status= models.CharField(max_length=15, choices= STATUS_CHOICES, default='n_member')
    departement=models.ForeignKey(Departement, on_delete=models.SET_NULL, null=True)
    occupation=models.CharField(max_length=100, null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.departement} ({self.status})"
    
class StatusHistory(models.Model):
    
    STATUS_CHOICES=[
        ('pastor', 'Pastor'),
        ('elder', 'Elder'),
        ('leader', 'Leader'),
        ('worker', 'Worker'),
        ('n_member', 'Normal Member'),
        ('seeker', 'Seeker'),
        ('newcomer', 'New-comer'),
        ('visitor', 'Visitor'),
    ]
    
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    old_status=models.CharField(max_length=10, choices= STATUS_CHOICES, default='n_member')
    new_status=models.CharField(max_length=10, choices= STATUS_CHOICES, default='n_member')
    date_changed=models.DateTimeField(auto_now_add=True,null=True,)
    
    def __str__(self):
        return f"{self.member} old status: {self.old_status} New Status:{self.new_status}"
    

class Attendance(models.Model):
    
    EVENT_CHOICES=[
        ('sunday_service', 'Sunday Service'),
        ('national_program', 'National Program'),
        ('special_program', 'Special program'),
        
    ]
    STATUS_CHOICES=[
        ('present', 'Present'),
        ('absent', 'Absent'),
        
    ]
     
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    event_date=models.DateTimeField(auto_now_add=True,null=True)
    event_type =models.CharField(max_length=20, choices= EVENT_CHOICES, default='sunday_service')
    status =models.CharField(max_length=20, choices= STATUS_CHOICES, default='present')
    
    def __str__(self):
        return f"{self.member} - {self.event_type} on {self.event_date} ({self.status})"
