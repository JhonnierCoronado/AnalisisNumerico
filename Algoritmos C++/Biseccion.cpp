#include <iostream>
#include <iomanip>
#include <math.h>

#define PRECISION 6
using namespace std;

void tabula(double, double, int); //Muestra en pantalla
double f(double);

int main(int argc, char const *argv[])
{
    int precision;
    cout << "Digite la precision que desea trabajar\n";
    cin >> precision;
    cout << setprecision(precision); //La precision con la que se trabajará

    double a, b, tol;
    float xr;
    int intervalos, contador = 0, opt;

    cout << "Biseccion\n";
    cout << "Intervalo [a, b]\n";

    cout << "a = ";
    cin >> a;

    cout << "b = ";
    cin >> b;

    cout << "Digite el numero de intervalos ";
    cin >> intervalos;

    tabula(a, b, intervalos);
do{
    cout << "Escoja un nuevo intervalo [a, b]\n";
    cout << "a = ";
    cin >> a;
    
    cout << "b = ";
    cin >> b;

    if (f(a) * f(b) > 0){
        cout << "No se puede aplicar el metodo\n";
    }
    else {
        cout << "Ingrese la tolerancia: ";
        cin >> tol;

        cout << "\na\tb\tx\tf(a)\t\tf(b)\t\tf(x)\n\n";
        do {
            xr = (a + b) / 2.0;
            cout << a << "\t\t" << b << "\t\t" << xr << "\t";
            cout << f(a) << "\t\t" << f(b) << "\t\t" << f(xr) << endl;
            if (fabs(f(xr)) <= tol){
                cout << "\n\nLa raiz de f es: " << xr << endl;
                cout << "Con " << contador << " interacciones\n";
                break;
            }
            else {
                if (f(xr) * f(a) > 0){
                    a = xr;
                }
                else if (f(xr) * f(b) > 0){
                    b = xr;
                }
            }
            contador ++ ;
        } while(true);
    }
    cout << "Desea continuar con otro intervalo? (0 = no)\n";
    cin >> opt;
} while(opt != 0);

    return 0;
}


void tabula(double a, double b, int intervalos){
    int puntos = intervalos + 1;
    double ancho = (b - a) / intervalos;

    cout << "\n\tx\t\tf(x) \n";
    for (size_t i = 0; i < puntos; i++){
        cout << "\t" << a << "\t\t" << f(a) << '\n';
        a += ancho;
    }
}

double f(double x){
    //Acá va la función, se usará para este caso 1 + sin(x) - sqrt(x)
    return 1 + sin(x) - sqrt(x);
}
