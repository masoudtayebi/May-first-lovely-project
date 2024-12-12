import math
while True:
    #ورودی های اینت مقدار های عددی
    #input
    a = int(input())
    b = int(input())
    # هدف کاربر را مشخص کن
    operator = input()

    # پردازش
    # process
    #اپراتور > در صورتی ک مشاهده کردی کاربر از دکمه + استفاده کرده
    #متغیر آ و ب را با هم جم کن
    if operator == "+":
        result = a + b
        #در صورتی که
    elif operator =="-":
        result = a - b
    elif operator =="*":
        result = a * b
    elif operator =="/":
        if b != 0:
             result = a / b
        else:
            result = "canat divide by ze"
            #محسابه مقدار توان
    elif operator =="^":
        #در این قسمت از دو ضرب استفاده کردیم و این به این معنا میباشد که
        #در حال استفاده کردین از توان هستیم  یعنی مقدار آ به توان ب

        #result = a ** b

        result = math.pow(a, b)
    elif operator == "kmm":
        result = math.lcm(a, b)
    elif operator == "exit":
        break
    else:
        result = "this operator not supported"
    # خروجی
    #output
    print(result)

    #برنامه ماشین حسابی بنویسید ک در ان عملیات + - % * انجام شود
    #و کلمه ای را برای بستن برنامه و عملیات توقف ان انجام بدهید