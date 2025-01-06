// 12) Programa una función que determine si un número es primo (aquel que solo es divisible por sí mismo y 1) o no, pe. miFuncion(7) devolverá true.

const primeNumber = (num) => {
    if (num === 0 || num === 1 || num === 4) return false;
    for (let i = 2; i < num / 2; i++) {
        if (num % i === 0) return false;
    }
    return true;
};


console.log(primeNumber(7)); // true