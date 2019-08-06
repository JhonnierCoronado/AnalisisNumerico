rm(list=ls())

fx = function(x){
  return (exp(x))
}

taylor = function(x,n){
  r = 0
  for (i in 0:n) {
    r = r + ((x^i)/factorial(i))
  }
  r = signif(r, 5)
  cat("El valor de la aproximación es: ", r, "\n")
}

x = 0.5
n = 10
taylor(x, n)
