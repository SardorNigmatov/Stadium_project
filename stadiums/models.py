from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime, timedelta




class StadiumsModels(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=300)
    contact =  models.CharField(
        max_length=16,
        blank=True,
        null=True,
        validators=[
          RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
          ),
        ],
      )
    img = models.ImageField(upload_to='news/',blank=True,null=True)
    stadium_about = models.CharField(max_length=250)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'stadiums'

# Create your models here.
class BronModel(models.Model):
    stadion_id = models.ForeignKey(StadiumsModels, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(
        max_length=16,
        blank=True,
        null=True,
        validators=[
          RegexValidator(
            regex=r'^\+?1?\d{9,15}$',
            message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
          ),
        ],
      )
    date = models.DateField()
    begin_time = models.TimeField(default=datetime.now)
    end_time = models.TimeField(default=datetime.now)
    is_broned = models.BooleanField(default=False)