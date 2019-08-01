rm(list=ls())

fx = function(x){
  return (exp(1)^x)
}

taylor = function(){
  a = 0
  r = fx(a)
  for (i in 0:100) r = r + (fx(a) / factorial(i)) * ((0.05-a))^i
  r = signif(r, 5)
  cat("El valor de la aproximación es: ", r, "\n")
}

taylor()
