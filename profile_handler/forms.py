# from django import forms
from django import forms as auth_forms
from account.forms import SignUpBuyerForm, SignUpSellerForm
from account.models import User
from django.contrib.auth.forms import UserChangeForm, ReadOnlyPasswordHashField

class BuyerEditProfileForm(UserChangeForm):
    # password = auth_forms.ReadOnlyPasswordHashField(label="Password",
    #     help_text="Raw passwords are not stored, so there is no way to see "
    #             "this user's password, but you can change the password "
    #             "using <a href=\"password/\">this form</a>.")

    class Meta:
        model = User
        # fields = ['nama','username','email','password']
        # help_texts = {
        #     'password ':(''),
        # }
        fields = ['username', 'email']
    
    # def clean_password(self):
    #     return self.initial["password"]

    # def clean_password(self):
    #     # Regardless of what the user provides, return the initial value.
    #     # This is done here, rather than on the field, because the
    #     # field does not have access to the initial value
    #     return self.initial["password"]
        

class SellerEditProfileForm(UserChangeForm):
    class Meta:
        model = User
        # fields = ['nama','username','email','password']
        fields = ['username', 'email']

    # def clean_email(self):
    #     email = self.cleaned_data['email'].lower()
    #     try:
    #         account = User.objects.exclude(pk=self.instance.pk).get(email=email)
    #     except User.DoesNotExist:
    #         return email
    #     raise forms.ValidationError("Email is already in use")
    # def save(self, commit=True):
    #     account = super(UpdateProfilBuyer, self).save(commit=False)
    #     account.email = self.cleaned_data['email']
    #     if commit:
    #         account.save()
    #     return account

# class UpdateProfilSeller(forms.ModelForm):
#     # class Meta:
#     #     model = SignUpSellerForm
#     #     fields = ['nama','username','email','password','namausaha','deskripsi','alamat','kontak','linktoko']

#     def clean_email(self):
#         email = self.cleaned_data['email'].lower()
#         try:
#             account = SignUpSellerForm.objects.exclude(pk=self.instance.pk).get(email=email)
#         except SignUpSellerForm.DoesNotExist:
#             return email
#         raise forms.ValidationError("Email is already in use")
#     def save(self, commit=True):
#         account = super(UpdateProfilSeller, self).save(commit=False)
#         account.email = self.cleaned_data['email']
#         if commit:
#             account.save()
#         return account
