library(pracma)
library(MASS)
n = 5

a = zeros(n, m = n)

condition = 0
contador = 0
while (condition <= 1000){
  for (i in 0:n){
    for (j in 0:n){
      contador = contador + 1
      a[i, j] = sample(1:20, 1)
    }
  }
  condition = kappa(a, exact = TRUE)
}
condition1 = 0
while (condition1 <= 1000){
  condition1 = 1/rcond(a)
}

print(condition1)

print("A: ")
print(a)
print(condition)

b = matrix(c(1, 2, 3, 4, 5), byrow = FALSE)
print("b")
print(b)

#Jacobi

A1 = matrix(c(8,9,2,2,7,2,2,8,6), 3, 3, byrow = TRUE)
b1 = matrix(c(69,47,68), byrow = FALSE)

diagonal = function(M){
  M[col(M)!=row(M)]= 0
  return(M)
}

#T= = -D^-1(L + U)
D = diagonal(A1)
#Matriz triangular inferior
L = Matrix::tril(A1, k = -1, diag = FALSE)
#Matriz triangular superior
U = Matrix::triu(A1, k=1, diag = FALSE)


T = (-solve(D))%*%(L+U)



print("T")
print(T)

print("Norma de T")
print(norm(T, "F"))

print(5/3)

