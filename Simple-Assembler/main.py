valid = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','_','0','1','2','3','4','5','6','7','8','9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def binary(n):
    n = int(n)
    s = bin(n)
    ans = s[2:]
    i = 8-len(ans)
    return '0'*i + ans

def isalpha(arr):
    for i in arr:
        if not( i.isalnum() or i == '_'):
            return False

    return True

def var_type(list1,startaddress):
    idx = list1.index('var')
    c = 1
    if idx + 1 == len(list1) - 1:
        for k in range(len(list1[idx+1])):
            if list1[idx+1][k] in valid:
                c = 1
            else:
                c = 0
                break
    else:
        return 'False'
    if c==0:
        return 'False'
    else:
        variable[list1[idx+1]] = binary(int(startaddress))
        return 'True'

def TypeA(array):

    n = 0
    #add
    if("add" in array):
        for i in array:
            if(i == "add"):
                break
            n += 1  
        ans = "0000000"

        if(n+1 < len(array) and n+2 < len(array) and n+3 <len(array)): # =checking further indices of n
            for i in registers.keys():
                if(i == array[n+1]):
                    ans += registers[i]
            if(len(ans) != 10):
                # print("Typo Error")
                return "-2"
            for i in registers.keys():
                if(i == array[n+2]):
                    ans += registers[i]
            if (len(ans) != 13):
                # print("Typo Error")
                return "-2"
            for i in registers.keys():
                if(i == array[n+3]):
                    ans += registers[i]
            if (len(ans) != 16):
                #print("Typo Error")
                return "-2"
        else:
            return "-1"
        return ans
    #sub
    elif ("sub" in array):
        for i in array:
            if (i == "sub"):
                break
            n += 1
        ans = "0000100"
        if (n + 1 < len(array) and n + 2 < len(array) and n + 3 < len(array)):
            for i in registers.keys():
                if (i == array[n + 1]):
                    ans += registers[i]
            if (len(ans) != 10):
                # print("Typo Error")
                return "-2"
            for i in registers.keys():
                if (i == array[n + 2]):
                    ans += registers[i]
            if (len(ans) != 13):
                # print("Typo Error")
                return "-2"
            for i in registers.keys():
                if (i == array[n + 3]):
                    ans += registers[i]
            if (len(ans) != 16):
                # print("Typo Error")
                return "-2"
        else:
            return "-1"
        return ans
    #mul
    elif ("mul" in array):
        for i in array:
            if (i == "mul"):
                break
            n += 1
        ans = "0011000"
        if (n + 1 < len(array) and n + 2 < len(array) and n + 3 < len(array)):
            for i in registers.keys():
                if (i == array[n + 1]):
                    ans += registers[i]
            if (len(ans) != 10):
                # print("Typo Error")
                return "-2"
            for i in registers.keys():
                if (i == array[n + 2]):
                    ans += registers[i]
            if (len(ans) != 13):
                # print("Typo Error")
                return "-2"
            for i in registers.keys():
                if (i == array[n + 3]):
                    ans += registers[i]
            if (len(ans) != 16):
                # print("Typo Error")
                return "-2"
        else:
            return "-1"
        return ans
    #xor
    elif ("xor" in array):
        for i in array:
            if (i == "xor"):
                break
            n += 1
        ans = "0101000"
        if (n + 1 < len(array) and n + 2 < len(array) and n + 3 < len(array)):
            for i in registers.keys():
                if (i == array[n + 1]):
                    ans += registers[i]
            if (len(ans) != 10):
                # print("Typo Error")
                return "-2"
            for i in registers.keys():
                if (i == array[n + 2]):
                    ans += registers[i]
            if (len(ans) != 13):
                # print("Typo Error")
                return "-2"
            for i in registers.keys():
                if (i == array[n + 3]):
                    ans += registers[i]
            if (len(ans) != 16):
                # print("Typo Error")
                return "-2"
        else:
            return "-1"
        return ans
    #or
    elif ("or" in array):
        for i in array:
            if (i == "or"):
                break
            n += 1
        ans = "0101100"
        if (n + 1 < len(array) and n + 2 < len(array) and n + 3 < len(array)):
            for i in registers.keys():
                if (i == array[n + 1]):
                    ans += registers[i]
            if (len(ans) != 10):
                # print("Typo Error")
                return "-2"
            for i in registers.keys():
                if (i == array[n + 2]):
                    ans += registers[i]
            if (len(ans) != 13):
                # print("Typo Error")
                return "-2"
            for i in registers.keys():
                if (i == array[n + 3]):
                    ans += registers[i]
            if (len(ans) != 16):
                # print("Typo Error")
                return "-2"
        else:
            return "-1"
        return ans
    #and
    elif ("and" in array):
        for i in array:
            if (i == "and"):
                break
            n += 1
        ans = "0110000"
        if (n + 1 < len(array) and n + 2 < len(array) and n + 3 < len(array)):
            for i in registers.keys():
                if (i == array[n + 1]):
                    ans += registers[i]
            if (len(ans) != 10):
                # print("Typo Error")
                return "-2"
            for i in registers.keys():
                if (i == array[n + 2]):
                    ans += registers[i]
            if (len(ans) != 13):
                return "-2"
            for i in registers.keys():
                if (i == array[n + 3]):
                    ans += registers[i]
            if (len(ans) != 16):
                # print("Typo Error")
                return "-2"
        else:
            return "-1"
        return ans
    else :
        # print("Typo Error")
        return "-1"

def TypeD(list1):
    if 'ld' in list1:
        idx = list1.index('ld')
        if idx + 2 == len(list1) - 1:
            if list1[idx+1] not in registers:
                return '-1'
            else:
                address = check1(list1[idx+2])
                if address=='False':
                    return '-2'
                else:
                    ans = '00100'
                    ans = ans + registers[list1[idx+1]]
                    ans = ans + str(address)
                    return ans
        else:
            return 'False'
    elif 'st' in list1:
        idx = list1.index('st')
        if idx + 2 == len(list1) - 1:
            if list1[idx+1] not in registers:
                return '-1'
            else:
                address = check1(list1[idx+2])
                if address=='False':
                    return '-2'
                else:
                    ans = '00101'
                    ans = ans + registers[list1[idx+1]]
                    ans = ans + address
                    return ans
        else:
            return 'False'

def check1(s):
    n1 = str(s)
    for k in variable.keys():
        if n1==k:
            return str(variable[k])
    return 'False'

def TypeE(array, Label_Dict, line_no):
    n = 0
    ans = ""

    if len(array) != 2:
        print("Syntax error at", line_no)
        return -1

    if array[1] not in Label_Dict:
        print("use of undefined label at", line_no)
        return -1
    
    if('jmp' in array):
        for i in array:
            if(i == 'jmp'):
                break
            n+=1
        ans = "01111000"
        if (n + 1 < len(array)):
            for i in Label_Dict:
                if(i == array[n+1]):
                    ans += Label_Dict[i]
            if(len(ans) != 16):
                print("use of undefined label at ")
                return '-1'
        else:
            print("semantics error at ")
            return '-1'

    elif('jlt' in array):
        for i in array:
            if(i == 'jlt'):
                break
            n+=1
        ans = "10000000"
        if (n + 1 < len(array)):
            for i in Label_Dict:
                if(i == array[n+1]):
                    ans += Label_Dict[i]
            if(len(ans) != 16):
                print("use of undefined label at ")
                return '-1'
        else:
            print("semantics error at ")
            return '-1'
    elif ('jgt' in array):
        for i in array:
            if (i == 'jgt'):
                break
            n += 1
        ans = "10001000"
        if (n + 1 < len(array)):
            for i in Label_Dict:
                if (i == array[n + 1]):
                    ans += Label_Dict[i]
            if (len(ans) != 16):
                print("use of undefined label at ")
                return '-1'
        else:
            print("semantics error at ")
            return '-1'
    elif ('je' in array):
        for i in array:
            if (i == 'je'):
                break
            n += 1
        ans = "10010000"
        if (n + 1 < len(array)):
            for i in Label_Dict:
                if (i == array[n + 1]):
                    ans += Label_Dict[i]
            if (len(ans) != 16):
                print("use of undefined label at ")
                return '-1'
        else:
            print("semantics error at ")
            return '-1'
    else :
        print("semantics Error at ")
        return '-1'
    return ans
 

def TypeF(array):
    ans = "10011"

    if len(array) == 2:
        if array[0][-1] == ":" and  isalpha(array[0][:-1]) and array[1] == "hlt":
            return ans+ "0"*11
        else:
            return '-1'
    elif(len(array)==1 and array[0] == "hlt"):
        return ans+ "0"*11

    else:
        return '-1'

def TypeB(array):
    n = 0
    ans = '-1'
    # mov
    if ("mov" in array):
        for i in array:
            if (i == "mov"):
                break
            n += 1  
        ans = "00010"
        if (n + 1 < len(array) and n + 2 < len(array)):
            for i in registers.keys():
                if (i == array[n + 1]):
                    ans += registers[i]
            if (len(ans) != 8):
                # print("Syntax Error")
                return '-1'
            check = array[n + 2]
            immediate = list(array[n + 2])
            if (immediate[0] == '$'):
                imm_number = int(check[1:])
                if (imm_number <= 255 and imm_number >= 0):
                    # reg=imm_number
                    answer = binary(imm_number)
                    ans += answer
                else:
                    # print("Illegal immediate value")
                    return '-2'
            else:
                return '-1'
            if (len(ans) != 16):
                # print("Syntax Error")
                return '-3'
        else:
            # print("General Syntax Error at line number") # needs to be written
            return '-3'
        return ans

    elif("rs" in array):
        # rightshift
        for i in array:
            if (i == "rs"):
                break
            n += 1  # increment n otherwise
        ans = "01000"

        if (n + 1 < len(array) and n + 2 < len(array)):
            for i in registers.keys():
                if (i == array[n + 1]):
                    ans += registers[i]
            if (len(ans) != 8):
                # print("Typo Error")
                return '-1'
            check = array[n + 2]
            immediate = list(array[n + 2])
            if (immediate[0] == '$'):
                imm_number = int(check[1:])
                if (imm_number <= 255 and imm_number >= 0):
                    # reg=imm_number*(2^imm_number)
                    answer = binary(imm_number)
                    ans += answer
                else:
                    # print("Illegal immediate value")
                    return '-2'
            if (len(ans) != 16):
                # print("Typo Error")
                return '-3'
        else:
            # print("Syntax Error at line number ")
            return '-1'
        return ans
    elif("ls" in array):
        # leftshift
        for i in array:
            if (i == "ls"):
                break
            n += 1  
        ans = "01001"

        if (n + 1 < len(array) and n + 2 < len(array)):
            for i in registers.keys():
                if (i == array[n + 1]):
                    ans += registers[i]
            if (len(ans) != 8):
                # print("Typo Error")
                return '-1'
            check = array[n + 2]
            immediate = list(array[n + 2])
            if (immediate[0] == '$'):
                imm_number = int(check[1:])
                if (imm_number <= 255 and imm_number >= 0):
                    answer = binary(imm_number)
                    ans += answer
                else:
                    # print("Illegal immediate value")
                    return '-2'
            if (len(ans) != 16):
                # print("Typo Error")
                return '-3'
        else:
            # print("Syntax Error ")
            return '-1'
        return ans
    return ans

def TypeC(list1):
    if 'mov' in list1:
        n = ''
        n = n + '00011'
        n = n + '00000'
        index = list1.index('mov')
        if index + 2 == len(list1) - 1:
            if list1[index+1] not in registers or list1[index+2] not in registers:
                return '-1'
            else:
                n = n + registers[list1[index+1]] + registers[list1[index+2]]
                return n
        else:
            return 'False'
    elif 'div' in list1:
        n = ''
        n = n + '00111'
        n = n + '00000'
        index = list1.index('div')
        if index + 2 == len(list1) - 1:
            if list1[index+1] not in registers or list1[index+2] not in registers:
                return '-1'
            else:
                n = n + registers[list1[index+1]] + registers[list1[index+2]]
                return n
        else:
            return 'False'
    elif 'cmp' in list1:
        n = ''
        n = n + '01110'
        n = n + '00000'
        index = list1.index('cmp')
        if index + 2 == len(list1) - 1:
            if list1[index+1] not in registers or list1[index+2] not in registers:
                return '-1'
            else:
                n = n + registers[list1[index+1]] + registers[list1[index+2]]
                return n
        else:
            return 'False'
    elif 'not' in list1:
        n = ''
        n = n + '01101'
        n = n + '00000'
        index = list1.index('not')
        if index + 2 == len(list1) - 1:
            if list1[index+1] not in registers or list1[index+2] not in registers:
                return '-1'
            else:
                n = n + registers[list1[index+1]] + registers[list1[index+2]]
                return n
        else:
            return 'False'

#main
registers = {'R0':'000','R1':'001','R2':'010','R3':'011','R4':'100','R5':'101','R6':'110','FLAGS':'111'}
values = {'R0':0,'R1':0,'R2':0,'R3':0,'R4':0,'R5':0,'R6':0}

instructions = {}
machinecode=[]

var = []
key = 0
empty = 0
empty_instructions = {}
variable = {}
Label_Dict = {}
valid_instruction = 0
halt = False
error=True

while(True):
    try:
        line = input()
        #if line=='-1':
            #break
        instructions[key] = line
        key = key + 1

        if 'var' in line:
            var.append(line)

        List = line.strip().split()

        if(len(List) > 0 and List[0] == "hlt"):
            halt = True
        
        if(len(List) > 0 and ':' == List[0][-1]):
            if(len(List) == 2) and "hlt" == List[1]:
                halt = True

            if(List[0][0:-1] in Label_Dict):
                print(f"multiple times same label at {key}")

            else:
                Label_Dict[List[0][0:-1]] = binary(valid_instruction)

        if "var" not in List and len(List) > 0:
            valid_instruction+=1

        if len(line)==0:
            empty = empty + 1
    except EOFError:
        break
total_instructions = len(instructions) #starting from 0 to key - 1
startaddress = total_instructions - len(var) - empty
key = key - 1


if not halt:
    print("Missing hlt instruction")
    error=False
   
else:
    for k in instructions.keys():
        list1 = []
        list1 = instructions[k].split()

        if 'hlt' in list1:
            if(k  < key):
                print("error: hlt is not used as a last statement at", k+1)
                error=False
                break
            else:
                temp = TypeF(list1)
                if temp == "-1":
                    print("typo at line", k+1)
                    error=False
                    break
                else:
                    machinecode.append(temp)
                    # print(temp)
        elif instructions[k].count(':')>1:
            print('error: Invalid label instruction in line : ',k+1)
            error=False
            break
        elif 'var' in list1:
            if k!=0 and 'var' not in instructions[k-1]:
                print('error: variable declared in between the program at line: ',k+1)
                error=False
                break
            else:
                isvalid = var_type(list1,startaddress)
                if isvalid=='False':
                    print('Invalid var instruction at line:',k+1)
                    error=False
                    break
                else:
                    startaddress = startaddress + int(1)
        elif 'add' in list1 or 'sub' in list1 or 'mul' in list1 or 'xor' in list1 or 'or' in list1 or 'and' in list1:
            if("FLAGS" in list1):
                print("Illegal use of Flag resistor at line:",k+1)
                error = False
                break
            temp = TypeA(list1)
            if temp=='-1':
                print('Semantics Error in line:',k+1)
                error=False
                break
            elif temp == '-2':
                print('Typo Error in Register Value at line:',k+1)
                error = False
                break
            else:
                machinecode.append(temp)
                # print(temp)
        elif 'ld' in list1 or 'st' in list1:
            temp = TypeD(list1)
            if temp=='-1':
                print('error: Typo in register name at line:',k+1)
                error=False
                break
            elif temp=='-2':
                print('error: Variable not found at line: ', k+1)
                error = False
                break
            elif temp=='False':
                print('error: Invalid syntax of instruction at line: ',k+1)
                error = False
                break
            else:
                machinecode.append(temp)
                # print(temp)
        elif 'mov' in list1:
            idx = list1.index('mov')
            if idx+2 < len(list1) and '$' in list1[idx+2]:
                isvalid = TypeB(list1)

                if (isvalid == '-1'):
                    print("Syntax Error at line:", k + 1)
                    error = False
                    break
                elif (isvalid == '-2'):
                    print("Illegal use of immediate value at line:", k + 1)
                    error = False
                    break
                elif (isvalid == '-3'):
                    print("Semantics error at line:", k + 1)
                    error = False
                    break
                else:
                    machinecode.append(isvalid)
            else:
                isvalid = TypeC(list1)
                if isvalid=='-1':
                    print('error: Typo in register name at line: ',k+1)
                    error=False
                    break
                elif isvalid=='False':
                    print('error: Syntax error in instruction at line: ',k+1)
                    error=False
                    break
                else:
                    machinecode.append(isvalid)
            
        elif 'rs' in list1 or 'ls' in list1:
            isvalid = TypeB(list1)
            if(isvalid == '-1'):
                print("Syntax Error at line:" ,k+1)
                error = False
                break
            elif(isvalid == '-2'):
                print("Illegal use of immediate value at line:",k+1)
                error = False
                break
            elif(isvalid == '-3'):
                print("Semantics error at line:",k+1)
                error = False
                break
            else:
                machinecode.append(isvalid)

        elif 'div' in list1 or 'not' in list1 or 'cmp' in list1:
            isvalid = TypeC(list1)
            if isvalid=='-1':
                print('error: Typo in register name at line: ',k+1)
                error=False
                break
            elif isvalid=='False':
                print('error: Syntax error in instruction at line: ',k+1)
                error=False
                break
            else:
                machinecode.append(isvalid)
        
        elif 'jmp' in list1 or 'jlt' in list1 or 'jgt' in list1 or 'je' in list1:   
            temp = TypeE(list1, Label_Dict, k+1)
            if(temp != -1):
                machinecode.append(temp)
                # print(temp)
            else:
                #print('Error at line:',k+1)
                error=False
                break
        else:
            print('Invalid instruction in line : ',k+1)
            error=False
            break
if (error):
    for j in machinecode:
        print(j)