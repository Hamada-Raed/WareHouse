from django.db import models
import re 

class UserManager(models.Manager):
    def regValidator(self, postData):
        errors = {}
        #input validations
        if len(postData['f_name']) < 2:
            errors['f_name'] = "First Name should at least be 2 charecters"
        if len(postData['l_name']) < 2:
            errors['l_name'] = "Last Name should at least be 2 charecters"
        if len(postData['s_name']) < 2:
            errors['s_name'] = "Store Name should at least be 2 charecters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        if User.objects.filter(email=postData['email']).exists():
            errors['email'] = "This email is already registered!"
        if len(postData['password'] or postData['password_conf']) < 8:
            errors['password_len'] = "Password should at least be 8 charecters"
        if postData['password'] != postData['password_conf']:
            errors['password_match'] = "Passwords do not match"
        return errors 

    def loginValidator(self, postData):
        errors = {}  
        if not (User.objects.filter(email=postData['email']) and User.objects.filter(password=postData['password'])):
            errors['login'] = "Login failed! Check email and password"

        return errors

    def editValidator(self, postData):
        errors = {}
        #input validations
        if len(postData['f_name']) < 2:
            errors['f_name'] = "First Name should at least be 2 charecters"
        if len(postData['l_name']) < 2:
            errors['l_name'] = "Last Name should at least be 2 charecters"
        if len(postData['s_name']) < 2:
            errors['s_name'] = "Store Name should at least be 2 charecters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address!"
        return errors

class User(models.Model):
    f_name = models.CharField(max_length=255)
    l_name = models.CharField(max_length=255)
    s_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager() 

class ProdcutManager(models.Manager): 
    def ProductValidator(self, postData):
        errors = {}
        if len(postData['p_name']) < 0:
            errors['p_name'] = "Prodcut Name should at least be 2 charecters"
        if postData['qty'] < 0: 
            errors['qty'] = "Quantity can not be negative"
        return errors
    
    def order_list_validation(self,data):
        errors = {}
        check = Prodcut.objects.filter(p_name = data['p_name'])
        if check[0] == None :
            errors['p_name'] = "The product name you entered dose not exists"
        return errors
    
class Prodcut(models.Model): 
    p_name = models.CharField(max_length=255)
    date = models.DateTimeField()
    qty = models.IntegerField()
    weight = models.ImageField()
    total_weight = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #orders_list

class Order(models.Model): 
    p_name = models.FloatField()
    qty_sell = models.IntegerField()
    products = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User,related_name='orders',on_delete=models.CASCADE)

    @property
    def totalValue(self):
        return self.p_price * self.qty_sell
    
    def __str__(self):
        return f"Order: {self.id} - Total Value: {self.totalValue}"
        

class Order_list(models.Model): 
    p_name = models.FloatField()
    qty_sell = models.IntegerField()
    products = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ProdcutManager()