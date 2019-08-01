
polinomio = function(x){
  coeficientes <- c(2, 0, -3, 3, 4)
  resultado = 0
  for (i in 0:length(coeficientes)) {
    resultado = resultado * x + coeficientes[i]
    }
  return(resultado)
}
result = polinomio(-2)
cat("La función da: ", result)