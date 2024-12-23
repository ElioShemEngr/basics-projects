const rollTheDice = () => {
  let die1 = Math.floor(Math.random() * 7 + 1);
  let die2 = Math.floor(Math.random() * 7 + 1);
  return die1 + die2
}

console.log(rollTheDice());
