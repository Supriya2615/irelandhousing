from django import forms



def year_choices():
    return [(r, r) for r in range(1984, 2017)]


CHART_CHOICES = (
    ('#1', 'BAR CHART'),
    ('#2', 'LINE CHART'),
)

RESULT_CHOICES = (
    ('National', 'National'),
    ('Dublin', 'Dublin'),
    ('Cork', 'Cork'),
    ('Galway', 'Galway'),
    ('Limerick', 'Limerick'),
    ('Waterford', 'Waterford'),
    ('Other areas', 'Other areas'),
)


class ReportSearchForm(forms.Form):
    year_from = forms.ChoiceField(choices=year_choices())
    year_to = forms.ChoiceField(choices=year_choices())
    chart_type = forms.ChoiceField(choices=CHART_CHOICES)
    show_results_of = forms.ChoiceField(choices=RESULT_CHOICES)
    compare_results_to = forms.ChoiceField(choices=RESULT_CHOICES)
