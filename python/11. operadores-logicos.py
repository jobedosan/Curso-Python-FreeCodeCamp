#Operador and
#Ambas expresiones son True así que arroja True
print((5 < 6) and (10 > 6 ))

#Ambas expresiones son False así que arroja False
print((5 > 6) and (10 > 6 ))

#Una de las expresiones es False y la otra True, así que retorna False
print((5 > 6) and (10 > 6 ))
print((5 < 6) and (10 < 6 ))

#Operador or
#Ambas expresiones son True así que arroja True
print((5 < 6) or (10 > 6 ))

#Ambas expresiones son False así que arroja False
print((5 > 6) or (10 < 6 ))

#Una de las expresiones es False y la otra True, así que retorna True
print((5 > 6) or (10 > 6 ))
print((5 < 6) or (10 < 6 ))

#Operador not
#La expresión es False así que arroja True
print(not(5 > 6))
#La expresión es True así que arroja False
print(not(5 < 6))

