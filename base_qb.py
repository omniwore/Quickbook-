import requests
import json
from intuitlib.client import AuthClient
from quickbooks import QuickBooks
from quickbooks.objects.customer import Customer
from quickbooks.objects.account import Account
from quickbooks.objects.bill import Bill
from quickbooks.objects.billpayment import BillPayment
from quickbooks.objects.deposit import Deposit
from quickbooks.objects.invoice import Invoice
from quickbooks.objects.item import Item
from quickbooks.objects.journalentry import JournalEntry
from quickbooks.objects.payment import Payment
from quickbooks.objects.purchase import Purchase
from quickbooks.objects.term import Term
from quickbooks.objects.timeactivity import TimeActivity
from quickbooks.objects.vendor import Vendor


# Accessing the API
# Set up an AuthClient passing in your CLIENT_ID and CLIENT_SECRET.

auth_client = AuthClient(
        client_id='AB0NiS9vr3NCIo4IAttD3HHow6MH9GuP3rmToh0MmyGRltNJhS',  # enter your id
        client_secret='RbJhUBA4hpeGq39vtZPLEerSShkYrzDVCHeZ7qnE',        # enter your secret
        access_token='****************************************************',      #enter access token
        environment='sandbox',                                                            
        redirect_uri='http://localhost:8000/callback',
    )

# Then create a QuickBooks client object passing in the AuthClient, refresh token, and company id

from quickbooks import QuickBooks

client = QuickBooks(
        auth_client=auth_client,
        refresh_token='AB11662899571G87y8twl6HWiEAT9CH1KzpcSeaV09rwAJlv8Q',          #enter refresh_token
        company_id='4620816365218690430',                                           #enter compnay_id
        minorversion=59
    )
        

# Get List of objects(API endpoints)

customers = Customer.all(qb=client)
accounts = Account.all(qb=client) 
bills = Bill.all(qb=client) 
billpayments = BillPayment.all(qb=client) 
deposits = Deposit.all(qb=client) 
invoices = Invoice.all(qb=client) 
items = Item.all(qb=client) 
journalentrys = JournalEntry.all(qb=client) 
payments = Payment.all(qb=client) 
purchases = Purchase.all(qb=client) 
terms = Term.all(qb=client) 
timeactivitys = TimeActivity.all(qb=client) 
vendors = Vendor.all(qb=client) 







