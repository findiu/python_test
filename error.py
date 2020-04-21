try:
    age=int(input("age: "))
    income=10000
    risk=income/age
    print(age)
except ZeroDivisionError:
    print("age不能为0")
except ValueError:
    print("age只能为数字")