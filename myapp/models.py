from django import forms

class AverageForm(forms.Form):
    average_price = forms.DecimalField(
        label="Average Price",
        max_digits=10,
        decimal_places=2,
        required=True
    )
    average_salary = forms.DecimalField(
        label="Average Salary",
        max_digits=10,
        decimal_places=2,
        required=True
    )
