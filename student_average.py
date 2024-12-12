#نمرات
a = float(input())
b = float(input())
c = float(input())

avg = (a + b + c) / 3

print("average = ",avg)
# اگر معدل بالای این مقدار باشد پیام تبریک اجرا شود
#دستور داخل ایف باید حتما مقداری جلوتر باشد به مقدار تایین شده یا 4 اسپیس
if avg >= 17:
    print("congratulations :)")
elif avg < 12:
    print("try more :-(")
else:
    print("normal >=<")
    print("normal =",13,14,15,16) 