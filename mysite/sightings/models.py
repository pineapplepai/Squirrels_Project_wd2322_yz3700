from django.db import models
    
class Squirrel(models.Model):
    
    X = models.DecimalField(
	max_length = 25,
	)

    Y = models.DecimalField(
	max_length = 25,
	)

    Unique_Squirrel_ID = models.CharField(
	max_length = 20,
	)

    Shift_ = (
	('AM', _('AM')),
	('PM', _('PM')),
    ) 

    Shift = models.CharField(
	max_length = 2,
	choices = Shift_,
	)

    Date = models.DateField(
	max_length = 8,
	)

    Age = models.CharField(
	max_length = 10,
	)
    
    Color_ = (
	('Adult', _('Adult')),
	('Juvenile', _('Juvenile')),
	('Unknown', _('Unknown')),
	)

    Primary_Fur_Color = models.CharField(
	max_length = 15,
	choices = Color_,	
	)
    
    Location_ = (
	('Above Ground', _('Above Ground'),
	('Ground Plance', _('Ground plane'),
	)

    Location = models.CharField(
	max_length = 20,
	choices = Location_,
	)
 
    Specific_Location = models.CharField(
	max_length = 50,
	)
 
    Running_ = (
        ('True', _('True'),
        ('False', _('False'),
        )

    Running = (
	max_length = 5,
	choices = Running_,
	)

    Chasing_ = (
        ('True', _('True'),
        ('False', _('False'),
        )

    Chasing = (
        max_length = 5,
        choices = Chasing_,
        )

    Climbing_ = (
        ('True', _('True'),
        ('False', _('False'),
        )

    Climbing = (
        max_length = 5,
        choices = Climbing_,
        )

    Eating_ = (
        ('True', _('True'),
        ('False', _('False'),
        )

    Eating = (
        max_length = 5,
        choices = Eating_,
        )

    Foraging_ = (
        ('True', _('True'),
        ('False', _('False'),
        )

    Foraging = (
        max_length = 5,
        choices = Foraging_,
        )

    Other_Activities = (
	max_length = 100,
	)

    Kuks_ = (
        ('True', _('True'),
        ('False', _('False'),
        )

    Kuks = (
        max_length = 5,
        choices = Kuks_,
        )

    Quaas_ = (
        ('True', _('True'),
        ('False', _('False'),
        )

    Quaas = (
        max_length = 5,
        choices = Quaas_,
        )

    Moans_ = (
        ('True', _('True'),
        ('False', _('False'),
        )

    Moans = (
        max_length = 5,
        choices = Moans_,
        )

    Tail_flags_ = (
        ('True', _('True'),
        ('False', _('False'),
        )

    Tail_flags = (
        max_length = 5,
        choices = Tail_flags_,
        )

    Tail_twitches_ = (
        ('True', _('True'),
        ('False', _('False'),
        )

    Tail_twitches = ( 
        max_length = 5,
        choices = Tail_twitches_,
        )

    Approaches_ = (
        ('True', _('True'),
        ('False', _('False'),
        )

    Approaches = (
        max_length = 5,
        choices = Approaches_,
        )

    Indifferent_ = (
        ('True', _('True'),
        ('False', _('False'),
        )

    Indifferent = (
        max_length = 5,
        choices = Indifferent_,
        )

    Runs_from_ = (
        ('True', _('True'),
        ('False', _('False'),
        )

    Runs_from = (
        max_length = 5,
        choices = Runs_from_,
        )



