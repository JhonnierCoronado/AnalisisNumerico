
Fx = function(x) {3.5*(x^2) + 6.8*x - 8}
#Primera Derivada
F1x = function(x) {7*x + 6.8}
#Segunda Derivada
F2x = function(x) {7}


Newton_Raphson =  function(x0, tol){
  it = 0
  error = 0
  xi = x0
  xz = 0
  repeat{
    cat("Iteracion: ", it, "\tXi: ", xi,"\tError: ", error, "\n")
    xz = xi - ((Fx(xi) * F1x(xi)) / (F1x(xi)^2 - Fx(xi)*F2x(xi)))
    error = abs((xz - xi))
    xi = xz
    it = it + 1
    if (error < tol){
      break
    }
  }
}
Newton_Raphson(1, 10e-18)

Newton = function(x, tol) {
  it = 0
  error = 0
  repeat {
    cat("Iteracion: ", it, "\tXi: ", x,"\tError: ", error, "\n")
    x=x-Fx(x)/F1x(x)
    error=abs(Fx(x)/F1x(x))
    it = it + 1
    if (error < tol){
      break
    }
  }
}
Newton(1, 10e-18)