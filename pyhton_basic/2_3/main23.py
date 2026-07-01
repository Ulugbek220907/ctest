#exception handling
# so many types errors exist but included only: ZeroDivisionError, TypeError

try:
    number = int(input("Enter a nnumber: "))
    result = 1/number
except ZeroDivisionError:
    print("You cannot enter 0!")
except TypeError:
    print("Only numbers!")
except ValueError:
    print("Only numbers!")
finally:
    print("Some sort of clean up")


