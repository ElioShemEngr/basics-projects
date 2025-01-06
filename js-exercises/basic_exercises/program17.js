// 17) Programa una función que dada una fecha válida determine cuantos años han pasado hasta el día de hoy, pe. miFuncion(new Date(1984,4,23)) devolverá 40 años (en 2024).

const yearsPassed = (date = undefined) => {
  if (date === undefined) return console.warn("No ingresaste una fecha válida");

  if (!(date instanceof Date))
    return console.error("El valor que ingresaste no es una fecha válida");

  let now = new Date().getTime();
  let past = date.getTime();

  if (now < past)
    return console.error("La fecha no puede ser mayor a la actual");

  let years = now - past;
  let yearsInMs = 1000 * 60 * 60 * 24 * 365.25;

  return Math.floor(years / yearsInMs);
};

console.log(yearsPassed(new Date(1984, 4, 23))); // 40