import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (10, 6)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

Register_Value = {'000':'0'*16,'001':'0'*16,'010':'0'*16,'011':'0'*16,'100':'0'*16,'101':'0'*16,'110':'0'*16,'111':'0'*16}

def decimalToBinary(n):
    s = bin(n)
    ans = s[2:]
    i = 16-len(ans)
    return '0'*i + ans

def binaryToDecimal(str):
    n = 1
    sum = 0
    for i in str[::-1]:
        sum = sum + int(i)*n
        n = n*2
    return sum

Mem_add = {}
s = 0
arr = []
while(True):
    try:
       line = input()
       if(len(line)>0):
           Mem_add[decimalToBinary(s)[8:]] = line
           arr.append(line)
           s = s+1
       #if line=='':
           #break
       ...
    except EOFError:
        break
i = 0
key = 0
cycle = {}
extra = {}
while(i<len(arr)): #i = PC
    cycle[key] = i
    if(arr[i][0:5] == '00000'):     #add
        str1 = Register_Value[arr[i][10:13]]
        str2 = Register_Value[arr[i][13:16]]
        str3 = decimalToBinary(i)
        n1 = binaryToDecimal(str1)
        n2 = binaryToDecimal(str2)
        n = n1+n2
        if(n>65535):
            Register_Value['111'] = '0'*12 + '1000'
            Register_Value[arr[i][7:10]] = decimalToBinary(n)[-16:]
        else:
            Register_Value[arr[i][7:10]] = decimalToBinary(n)
            Register_Value['111']='0'*16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
    elif(arr[i][0:5] == '00001'):     #subtract
        str1 = Register_Value[arr[i][10:13]]
        str2 = Register_Value[arr[i][13:16]]
        str3 = decimalToBinary(i)
        n1 = binaryToDecimal(str1)
        n2 = binaryToDecimal(str2)
        n = n1 - n2
        if(n<0):
            Register_Value['111'] = '0' * 12 + '1000'
            Register_Value[arr[i][7:10]] = '0'*16
        else:
            Register_Value[arr[i][7:10]] = decimalToBinary(n)
            Register_Value['111']='0'*16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
    elif(arr[i][0:5] == '00110'):     #multiply
        str1 = Register_Value[arr[i][10:13]]
        str2 = Register_Value[arr[i][13:16]]
        str3 = decimalToBinary(i)
        n1 = binaryToDecimal(str1)
        n2 = binaryToDecimal(str2)
        n = n1 * n2
        if(n>65535):
            Register_Value['111'] = '0' * 12 + '1000'
            Register_Value[arr[i][7:10]] = decimalToBinary(n)[-16:]
        else:
            Register_Value[arr[i][7:10]] = decimalToBinary(n)
            Register_Value['111']='0'*16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
    elif(arr[i][0:5] =='01010'):      #xor
        str1 = Register_Value[arr[i][10:13]]
        str2 = Register_Value[arr[i][13:16]]
        str3 = decimalToBinary(i)
        n1 = binaryToDecimal(str1)
        n2 = binaryToDecimal(str2)
        n = n1^n2
        Register_Value[arr[i][7:10]] = decimalToBinary(n)
        Register_Value['111'] = '0'*16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
    elif(arr[i][0:5] == '01011'):      #or
        str1 = Register_Value[arr[i][10:13]]
        str2 = Register_Value[arr[i][13:16]]
        str3 = decimalToBinary(i)
        n1 = binaryToDecimal(str1)
        n2 = binaryToDecimal(str2)
        n = n1 | n2
        Register_Value[arr[i][7:10]] = decimalToBinary(n)
        Register_Value['111'] = '0' * 16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
    elif(arr[i][0:5] == '01100'):      #and
        str1 = Register_Value[arr[i][10:13]]
        str2 = Register_Value[arr[i][13:16]]
        str3 = decimalToBinary(i)
        n1 = binaryToDecimal(str1)
        n2 = binaryToDecimal(str2)
        n = n1 & n2
        Register_Value[arr[i][7:10]] = decimalToBinary(n)
        Register_Value['111'] = '0' * 16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
    elif(arr[i][0:5]=='00010'):                #mov $imm
        imm_value=(arr[i][8:])
        n = binaryToDecimal(imm_value)
        str3 = decimalToBinary(i)
        Register_Value[arr[i][5:8]] =  decimalToBinary(n)
        Register_Value['111'] = '0' * 16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
    elif(arr[i][0:5] == '01000'):                #right shift
        str1 = Register_Value[arr[i][5:8]]
        imm_value=binaryToDecimal(arr[i][8:])
        str3 = decimalToBinary(i)
        n = binaryToDecimal(str1)/imm_value
        Register_Value[arr[i][5:8]]=decimalToBinary(n)
        Register_Value['111'] = '0' * 16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
    elif(arr[i][0:5] == '01001'):                #left shift
        str1= Register_Value[arr[i][5:8]]
        imm_value=binaryToDecimal(arr[i][8:])
        str3 = decimalToBinary(i)
        n=binaryToDecimal(str1)*imm_value
        Register_Value[arr[i][5:8]]=decimalToBinary(n)
        Register_Value['111'] = '0' * 16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
    elif(arr[i][0:5] == '00011'):                #Move Register
        str3 = decimalToBinary(i)
        Register_Value[arr[i][10:13]] = Register_Value[arr[i][13:]]
        Register_Value['111'] = '0' * 16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
    elif(arr[i][0:5] == '00111'):                #Div
        str1 = Register_Value[arr[i][10:13]]
        str2 = Register_Value[arr[i][13:]]
        str3 = decimalToBinary(i)
        n1 = binaryToDecimal(str1)
        n2 = binaryToDecimal(str2)
        n = n1/n2
        m = n1%n2
        Register_Value['000'] = decimalToBinary(n)
        Register_Value['001'] = decimalToBinary(m)
        Register_Value['111'] = '0' * 16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
    elif(arr[i][0:5] == '01110'):                #compare
        str1 = Register_Value[arr[i][10:13]]
        str2 = Register_Value[arr[i][13:]]
        str3 = decimalToBinary(i)
        n1 = binaryToDecimal(str1)
        n2 = binaryToDecimal(str2)
        if(n1 == n2):
            Register_Value['111'] = '0'*15 + '1'
        elif(n1<n2):
            Register_Value['111'] = '0'*13 + '100'
        elif(n1>n2):
            Register_Value['111'] = '0'*14 + '10'
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
    elif(arr[i][0:5] == '01101'):              #invert
        str1 = Register_Value[arr[i][13:]]
        n1 = binaryToDecimal(str1)
        str3 = decimalToBinary(i)
        n = ~n1
        Register_Value[arr[i][10:13]] = decimalToBinary(n)
        Register_Value['111'] = '0' * 16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
    elif(arr[i][0:5] == '00100'):             #load
        str1 = arr[i][8:]
        str3 = decimalToBinary(i)
        if (arr[i][8:] not in Mem_add):
            Mem_add[str1] = '0'*16
            s += 1
        Register_Value[arr[i][5:8]] = Mem_add[str1]
        Register_Value['111'] = '0' * 16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
        temp = binaryToDecimal(str1)
        extra[key] = temp
    elif(arr[i][0:5] == '00101'):              #store
        str1 = Register_Value[arr[i][5:8]]
        str3 = decimalToBinary(i)
        if(arr[i][8:] not in Mem_add):
            s += 1
        Mem_add[arr[i][8:]] = str1
        Register_Value['111'] = '0' * 16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
        temp = binaryToDecimal(arr[i][8:])
        extra[key] = temp
    elif(arr[i][0:5] == '01111'):             #jump
        n = binaryToDecimal(arr[i][8:])
        str3 = decimalToBinary(i)     
        extra[key] = i  
        key = key + 1                                                            
        i = n
        Register_Value['111'] = '0' * 16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
        continue
    elif(arr[i][0:5] == '10000' and binaryToDecimal(Register_Value['111'])==4):   #lessthanjmp
        n = binaryToDecimal(arr[i][8:])
        str3 = decimalToBinary(i)
        extra[key] = i
        key = key + 1
        i = n
        Register_Value['111'] = '0' * 16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
        continue
    elif (arr[i][0:5] == '10001' and binaryToDecimal(Register_Value['111']) == 2):  #greaterthanjmp
        n = binaryToDecimal(arr[i][8:])
        str3 = decimalToBinary(i)
        extra[key] = i
        key = key + 1
        i = n
        Register_Value['111'] = '0' * 16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])

        continue
    elif (arr[i][0:5] == '10010' and binaryToDecimal(Register_Value['111']) == 1):    #equaljmp
        n = binaryToDecimal(arr[i][8:])
        str3 = decimalToBinary(i)
        extra[key] = i
        key = key + 1
        i = n
        Register_Value['111'] = '0' * 16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
              Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
                  '110'] + " " + Register_Value['111'])
        continue
    else:
        str3 = decimalToBinary(i)
        Register_Value['111'] = '0' * 16
        print(str3[8:] + " " + Register_Value['000'] + " " + Register_Value['001'] + " " + Register_Value['010'] + " " +
          Register_Value['011'] + " " + Register_Value['100'] + " " + Register_Value['101'] + " " + Register_Value[
              '110'] + " " + Register_Value['111'])
        extra[key] = i
    key = key + 1
    i+=1
for i in Mem_add:
    print(Mem_add[i])
for i in range(s,256):  
    print('0'*16)
#colors = list("rgbcmyk")
#print(cycle)
#print(extra)
for j in cycle.keys():
    x = j
    y = cycle[j]
    plt.scatter(x,y,color='b')
    if x in extra.keys():
        y1 = extra[x]
        plt.scatter(x,y1,color='b')
#plt.legend(cycle.keys())
plt.title('Memory Accesses vs Cycle')
plt.xlabel('Cycle')
plt.ylabel('Memory Accesses')
plt.show()