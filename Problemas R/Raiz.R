rm(list=ls())

Raiz = function(n, E, x, y)
{
  contador = 0
  while (abs(x -y) > E) {
    y = (x + n/x)
    y = y / 2
    x = y
    contador = contador + 1
  }
  return (c(y, contador))
}
resultado= Raiz(7, 0.1, 3, 0)
cat("El resultado de la raiz es: ", resultado[1], "Con: ", resultado[2], "iteraccion \n")