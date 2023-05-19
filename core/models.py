from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
from django.utils import timezone



class Patient(User):

    """Class Patient for medical use"""

    phone_number = PhoneField(blank=True, help_text="Contact phone number")
    joining_date = models.DateTimeField(verbose_name="Date of joining", default=timezone.now)

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
    def __str__(self) -> str:
        return str(self.email)



class Doctor(User):

    """Class Doctor for medical use"""

    phone_number = PhoneField(blank=True, help_text="Contact phone number")
    joining_date = models.DateTimeField(verbose_name="Date of joining", default=timezone.now)

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctrors"
    def __str__(self) -> str:
        return str(self.email)
        

    
class Record(models.Model):

    """Class for medical use to record all data about patient."""

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    subject = models.CharField(verbose_name='Subject', max_length=255)
    description = models.TextField(verbose_name="Description", default='')
    prescription = models.TextField(verbose_name="Prescription", null=True, blank=True)
    oppointment_date = models.DateTimeField(verbose_name="Oppointment date.", default=timezone.now)
    meeting_date = models.DateTimeField(verbose_name="Meeting date of users.", default=None)

    def __str__(self) -> str:
        return self.subject


class ConversationAI(models.Model):

    """Class ConverstionAI for recording all char data between ChatGPT and patient"""

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    text = models.TextField()
    conversation_date = models.DateTimeField(verbose_name="Conv start", default=timezone.now)

