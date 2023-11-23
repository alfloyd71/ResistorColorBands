from django.db import models


FIRSTBAND_CHOICES = (
    ('Brown','Brown      1'),
    ('Red','Red          2'),
    ('Orange','Orange    3'),
    ('Yellow','Yellow    4'),
    ('Green','Green      5'),
    ('Blue','Blue        6'),
    ('Violet','Violet    7'),
    ('Grey','Grey        8'),
    ('White','White      9'),
)

SECONDBAND_CHOICES = (
    ('Black','Black      0'),
    ('Brown','Brown      1'),
    ('Red','Red          2'),
    ('Orange','Orange    3'),
    ('Yellow','Yellow    4'),
    ('Green','Green      5'),
    ('Blue','Blue        6'),
    ('Violet','Violet    7'),
    ('Grey','Grey        8'),
    ('White','White      9'),
)

THIRDBAND_CHOICES = (
    ('Black','Black      x1Ω'),
    ('Brown','Brown      x10Ω'),
    ('Red','Red          x100Ω'),
    ('Orange','Orange    x1kΩ'),
    ('Yellow','Yellow    x10kΩ'),
    ('Green','Green      x100kΩ'),
    ('Blue','Blue        x1MΩ'),
    ('Violet','Violet    x10MΩ'),
    ('Grey','Grey        x100MΩ'),
    ('White','White      x1GΩ'),
    ('Gold','Gold        x0.1Ω'),
    ('Silver','Silver   x.01Ω'), 
)

FOURTHBAND_CHOICES = (
    ('Brown','Brown      +-1%'),
    ('Red','Red          +-2%'),
    ('Green','Green     +-0.5%'),
    ('Blue','Blue        +-0.25%'),
    ('Violet','Violet    +-0.1%'),
    ('Grey','Grey        +-0.05%'),
    ('Gold','Gold        +-5%'),
    ('Silver','Silver    +-10%'),
)

class RCB(models.Model):

    firstband = models.CharField(max_length=100, choices=FIRSTBAND_CHOICES, default='Red')
    secondband = models.CharField(max_length=100, choices=SECONDBAND_CHOICES, default='Green')
    thirdband = models.CharField(max_length=100, choices=THIRDBAND_CHOICES, default='Blue')
    fourthband = models.CharField(max_length=100, choices=FOURTHBAND_CHOICES, default='Gold')
    resistancevalue = models.CharField(max_length=100, default='100')
    


    def __str__(self):
        return str(self.id)


