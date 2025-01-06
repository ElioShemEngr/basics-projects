// 15) Programa una función para convertir números de base binaria a decimal y viceversa, pe. miFuncion(100,2) devolverá 4 base 10.

const convertBase = (number, base) => {
    if (typeof number !== 'number' || typeof base !== 'number') return console.error('Debes ingresar un número');
    if (base === 2) return console.info(`El número ${number} base ${base} es igual a ${parseInt(number, base)} base 10`);
    if (base === 10) return console.info(`El número ${number} base ${base} es igual a ${number.toString(2)} base 2`);
    return console.warn('El tipo de base a convertir no es válido');
};

convertBase(100, 2);