function howOld(age, year){
    const currentYear = 2024;
    const yearDifference = year - currentYear;
    const yearBorn = currentYear - age + 1;

    if(yearDifference > 0){
        return `You will be ${age + yearDifference} in the year ${year}`;
    } else if(yearDifference < 0 && year < yearBorn){
        return `The year ${year} was ${yearBorn - year} years before you were born`;
    } else if (yearDifference < 0 && year >= yearBorn){
        return `You were ${year - yearBorn} in the year ${year}`;
    }
};

console.log(howOld(32, 2000));