from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'

# patient.doctors.all()
# doctor.patients.all()
class Patient(models.Model):
    name = models.CharField(max_length=200)
    doctors = models.ManyToManyField(Doctor, related_name='patients') # 역으로 접근할 수 있도록 이름을 지어주기.
    # doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    # 아예 여기 빼버렸다.

    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.doctor.id}번 의사의 {self.patient.id}번 환자'
    