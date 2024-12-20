console.log('Play - Rock, Paper, or Scissors');

const getUserChoice = userInput => {
  userInput = userInput.toLowerCase();

  if (userInput === 'rock' || userInput === 'paper' || userInput === 'scissors' || userInput === 'bomb') {
    return userInput;
  } else {
    console.log('The option is not valid!');
  }

};

function getComputerChoice() {
  let number = Math.floor(Math.random() * 3);
  if (number === 0){
    return 'rock';
  } else if (number === 1) {
    return 'paper';
  } else if (number === 2) {
    return 'scissors';
  }
};

function determineWinner(userChoice, computerChoice){
  if (userChoice === computerChoice) {
    console.log("It's a tie");
  } else if (userChoice === 'rock'){
      if (computerChoice === 'paper'){
        console.log(`The user choice : ${userChoice}`);
        console.log(`The PC choice : ${computerChoice}`);
        console.log('User Lost');
      } else if (computerChoice === 'scissors'){
        console.log(`The user choice : ${userChoice}`);
        console.log(`The PC choice : ${computerChoice}`);
        console.log('User Win!');
      }
  } else if (userChoice === 'paper') {
      if (computerChoice === 'scissors'){
        console.log(`The user choice : ${userChoice}`);
        console.log(`The PC choice : ${computerChoice}`);
        console.log('User Lost');
      } else if (computerChoice === 'rock'){
        console.log(`The user choice : ${userChoice}`);
        console.log(`The PC choice : ${computerChoice}`);
        console.log('User Win!');
      }   
  } else if (userChoice === 'scissors') {
      if (computerChoice === 'rock'){
        console.log(`The user choice : ${userChoice}`);
        console.log(`The PC choice : ${computerChoice}`);
        console.log('User Lost');
      } else if (computerChoice === 'paper'){
        console.log(`The user choice : ${userChoice}`);
        console.log(`The PC choice : ${computerChoice}`);
        console.log('User Win!');
      }
  } else if (userChoice === 'bomb') {
    console.log(`The user choice : ${userChoice}`);
    console.log(`The user is complety Winner!`);
  };
};

function playGame(userChoice = getUserChoice('bomb'),computerChoice = getComputerChoice()){
  determineWinner(userChoice, computerChoice);
};

playGame();
