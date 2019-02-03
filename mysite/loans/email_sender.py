import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email_Sender():

    def __init__(self,receiver_email,receiver_name,loan,payment_info):
        self.receiver_email = receiver_email
        self.loan = loan
        self.payment_info = payment_info
        self.receiver_name = receiver_name
        self.email_id = ""
        self.password = ""
        """
        User can save down email and password as a txt file in mysite/email.txt
        Or you can input the user and email above and comment out the short snipet below.
        """
        self.email_id, self.password = self.import_login_credentials()
        self.send_email(self.loan,self.payment_info, self.receiver_email, self.email_id,self.password)
    
    def import_login_credentials(self):
        with open("mysite/email.txt","r") as my_file:
            email_id = my_file.readline()
            password = my_file.readline()
        return email_id, password

    def send_email(loan,payment_info,receiver_email,receiver_name,email_id,password):
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls() #Encrypt login information
        mail.login(email_id, password)
        send_to = email_out
        
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

