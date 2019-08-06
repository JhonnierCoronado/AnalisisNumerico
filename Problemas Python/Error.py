v = 4
Ev = 0.1
t = 5
Et = 0.1

mayorError = (v + Ev) * (t + Et)
print("El valor máximo que puede dar es ", mayorError)

minimoError = (v - Ev) * (t - Et)
print("El valor minimo que puede da es ", minimoError)

promedioError = (mayorError + minimoError) / 2
print("Valor: ", promedioError)

error = mayorError - promedioError
print("El error es +-", error)

print("Error absoluto ", promedioError - v * t)
print("Error relativo ", (promedioError - v * t) / promedioError)