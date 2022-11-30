from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Surah(models.Model):
    name_en = models.CharField(unique=True, max_length=64)
    name_ar = models.CharField(unique=True, max_length=64)
    ayas = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(286),
            MinValueValidator(3)
        ]
    )
    number = models.PositiveSmallIntegerField(primary_key=True, validators=[
        MaxValueValidator(114),
        MinValueValidator(1)
    ])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name_ar} ({self.name_en})'


class Session(models.Model):
    class AttendanceType(models.TextChoices):
        ATTENDED = 'AT', 'Attended'
        MISSED = 'MI', 'Missed'
        UNKNOWN = 'UN', 'Unknown'

    student = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField()
    attendance = models.CharField(max_length=2, choices=AttendanceType.choices, default=AttendanceType.UNKNOWN)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return f'{self.student.username} > {self.get_attendance_display()}'

    class Meta:
        unique_together = [['student', 'date']]


class Progress(models.Model):
    class ProgressType(models.TextChoices):
        HIFZ = 'HI', 'Hivz'
        REVISION = 'RE', 'Revision'

    surah = models.ForeignKey(Surah, on_delete=models.PROTECT)
    from_aya = models.PositiveSmallIntegerField()
    to_aya = models.PositiveSmallIntegerField()
    session = models.ForeignKey(Session, on_delete=models.PROTECT)
    type = models.CharField(max_length=2, choices=ProgressType.choices, default=ProgressType.HIFZ)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
