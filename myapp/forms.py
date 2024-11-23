from django import forms

class AverageForm(forms.Form):
    average_salary = forms.DecimalField(
        label="Average Salary",
        max_digits=10,
        decimal_places=2,
        required=True
    )
