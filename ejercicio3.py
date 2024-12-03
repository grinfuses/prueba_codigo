# Creamos el diccionario inicial
diccionario = {
    "usuario": "qa_tester",
    "habilidades": ["Selenium", "Appium", "Requests"]
}

# Primera parte, se añade una nueva clave 'experiencia' con el valor '3 años' al diccionario
diccionario["experiencia"] = "3 años"

# Se recorre el diccionario imprimiendo las claves y valores
for clave, valor in diccionario.items():
    print(f"Clave: {clave}, Valor: {valor}")