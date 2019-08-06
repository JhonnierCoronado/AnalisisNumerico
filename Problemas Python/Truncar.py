import math
x = 536.78
truncado = float(int(x*100) / 10) / 10
error = x -truncado
error = math.fabs(error)

print("El error es ")
print(error);
