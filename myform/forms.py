from django import forms
class ContactForm(forms.Form):
	name = forms.CharField(max_length=30, 
		widget=forms.TextInput(attrs={
		# 'style': 'border-color: blue;',
		'placeholder': 'Write your name here'
		}))
	email = forms.EmailField(
		max_length=254, 
		widget= forms.EmailInput(attrs={
			# 'style': 'border-color: green;'
			'placeholder':'Write your Email here'}))
	message = forms.CharField(max_length=2000, widget=forms.Textarea(attrs={
		# 'style': 'border-color: orange;'
		}),
		help_text='Write here your message!')
	source   =   forms.CharField(max_length= 200, widget = forms.HiddenInput())
	def clean(self):
		cleaned_data= super(ContactForm, self).clean()
		name = cleaned_data.get('name')
		email = cleaned_data.get('email')
		message = cleaned_data.get('message')
		if not name and not email and not message:
			raise forms.ValidationError(' Try to fill in the form')
				