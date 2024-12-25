const team = {
    _players: [{
      firstName: 'Elioshem',
      lastName: 'Solis',
      age: 32
    }, {
      firstName: 'Fabio',
      lastName: 'Mogrovejo',
      age: 28
    }, {
      firstName: 'Alondra',
      lastName: 'Castillo',
      age: 15
    }],
    _games: [{
      opponent: 'Lions',
      teamPoints: 42,
      opponentPoints: 35,
    }, {
      opponent: 'Tigers',
      teamPoints: 38,
      opponentPoints: 40,
    }, {
      opponent: 'Bears',
      teamPoints: 50,
      opponentPoints: 48,
    }],
    //Getters
    get players(){
      return this._players;
    },
    get games(){
      return this._games;
    },
    //Methods
    addPlayer (newFirstName, newLastName, newAge){
      let player = {
        firstName: newFirstName,
        lastName: newLastName,
        age: newAge
      };
        this.players.push(player);
    },
    addGame (newOpponent, newTeamPoints, newOpponentPoints){
      let game = {
        opponent: newOpponent,
        teamPoints: newTeamPoints,
        opponentPoints: newOpponentPoints
      };
        this.games.push(game);
    }
};

 team.addPlayer('Bugs', 'Bunny', 76);
 team.addGame('Titans', 100, 98);

 console.log(team._players);
 console.log(team._games);