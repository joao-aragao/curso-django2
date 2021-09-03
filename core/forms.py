from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=255, required=False)
    email = forms.EmailField(
        label='Email', max_length=255, required=False)
    assunto = forms.CharField(
        label='Assunto', max_length=255, required=False)
    mensagem = forms.CharField(
        label='Mensagem', max_length=3000, required=False, widget=forms.Textarea())
