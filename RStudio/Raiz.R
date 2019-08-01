rm(list=ls())

Raiz = function(n, E, x, y)
{
  while (abs(x -y) > E) {
    y = (x + n/x) * 1/2
    x = y
  }
  return (y)
}
resultado = Raiz(7, 10e-10, 2, 0)
cat("El resultado de la raiz es: ", resultado, "\n")