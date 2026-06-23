#Variables

#Para que no nos confundamos y que python interprete
#correctamente el tipo de variable, es recomendable que el nombre de la variable sea descriptivo y que empiece con minúscula.

my_String_variable= 'My String variable'
print(my_String_variable)

my_int_variable= 10
print(my_int_variable) 

my_boolean_variable= True
print(my_boolean_variable)


#En el siguiente print se muestran todas las variables en una sola línea, separadas por comas.
#Así no nos vamos a confundir con el tipo de variable que es cada una.

print(my_String_variable, my_int_variable, my_boolean_variable)



#Con lo que vamos a hacer en el siguiente print es cambiar de tipo de variable, es decir, vamos a convertir la variable my_int_variable en un string
# para que se pueda concatenar con la variable my_String_variable.
my_int_str_variable= str(my_int_variable)
print(my_int_str_variable)
print((type(my_int_str_variable))) 
#Esto nos dirá que es un string

print(type(print('Experimentando con los print',my_boolean_variable)))


#Funciones del sistema 
print(len(my_int_str_variable)) #Esto nos dirá la cantidad de caracteres que tiene la variable my_String_variable

#Varibales en una sola línea
name, surname, age, alias= 'Fabian', 'Trujillo', 18, 'Rick'
print('Hola, soy', name, 'mi apellido es', surname, 'y tengo', age, 'de edad', 'me dicen', alias, 'Porque mi segundo nombre es Ricardo')

'Para hacerlo mejor es recomendable separar las variables y asiganrlas en líneas diferentes, para que sea más fácil de leer y entender el código.'


#Input de datos
#Para que el usuario pueda ingresar datos, se puede usar la función input().

first_name= input('Ingrese su primer nombre: ')
last_name= input('Ingrese su apellido: ')
age=input('Ingrese su edad: ')

print('Hola', first_name, last_name, 'tienes', age, 'años de edad')









