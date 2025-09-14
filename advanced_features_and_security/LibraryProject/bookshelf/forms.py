from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from .models import Book, CustomUser
import html
import re

class ExampleForm(forms.Form):
    """
    Example form demonstrating secure form practices including:
    - Input validation
    - HTML escaping
    - CSRF protection (handled automatically in templates)
    """
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your name'
        }),
        help_text="Enter your full name (letters and spaces only)"
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email'
        }),
        help_text="Enter a valid email address"
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Enter your message'
        }),
        help_text="Enter your message (500 characters maximum)",
        max_length=500
    )
    
    def clean_name(self):
        """Validate and sanitize the name field"""
        name = self.cleaned_data.get('name', '').strip()
        
        # HTML escape to prevent XSS
        name = html.escape(name)
        
        # Validate name contains only letters and spaces
        if not re.match(r'^[a-zA-Z\s]+$', name):
            raise ValidationError("Name can only contain letters and spaces.")
        
        if len(name) < 2:
            raise ValidationError("Name must be at least 2 characters long.")
        
        return name
    
    def clean_message(self):
        """Validate and sanitize the message field"""
        message = self.cleaned_data.get('message', '').strip()
        
        # HTML escape to prevent XSS
        message = html.escape(message)
        
        if len(message) < 10:
            raise ValidationError("Message must be at least 10 characters long.")
        
        # Check for potential malicious content
        malicious_patterns = [
            r'<script.*?>',
            r'javascript:',
            r'onerror=',
            r'onload=',
            r'alert\(.*?\)'
        ]
        
        for pattern in malicious_patterns:
            if re.search(pattern, message, re.IGNORECASE):
                raise ValidationError("Message contains invalid content.")
        
        return message