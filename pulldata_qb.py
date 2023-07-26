import base_qb
import pandas as pd
from IPython.display import display


class Quickbook_customer():  
    def To_Json(self):
        self.data = []                                                 #creating empty list
        for customer in base_qb.customers:
            customer_vars=vars(customer)                               #vars converts object to dictionary basically object to JSON
            self.data.append(customer_vars)  
        
    def PrintData(self,Name):
        df = pd.DataFrame(self.data)       
        pd.set_option('display.max_columns', 50)                                
        df.to_csv(Name+'.csv',index = False)                           #dataframe to excel
        display(df) 


  
# from quickbooks.objects import account
# help(account) 



class Quickbook_account():  
    def To_Json(self):
        self.data = []                                              
        for account in base_qb.accounts:
            account_vars=vars(account)                             
            self.data.append(account_vars)  
        
    def PrintData(self,Name):
        df = pd.DataFrame(self.data)       
        pd.set_option('display.max_columns', 50)                                
        df.to_csv(Name+'.csv',index = False)                      
        display(df) 


class Quickbook_bill():  
    def To_Json(self):
        self.data = []                                                    
        for bill in base_qb.bills:
            bill_vars=vars(bill)                                     
            self.data.append(bill_vars)
        
    def PrintData(self,Name):
        df = pd.DataFrame(self.data)       
        pd.set_option('display.max_columns', 50)                                
        df.to_csv(Name+'.csv',index = False)                          
        display(df) 


class Quickbook_billpayment():  

    def To_Json(self):
        self.data = []                                                    
        for billpayment in base_qb.billpayments:
            billpayment_vars=vars(billpayment)                          
            self.data.append(billpayment_vars) 
        
    def PrintData(self,Name):
        df = pd.DataFrame(self.data)       
        pd.set_option('display.max_columns', 50)                                
        df.to_csv(Name+'.csv',index = False)                           
        display(df) 
                              


class Quickbook_deposit():  

    def To_Json(self):
        self.data = []                                                    
        for deposit in base_qb.deposits:
            deposit_vars=vars(deposit)                             
            self.data.append(deposit_vars)  
        
    def PrintData(self,Name):
        df = pd.DataFrame(self.data)       
        pd.set_option('display.max_columns', 50)                                
        df.to_csv(Name+'.csv',index = False)                        
        display(df) 
                                                   


class Quickbook_invoice():  

    def To_Json(self):
        self.data = []                                                    
        for invoice in base_qb.invoices:
            invoice_vars=vars(invoice)                              
            self.data.append(invoice_vars)  
        
    def PrintData(self,Name):
        df = pd.DataFrame(self.data)       
        pd.set_option('display.max_columns', 50)                                
        df.to_csv(Name+'.csv',index = False)                        
        display(df) 



class Quickbook_item():  

    def To_Json(self):
        self.data = []                                                    
        for item in base_qb.items:
            item_vars=vars(item)                                      
            self.data.append(item_vars)  
        
    def PrintData(self,Name):
        df = pd.DataFrame(self.data)       
        pd.set_option('display.max_columns', 50)                                
        df.to_csv(Name+'.csv',index = False)                            
        display(df) 



class Quickbook_journalentry():  

    def To_Json(self):
        self.data = []                                                    
        for journalentry in base_qb.journalentrys:
            journalentry_vars=vars(journalentry)                        
            self.data.append(journalentry_vars)  
        
    def PrintData(self,Name):
        df = pd.DataFrame(self.data)       
        pd.set_option('display.max_columns', 50)                                
        df.to_csv(Name+'.csv',index = False)                              
        display(df) 



class Quickbook_payment():  

    def To_Json(self):
        self.data = []                                                    
        for payment in base_qb.payments:
            payment_vars=vars(payment)                                    
            self.data.append(payment_vars)  
        
    def PrintData(self,Name):
        df = pd.DataFrame(self.data)       
        pd.set_option('display.max_columns', 50)                                
        df.to_csv(Name+'.csv',index = False)                        
        display(df) 



class Quickbook_purchase():  

    def To_Json(self):
        self.data = []                                                    
        for purchase in base_qb.purchases:
            purchase_vars=vars(purchase)                           
            self.data.append(purchase_vars)  
        
    def PrintData(self,Name):
        df = pd.DataFrame(self.data)       
        pd.set_option('display.max_columns', 50)                                
        df.to_csv(Name+'.csv',index = False)                             
        display(df) 



class Quickbook_term():  

    def To_Json(self):
        self.data = []                                                    
        for term in base_qb.terms:
            term_vars=vars(term)                                           
            self.data.append(term_vars)  
        
    def PrintData(self,Name):
        df = pd.DataFrame(self.data)       
        pd.set_option('display.max_columns', 50)                                
        df.to_csv(Name+'.csv',index = False)                            
        display(df) 
    


class Quickbook_timeactivity():  

    def To_Json(self):
        self.data = []                                                    
        for timeactivity in base_qb.timeactivitys:
            timeactivity_vars=vars(timeactivity)                          
            self.data.append(timeactivity_vars)  
        
    def PrintData(self,Name):
        df = pd.DataFrame(self.data)       
        pd.set_option('display.max_columns', 50)                                
        df.to_csv(Name+'.csv',index = False)                               
        display(df) 
   


class Quickbook_vendor():  

    def To_Json(self):
        self.data = []                                                    
        for vendor in base_qb.vendors:
            vendor_vars=vars(vendor)                                       
            self.data.append(vendor_vars)  
        
    def PrintData(self,Name):
        df = pd.DataFrame(self.data)       
        pd.set_option('display.max_columns', 50)                                
        df.to_csv(Name+'.csv',index = False)                              
        display(df) 
