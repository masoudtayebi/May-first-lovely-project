from jinja2.sandbox import safe_range

while True:
     username = input()
     password = input()
#استفاده کردن از 2 مساوی در قسمت پایین به دلیل ایجاد بررسی میباشد ما 
#میخواهیم با استفاده از دو مساوی بررسی کنیم ک  ایا یوسر سجاد میباشد یا خیر 


     if username == "masoud" and password == "006600":
        print("you have successfully logged in! ")
        break
     elif username  != "masoud":
        print("username is incorrect!")

     elif password  != "006600":
        print("password is incorrect!")
     else:
         print("something went wrong!")