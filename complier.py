
# Read assembly code from input file
with open('1.txt', 'r') as file:
    assembly_code = file.readlines()

# Convert assembly code to machine code
machine_code = []
for instruction in assembly_code:
    instruction = instruction.strip()
    if instruction == 'CLEAR ALL':
        machine_code.append('101000000')
        machine_code.append('101001000')
        machine_code.append('101001001')
        machine_code.append('101001010')
        machine_code.append('101001011')
        machine_code.append('101001100')
        machine_code.append('101001101')
        machine_code.append('101001110')
        machine_code.append('101001111')
    elif  instruction.startswith('IMM'): 
        value = int(instruction.split('#')[1].strip())
        binary_value = bin(value)[2:].zfill(7)
        machine_code.append('11' + binary_value)
    elif instruction.startswith('AUTO'):
        machine_code.append('000000000')
    elif instruction.startswith('LBS'):
        machine_code.append('000001000')
    elif instruction.startswith('LLS'):
        if instruction.startswith('LLS SUPER'):
            machine_code.append('000010000')
        else:
            register = int(instruction.split()[1][1:])
            machine_code.append('000011' + bin(register)[2:].zfill(3))
    elif instruction.startswith('RLS'):
        if instruction.startswith('RLS SUPER'):
            machine_code.append('000100000')
        else:
            register = int(instruction.split('R')[2])
            machine_code.append('000101' + bin(register)[2:].zfill(3))
    elif instruction.startswith('AND'):
        if instruction.startswith('AND SUPER'):
            register = int(instruction.split('R')[2])
            machine_code.append('000110' + bin(register)[2:].zfill(3))
        else:
            register = int(instruction.split()[1][1:])
            machine_code.append('000111' + bin(register)[2:].zfill(3))

    elif instruction.startswith('OR'):
        if instruction.startswith('OR SUPER'):
            register = int(instruction.split('R')[3])
            machine_code.append('001000' + bin(register)[2:].zfill(3))
        else:
            register = int(instruction.split()[1][1:])
            machine_code.append('001001' + bin(register)[2:].zfill(3))
            
    elif instruction.startswith('XOR SUPER'):
            register = int(instruction.split('R')[3])
            machine_code.append('001010' + bin(register)[2:].zfill(3))
    elif instruction.startswith('IOR SUPER'):
            machine_code.append('001011000')
    elif instruction.startswith('IXOR SUPER'):           
            machine_code.append('001100000')
    elif instruction.startswith('CLEAR'):
            if instruction.startswith('CLEAR SUPER'):           
                machine_code.append('101000000')
            else:
                register = int(instruction.split('R')[2])
                machine_code.append('101001' + bin(register)[2:].zfill(3))
    elif instruction.startswith('SUB'):
            register = int(instruction.split()[1][1:])
            machine_code.append('001101' + bin(register)[2:].zfill(3))
    elif instruction.startswith('ADD'):
        if instruction.startswith('ADD SUPER'): 
            register = int(instruction.split('R')[2])  
            machine_code.append('001110' + bin(register)[2:].zfill(3))
        else:
            register = int(instruction.split()[1][1:])  
            machine_code.append('001111' + bin(register)[2:].zfill(3))
    elif instruction.startswith('LB'):
            registerx = int(instruction.split('R')[1])
            registery = int(instruction.split('R')[2])
            machine_code.append('010' + bin(registerx)[2:].zfill(3)+bin(registery)[2:].zfill(3))
    elif instruction.startswith('SB'):
            registerx = int(instruction.split()[1][1:])
            registery = int(instruction.split()[2][1:])
            machine_code.append('011' + bin(registerx)[2:].zfill(3)+bin(registery)[2:].zfill(3))
    elif instruction.startswith('BZ'):
           registerx = int(instruction.split('R')[1][1:])
           registery = int(instruction.split('R')[2][1:])
           machine_code.append('1000' + bin(registerx)[2:].zfill(2)+bin(registery)[2:].zfill(3))
    elif instruction.startswith('BNZ'):
            registerx = int(instruction.split('R')[1][1:])
            registery = int(instruction.split('R')[2][1:])
            machine_code.append('1001' + bin(registerx)[2:].zfill(2)+bin(registery)[2:].zfill(3))
    elif instruction.startswith('MOVE'):
        if instruction.startswith('MOVE SUPER'):
            register = int(instruction.split('R')[2])
            machine_code.append('101010' + bin(register)[2:].zfill(3))
        else:
            register = int(instruction.split()[1][1:])
            machine_code.append('101011' + bin(register)[2:].zfill(3))
                
                           
                   
    else:
        machine_code.append('Invalid instruction')

# Write machine code to output file
with open('2.txt', 'w') as file:
    file.write('\n'.join(machine_code))
