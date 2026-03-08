#hex codes missing leading zeros

#https://colorwikia.com/blog/how-hex-color-codes-work/

#--output missing 0s if value needs only one value-space
# (too condensed 3 digit hex-codes imply there are doubles
#of that value ie a would be aa -- ABC => AABBCC so while at times
#the leading nums can be condensed other times it causes
# the hex-code to be incorrect)

#https://docs.python.org/3/library/stdtypes.html#float.fromhex 

#https://python-reference.readthedocs.io/en/latest/docs/float/hex.html
#using hex() returns a string of the number as its floating int equivelent--> returns string type specifically so may not
#be what is causing this error

#or that typically hex is used to store compressed binary so what might be returned is the value as is
#and not the appropoiate format for the hex version of RGB values 
#(in other words the nost condenced version of the nums are returned so the bug may be in the 
#formatting of the three values in hex in order while not being a single value as the default might be)

#Using the prefix 0x cann allow for literal values to be stored in hex


#potential for the concatnation of the three values stored in the single variable


#length of output check (this implies a check for an appropriate amount of
#leading zeros

def proper_length(input, output):
    str_output = output.toString()
    if (str_output.length < 8):
        return False

 



