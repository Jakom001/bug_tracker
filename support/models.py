from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models


class Support(models.Model):
    Status = (
        ('New', 'New'),
        ('Completed', 'Completed'),
        ('Review', 'Review'),
    )
    Category = (
        ("Network", 'Network'),
        ("Printer", 'Printer'),
        ("CCTV", 'CCTV'),
        ("Software", 'Software'),
        ("Data/Files", 'Data/Files'),

    )

    name = models.CharField('Name (User)', max_length=255)
    date_created = models.DateTimeField('Date', editable=False, null=True)
    extension = models.IntegerField('Extension')
    department = models.CharField('Department', max_length=255)
    category = models.CharField(choices=Category, max_length=120, default='Network')
    summary = models.TextField('Summary/Issue', max_length=255)
    assigned = models.CharField('Assigned To', max_length=255)
    solution = models.TextField('Solution/Remarks', max_length=500, default="")
    status = models.CharField(choices=Status, max_length=120, default='New')

    class Meta:
        verbose_name_plural = 'Tasks'
        db_table = 'support'

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        self.date_created = timezone.now()
        return super(Support, self).save(*args, **kwargs)


    def __str__(self):
        return self.name
