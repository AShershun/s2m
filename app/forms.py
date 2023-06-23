from django.forms import Form, ChoiceField, CharField


class SelectForm(Form):
    FILTER_CHOICES = (
        ('fullname', 'ПІБ'),
        ('department', 'Кафедра'),
        ('speciality', 'Спеціальність'),
        ('keyword', 'Ключеве слово'),
    )
    # search = CharField(required=False)
    select = ChoiceField(choices=FILTER_CHOICES)
