from django import forms


# ----------------------- CUSTOM FORMS -------------------------

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


# register form
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



# ----------------------- CUSTOM FUNCTIONS -------------------------





# ----------------------- CUSTOM EXCEPTIONS -------------------------

class EmptyClass(Exception):
    pass


class InvalidLearners(Exception):
    pass

class EmptyPayer(Exception):
    pass

class MultiplePayers(Exception):
    pass