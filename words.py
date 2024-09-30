def inverter_string(string):
    invertida = ""
    
    # Percorre a string de trás para frente
    for i in range(len(string) -1, -1, -1):
        invertida += string[i]
    return invertida

txt = input("Digite uma string para inverter: ")

print(f'String Invertida: {inverter_string(txt)}')