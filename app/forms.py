from django.forms import Form, ChoiceField


class SelectForm(Form):
    FILTER_CHOICES = (
        ('fullname', 'ПІБ'),
        ('department', 'Кафедра'),
        ('speciality', 'Спеціальність'),
        ('keyword', 'Ключове слово'),
    )
    
    select = ChoiceField(choices=FILTER_CHOICES)
