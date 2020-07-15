## Alex Parys
## C5 Activity 1 - Session 5.3
## 2/13/2019
## formatting strings

a = 10
b = "cookie"

print("The %s costs %d cents" % (b,a))

## %s - String, or any Python data object that can be converted to a string by using the str function.
## %d or %i - Integer or long integer

# The + Number or - number add spaces in the string

myStr = "The %+15s costs %4.1d cents" % (b,a)

print(myStr)

## the use of the floating point caused the output to be displayed as a decimal number
myStr = "The %+15s costs %6.1f cents" % (b,a)
print(myStr)


## way to prefill the values making it easy to read
myDict = { 'name':'gold', 'cost':10, 'price':15}

print("The %(name)s costs %(price)5.1f cents" % myDict)
