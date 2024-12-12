#کتاب خانه رندوم
import  random
# عددی رندوم بین اعداد گفته شده توسط کامپیوتر ایجاد میشود
computer_number  = random.randint(0, 100)
while True:
    #کاربر مقدار زیر را وارد میکند
    user_number = int(input())
    #اگر
    if  user_number == computer_number:
        print("ایول باریکلا")
        break
    #در صورتی ک
    elif user_number < computer_number:
        print("بورو بالاااا")
  #و در غیر این
    else:
        print("بورو پاییین")


#برنامه ای بنویسید ک در ان عددی مجهول توسط کامپیوتر ایجاد شود وکاربر آن عدد را حدس بزند
#و با استفاده از حلقه wile true  حلقه ای ایجاد کنید تا کاربر قبل از
#پیروزی در ان متوقف نشود
#