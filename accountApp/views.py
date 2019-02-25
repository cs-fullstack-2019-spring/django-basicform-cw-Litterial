from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Account

# Create your views here.
def index(request):

    return render(request,"accountApp/index.html",) #Goes to the the index in templates

def welcome(request):
    accountOwner=(request.POST['accountOwner']) #defines this name they entered as a variable
    allAccounts=Account.objects.all()
    context={                        #object to hold all the informatioin I want to carry
        'allAccounts':allAccounts,
        'accountOwner':accountOwner,
    }
    return render(request,'accountApp/accounts.html',context) #Hey go to the accounts page in templates. Also carry this information too

def add5ToAccount(request,accountID):
    accountUser = get_object_or_404(Account, pk=accountID) #Will error in case of an invalid id
    accountUser.checking += 5   #adds 5 to checking
    accountUser.savings += 5    #adds 5 to savings
    accountUser.save()      #saves input
    return redirect("index")   #Hey man Go back to the index to enter a name again.

