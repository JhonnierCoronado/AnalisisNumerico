rm(list=ls())

calculo = function(v, Ev, t, Et){
  errorMaximo = (v + Ev) * (t + Et)
  errorMinimo = (v - Ev) * (t - Et)
  
  resultado = (errorMaximo + errorMinimo) / 2
  error = errorMaximo - resultado
  errorAbs = resultado - v * t
  errorRel = errorAbs / resultado
  
  cat("Valor maximo: ", errorMaximo, "\nValor minimo: ", errorMinimo, "\n")
  cat("El valor es: ", resultado, "\n")
  cat("El error es: ", error, "\nError relativo: ", errorRel, "\nError absoluto: ", errorAbs)
}

calculo(4, 0.1, 5, 0.1)