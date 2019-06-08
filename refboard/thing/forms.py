from django import forms


class NewThingForm(forms.Form):
    thing_name = forms.CharField(label="New Thing", max_length=255)


class NewThingyForm(forms.Form):
    thingy_name = forms.CharField(label="New Thingy", max_length=255)

