"""
Forms for locator app
"""

from django import forms
from .models import Tournaments

from geo_utils import address_is_valid


class AddTournamentForm(forms.ModelForm):
    """
    ModleForm class for add tournaments page
    """
    class Meta:
        model = Tournaments


    def __init__(self, *args, **kwargs):
        """
        Assign custom error messages
        """
        super(AddTournamentForm, self).__init__(*args, **kwargs)

        self.fields['name'].error_messages = {
            'required': 'Name is a required field'}

        self.fields['address'].error_messages = {
            'required': 'Address is a required field'}

        self.fields['address'].validators.append(address_is_valid)

        self.fields['city'].error_messages = {
            'required': 'City is a required field'}

        self.fields['state'].error_messages = {
            'required': 'State is a required field'}

        self.fields['start_date'].error_messages = {
            'required': 'Start Date is a required field'}

        self.fields['end_date'].error_messages = {
            'required': 'End_Date is a required field'}


class SearchForm(forms.ModelForm):
    """
    ModleForm class for search tournaments page
    """
    class Meta:
        """
        Bind to tournaments model and assign fields
        """
        model = Tournaments
        fields = ('state',)

