from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django.db.models import Q

from children.models import Children, ChildrenGroup
from profileapp.models import Profile
from schedule.models import Lesson, ChildrenScopeResult, Survey, Scope


class DateInput(forms.DateInput):
    input_type = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)


class TimeInput(forms.TimeInput):
    input_type = "time"


class UpdateChildrenForm(forms.ModelForm):
    class Meta:
        model = Children
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["BornDate"].widget = DateInput()

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class ChildrenForm(forms.ModelForm):
    class Meta:
        model = Children
        fields = "__all__"
        widgets = {'Group': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["BornDate"].widget = DateInput()

        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class UserForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.filter(~Q(id=0)),
                                   required=True, label="Должность")
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "group"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["LastName", "FirstName", "MiddleName", "BornDate"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class UserGroupUpdateForm(forms.ModelForm):
    group = forms.ModelChoiceField(queryset=Group.objects.filter(~Q(id=0)),
                                   required=True, label="Должность")
    class Meta:
        model = User
        fields = ["group"]

class GroupForm(forms.ModelForm):
    class Meta:
        model = ChildrenGroup
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        """self.Mentor = self.instance.Mentor.User.Profile.FirstName.__str__()"""
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = "__all__"
        widgets = {'Group': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["Date"].widget = DateInput()
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class ResultForm(forms.ModelForm):
    class Meta:
        model = ChildrenScopeResult
        fields = "__all__"
        widgets = {'Group': forms.HiddenInput(), "Survey": forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = "__all__"
        widgets = {'Group': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'

class ScopeForm(forms.ModelForm):
    class Meta:
        model = Scope
        fields = "__all__"
        widgets = {'Survey': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'