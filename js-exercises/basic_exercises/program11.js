// 11) Programa una función que calcule el factorial de un número (El factorial de un entero positivo n, se define como el producto de todos los números enteros positivos desde 1 hasta n), pe. miFuncion(5) devolverá 120.

function miFuncion(n) {
    if (n < 0) {
        return "El factorial no está definido para números negativos.";
    }

    let factorial = 1; // Inicializamos el resultado
    for (let i = 1; i <= n; i++) {
        factorial *= i; // Multiplicamos por cada número del rango
    }
    return factorial;
}

console.log(miFuncion(5)); // Salida: 120
