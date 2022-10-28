from django import forms
from account.forms import SignUpBuyerForm, SignUpSellerForm

class UpdateProfilBuyer(forms.ModelForm):
    class Meta:
        model = SignUpBuyerForm
        fields = ['nama','username','email','password']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = SignUpBuyerForm.objects.exclude(pk=self.instance.pk).get(email=email)
        except SignUpBuyerForm.DoesNotExist:
            return email
        raise forms.ValidationError("Email is already in use")
    def save(self, commit=True):
        account = super(UpdateProfilBuyer, self).save(commit=False)
        account.email = self.cleaned_data['email']
        if commit:
            account.save()
        return account

class UpdateProfilSeller(forms.ModelForm):
    class Meta:
        model = SignUpSellerForm
        fields = ['nama','username','email','password','namausaha','deskripsi','alamat','kontak','linktoko']

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        try:
            account = SignUpSellerForm.objects.exclude(pk=self.instance.pk).get(email=email)
        except SignUpSellerForm.DoesNotExist:
            return email
        raise forms.ValidationError("Email is already in use")
    def save(self, commit=True):
        account = super(UpdateProfilSeller, self).save(commit=False)
        account.email = self.cleaned_data['email']
        if commit:
            account.save()
        return account
