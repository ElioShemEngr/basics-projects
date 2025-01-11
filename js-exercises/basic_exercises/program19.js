// 19) Programa una función que valide que un texto sea un nombre válido, pe. miFuncion("Jonathan MirCha") devolverá verdadero.

const nameValid = (name = '') => {
    if (!name) return console.warn("No ingresaste una cadena de texto");

    if (typeof name !== "string")
      return console.error("El valor ingresado no es una cadena de texto");

    let expReg = /^[A-Za-zñÑ\s]+$/g.test(name);

    return (expReg)
    ? console.info(`"${name}", es un nombre valido`)
    : console.info(`"${name}", NO es un nombre valido`);
};

nameValid("Elio Solis Ñaupari");