class CustomException(Exception):
    pass


x = 2
try:
    # print(y)
    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
    # raise Exception("Something went wrong.")
    raise CustomException("A custom exception.")
except NameError:
    print("NameError means something is probably undefined.")
except ZeroDivisionError:
    print("Please do not divide by zero.")
except Exception as error:  # catches all errors
    print(f"An error ocurred --> {error}")
else:  # if there is no error
    print("No errors!")
finally:  # no matter what, this block will be executed
    print("Done.")

# PS: else and finally cannot be added at the same time!
