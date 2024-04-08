from django import forms


# login form
class LoginForm(forms.Form):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control",
                "autocomplete": "off",
            }
        )
    )

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        )
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control",
                "autocomplete": "off",
            }
        )
    )

    email = forms.CharField(
        label="",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control",
                "autocomplete": "off",
            }
        )
    )

    password = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        )
    )

    confirmation = forms.CharField(
        label="",
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password Confirmation",
                "class": "form-control"
            }
        )
    )