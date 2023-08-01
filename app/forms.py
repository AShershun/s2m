from django.forms import Form, ChoiceField, CharField


class SelectForm(Form):
    FILTER_CHOICES = (
        ('fullname', 'ПІБ'),
        ('department', 'Кафедра'),
        ('speciality', 'Спеціальність'),
        ('keyword', 'Ключове слово'),
    )
    # search = CharField(required=False)
    select = ChoiceField(choices=FILTER_CHOICES)
