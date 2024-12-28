const dogFactory = (name, breed, weight) => {
    return {
      // Propiedades con un guion bajo antepuesto
      _name: name,
      _breed: breed,
      _weight: weight,
  
      // Getter para name
      get name() {
        return this._name;
      },
  
      // Setter para name
      set name(newName) {
        if (typeof newName === 'string') {
          this._name = newName;
        } else {
          console.log('Name must be a string');
        }
      },
  
      // Getter para breed
      get breed() {
        return this._breed;
      },
  
      // Setter para breed
      set breed(newBreed) {
        if (typeof newBreed === 'string') {
          this._breed = newBreed;
        } else {
          console.log('Breed must be a string');
        }
      },
  
      // Getter para weight
      get weight() {
        return this._weight;
      },
  
      // Setter para weight
      set weight(newWeight) {
        if (typeof newWeight === 'number' && newWeight > 0) {
          this._weight = newWeight;
        } else {
          console.log('Weight must be a positive number');
        }
      },
  
      // Método bark
      bark() {
        return 'ruff! ruff!';
      },
  
      // Método eatTooManyTreats
      eatTooManyTreats() {
        this._weight += 1; // Incrementa el peso en 1
      }
    };
  };
  
  dogFactory('Joe', 'Pug', 27);