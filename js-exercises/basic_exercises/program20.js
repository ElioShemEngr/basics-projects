// 20) Programa una función que valide que un texto sea un email válido, pe. miFuncion("jonmircha@gmail.com") devolverá verdadero.

const emailValid = (email = '') => {
    if (!email) return console.warn("No ingresaste una cadena de texto");

    if (typeof email !== "string")
      return console.error("El valor ingresado no es una cadena de texto");

    let expReg = /^[-\w.%+]{1,64}@(?:[A-Z0-9-]{1,63}\.){1,125}[A-Z]{2,63}$/i.test(email);

    // /^(([^<>()[\]\.,;:\s@\"]+(\.[^<>()[\]\.,;:\s@\"]+)*)|(\".+\"))@(([^<>()[\]\.,;:\s@\"]+\.)+[^<>()[\]\.,;:\s@\"]{2,})$/i.test(email);

    return (expReg)
    ? console.info(`"${email}", es un email valido`)
    : console.info(`"${email}", NO es un email valido`);
};

emailValid("ejem**/pló.ema_il@gmail.com");


