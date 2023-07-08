from django import forms
from .models import Detail

class DetailForm(forms.ModelForm):
    class Meta:
        model=Detail
        fields=['name','DOB','Age','Gender','PhoneNo','Email','Address','Department','Course','Purpose','DebitNoteBook','Pen','ExamPaper']