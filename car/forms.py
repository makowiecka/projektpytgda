from django import forms


class CarForm(forms.ModelForm):
    brand = forms.CharField(
        label='Marka samochodu',
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-lg pr-4 shadow-none',
                   'placeholder': 'marka'}
        )
    )

    model = forms.CharField(
        label='Model samochodu',
        widget=forms.TextInput(
            attrs={'class': 'form-control form-control-lg pr-4 shadow-none',
                   'placeholder': 'model'}
        )
    )

    # production_year = forms.CharField(
    #     label='Treść newsa',
    #     widget=forms.Textarea(
    #         attrs={'class': 'form-control form-control-lg pr-4 shadow-none'}
    #     )
    # )
    #
    # category = forms.CharField(
    #     # queryset=Categories.objects.all(),
    #     label='Kategoria',
    #     widget=ListTextWidget(
    #         name="category",
    #         data_list=Categories.objects.all(),
    #         attrs={'class': 'form-control form-control-lg pr-4 shadow-none'}
    #     )
    # )