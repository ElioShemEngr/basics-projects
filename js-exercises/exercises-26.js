const sortSpeciesByTeeth = (speciesArray) => {
    return speciesArray.sort((a, b) => a.numTeeth - b.numTeeth);
  };
  
  const speciesArray = [
    { speciesName: 'shark', numTeeth: 50 },
    { speciesName: 'dolphin', numTeeth: 80 },
    { speciesName: 'whale', numTeeth: 20 },
    { speciesName: 'seal', numTeeth: 30 }
  ];
  
  console.log(sortSpeciesByTeeth(speciesArray));