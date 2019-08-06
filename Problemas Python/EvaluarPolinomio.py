#Despues de buscar, se decidió usar el Método de Horner, el cual la profesora ya habia mencionado

def polinomio(x):
        coeficientes=[-4, 3, -3, 0, 2]
        resultado = 0 
        for i in reversed(range(len(coeficientes))):
                resultado = coeficientes[i] + resultado * x
        return resultado
print(polinomio(-2))