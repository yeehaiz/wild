from django import forms

class EventSaveForm(forms.Form):
    id = forms.IntegerField(required=False)
    title = forms.CharField()
    outline = forms.CharField()
    route = forms.CharField()
    type_id = forms.IntegerField()
    intensity = forms.ChoiceField(choices=[(x,x) for x in range(1, 6)])
    days = forms.IntegerField(min_value=0)
    places = forms.IntegerField(min_value=0)
    price = forms.DecimalField(min_value=0)
    # covers
    planning = forms.CharField()
    fee_desc = forms.CharField()
    equipment = forms.CharField()
