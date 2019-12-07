from django.db import models

class Squirrel(models.Model):

    X = models.DecimalField(
    max_digits = 25,
    decimal_places = 15,
	)

    Y = models.DecimalField(
	max_digits = 25,
    decimal_places = 15,
	)

    Unique_Squirrel_ID = models.CharField(
	max_length = 20,
	)

    AM = 'AM'
    PM = 'PM'

    Shift_ = (
        (AM, 'AM'),
        (PM, 'PM'),
    )

    Shift = models.CharField(
	   max_length = 2,
	   choices = Shift_,
	)

    Date = models.DateField(
	max_length = 8,
	)

    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Unknown = 'Unknown'
    Blank = ''

    Age_ = (
	   (Adult, 'Adult'),
	   (Juvenile, 'Juvenile'),
	   (Unknown, '?'),
       (Blank, ''),
	)

    Age = models.CharField(
	max_length = 10,
    choices = Age_,
	)

    Gray = 'Gray'
    Cinnamon = 'Cinnamon'
    Black = 'Black'
    Blank = ''

    Color_ = (
	   (Gray, 'Gray'),
	   (Cinnamon, 'Cinnamon'),
	   (Black, 'Black'),
       (Blank, ''),
	)

    Primary_Fur_Color = models.CharField(
	max_length = 15,
	choices = Color_,
	)

    Above_Ground = 'Above Ground'
    Ground_Plance = 'Ground plane'

    Location_ = (
	(Above_Ground, 'Above Ground'),
	(Ground_Plance, 'Ground plane'),
	)

    Location = models.CharField(
	max_length = 20,
	choices = Location_,
	)

    Specific_Location = models.CharField(
	max_length = 50,
	)

    TRUE = 'True'
    FALSE = 'False'

    Running_ = (
        (TRUE, 'True'),
        (FALSE, 'False'),
        )

    Running = models.CharField(
    max_length = 5,
	choices = Running_,
	)

    TRUE = 'True'
    FALSE = 'False'

    Chasing_ = (
        (TRUE, 'True'),
        (FALSE, 'False'),
        )

    Chasing = models.CharField(
        max_length = 5,
        choices = Chasing_,
        )

    TRUE = 'True'
    FALSE = 'False'

    Climbing_ = (
        (TRUE, 'True'),
        (FALSE, 'False'),
        )

    Climbing = models.CharField(
        max_length = 5,
        choices = Climbing_,
        )

    TRUE = 'True'
    FALSE = 'False'

    Eating_ = (
        (TRUE, 'True'),
        (FALSE, 'False'),
        )

    Eating = models.CharField(
        max_length = 5,
        choices = Eating_,
        )

    TRUE = 'True'
    FALSE = 'False'

    Foraging_ = (
        (TRUE, 'True'),
        (FALSE, 'False'),
        )

    Foraging = models.CharField(
        max_length = 5,
        choices = Foraging_,
        )

    Other_Activities = models.CharField(
	max_length = 100,
	)

    TRUE = 'True'
    FALSE = 'False'

    Kuks_ = (
        (TRUE, 'True'),
        (FALSE, 'False'),
        )

    Kuks = models.CharField(
        max_length = 5,
        choices = Kuks_,
        )

    TRUE = 'True'
    FALSE = 'False'

    Quaas_ = (
        (TRUE, 'True'),
        (FALSE, 'False'),
        )

    Quaas = models.CharField(
        max_length = 5,
        choices = Quaas_,
        )

    TRUE = 'True'
    FALSE = 'False'

    Moans_ = (
        (TRUE, 'True'),
        (FALSE, 'False'),
        )

    Moans = models.CharField(
        max_length = 5,
        choices = Moans_,
        )

    TRUE = 'True'
    FALSE = 'False'

    Tail_flags_ = (
        (TRUE, 'True'),
        (FALSE, 'False'),
        )

    Tail_flags = models.CharField(
        max_length = 5,
        choices = Tail_flags_,
        )

    TRUE = 'True'
    FALSE = 'False'

    Tail_twitches_ = (
        (TRUE, 'True'),
        (FALSE, 'False'),
        )

    Tail_twitches = models.CharField(
        max_length = 5,
        choices = Tail_twitches_,
        )

    TRUE = 'True'
    FALSE = 'False'

    Approaches_ = (
        (TRUE, 'True'),
        (FALSE, 'False'),
        )

    Approaches = models.CharField(
        max_length = 5,
        choices = Approaches_,
        )

    TRUE = 'True'
    FALSE = 'False'

    Indifferent_ = (
        (TRUE, 'True'),
        (FALSE, 'False'),
        )

    Indifferent = models.CharField(
        max_length = 5,
        choices = Indifferent_,
        )

    TRUE = 'True'
    FALSE = 'False'

    Runs_from_ = (
        (TRUE, 'True'),
        (FALSE, 'False'),
        )

    Runs_from = models.CharField(
        max_length = 5,
        choices = Runs_from_,
        )
