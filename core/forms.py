from django import forms


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=255, required=True)
    email = forms.EmailField(
        label='Email', max_length=255, required=True)
    assunto = forms.CharField(
        label='Assunto', max_length=255, required=True)
    mensagem = forms.CharField(
        label='Mensagem', max_length=3000, required=True, widget=forms.Textarea())
