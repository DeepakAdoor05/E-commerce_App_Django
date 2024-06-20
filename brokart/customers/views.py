from django.shortcuts import render

# Create your views here.

# Function for SignUp and SignIn.
def show_account(request):
    return render(request,'account.html')