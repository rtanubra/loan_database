from django.shortcuts import render,redirect,get_object_or_404

from .models import Loan
from .forms import LoanAddForm, LoanEmailForm

from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    View
)
#email stuff
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#===================Helper Function for emailing===================#
class EmailSender():

    def import_login_credentials(self):
        with open('loans/email.txt','r') as my_file:
            email_id= my_file.readline()
            password = my_file.readline()
        return email_id, password

    def send_email(self, loan,payment_info,receiver_email,receiver_name,email_id,password):
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls() #Encrypt login information
        mail.login(email_id, password)
        send_to = receiver_email
        
        message_body = f"""
        Dear {receiver_name},
        
        Here is the current information on loan {loan.loan_name}.
        The current loan principal is {loan.loan_principal}.
        The last action date was {loan.loan_last_action_date}.
        On {loan.loan_last_action_date} a payment of {payment_info.payment_amount} was made.

        Breakdown as follows
        Pre payment Principal: {payment_info.payment_pre_principal}
        Payment: {payment_info.payment_amount}
        Interest Paid: {payment_info.payment_interest_paid}
        Principal paid: {payment_info.payment_principal_paid}
        Post payment Principal: {payment_info.payment_post_principal}
        Interest Per day during this period: {payment_info.payment_ipd}

        Thank you,
        """

        #Start multimessage
        message = MIMEMultipart()

        #params: From, To Subject
        message["From"] = email_id
        message["To"] = receiver_email
        message["Subject"] = f"{loan.loan_name} on {loan.loan_last_action_date}"

        #Params Body
        message.attach(MIMEText(message_body,"plain"))

        mail.sendmail(email_id, receiver_email,message.as_string())
        mail.close()

# Create your views here.
class LoanListView(ListView):
    template_name = "loans/loan_list.html"
    queryset = Loan.objects.all()

class LoanCreateView(CreateView):
    template_name = 'loans/loan_create.html'
    form_class = LoanAddForm

class LoanEmailView(EmailSender,View):
    template_name = 'loans/loan_email.html'
    def post(self,request,*args,**kwargs):
        form = LoanEmailForm(request.POST)
        if form.is_valid():
            self.email_id , self.password = self.import_login_credentials()
            loan_id = self.kwargs.get("loan_id")
            loan = get_object_or_404(Loan, id=loan_id)
            payment_info_list = loan.paymenttracker_set.all()
            payment_info = payment_info_list[len(payment_info_list)-1]
            
            #email out
            self.send_email(
                loan,payment_info,
                form.cleaned_data["email"],
                form.cleaned_data["name"],
                self.email_id,
                self.password
            )

        form = LoanEmailForm()
        context ={
            'form':form,
            'loan':loan
        }
        return render(request,'loans/loan_email.html',context)
        
    def get(self,request,*args,**kwargs):
        form = LoanEmailForm()
        loan_id = self.kwargs.get("loan_id")
        loan = get_object_or_404(Loan, id=loan_id)
        context ={
            'form':form,
            'loan':loan
        }
        return render(request,'loans/loan_email.html',context)
