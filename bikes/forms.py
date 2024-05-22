from django import forms
from .models import Bike, Review


class BikeForm(forms.ModelForm):
    class Meta:
        model = Bike
        fields = ['bikemodel', 'image', 'bikecolor', 'size', 'price', 'miqdori', 'category']
        widgets = {
            'bikecolor': forms.TextInput(attrs={'type': 'color'}),
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'star_given']


class AddReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'star_given']
