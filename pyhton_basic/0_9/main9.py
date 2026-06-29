#format specifiers = {value:format_specifier} 


price = 3.1415
price2 = -987.56
price3 = 12.34


print(f"price is ${price:.2f}") #price is $3.14
print(f"price2 is ${price2:+,.1f}") #price2 is $-987.6
print(f"price3 is ${price3:-,.3f}") #price3 is $12.340