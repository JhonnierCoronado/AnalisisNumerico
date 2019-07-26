import math
x = 2.1234567
truncado = float(int(x*1000)) / 1000
error = x -truncado
error = math.fabs(error)

print("El error es ")
print(error);
