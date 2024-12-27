function greetAliens(aliens) {
  for (let i = 0; i < aliens.length; i++) {
    console.log(`Oh powerful ${aliens[i]}, we humans offer our unconditional surrender!`);
  }
}

const aliens = ["Blorgous", "Glamyx", "Wegord", "SpaceKing"];

greetAliens(aliens);