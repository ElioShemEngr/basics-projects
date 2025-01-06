// 16) Programa una función que devuelva el monto final después de aplicar un descuento a una cantidad dada, pe. miFuncion(1000, 20) devolverá 800.

const applyDiscount = (amount = undefined, discount = 0) => {
  if (amount === undefined) return console.warn("No ingresaste el monto");
  if (typeof amount !== "number")
    return console.error(`El valor ${amount} ingresado, NO es un número`);
  if (typeof discount !== "number")
    return console.error(`El valor ${discount} ingresado, NO es un número`);
  if (amount === 0) return console.error("El monto no puede ser 0");
  if (discount === 0) return console.error("El descuento no puede ser 0");
  if (Math.sign(amount) === -1) return console.error("El monto no puede ser negativo");
  if (Math.sign(discount) === -1) return console.error("El descuento no puede ser negativo");

  return console.info(`$${amount} - ${discount}% = $${amount - (amount * discount) / 100}`);
};


applyDiscount(1000, 20); // 800