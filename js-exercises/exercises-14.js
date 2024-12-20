function getSleepHours(day) {
    switch (day.toLowerCase()) {
      case "monday":
        return 8;
      case "tuesday":
        return 7;
      case "wednesday":
        return 5;
      case "thursday":
        return 8;
      case "friday":
        return 4;
      case "saturday":
        return 9;
      case "sunday":
        return 7;
      default:
        return "Please enter a valid day."; 
    };
  };
  
  function getActualSleepHours() {
    return (
      getSleepHours("monday") +
      getSleepHours("tuesday") +
      getSleepHours("wednesday") +
      getSleepHours("thursday") +
      getSleepHours("friday") +
      getSleepHours("saturday") +
      getSleepHours("sunday")
    );
  };
  
  function getIdealSleepHours(idealHours) {
    return idealHours * 7;
  };
  
  
  function calculateSleepDebt() {
    const actualSleepHours = getActualSleepHours();
    const idealSleepHours = getIdealSleepHours(8); 
  
    if (actualSleepHours === idealSleepHours) {
      console.log("Perfect amount of sleep! You got just the right amount.");
    } else if (actualSleepHours > idealSleepHours) {
      console.log(
        `You got more sleep than needed. You slept ${
          actualSleepHours - idealSleepHours
        } hour(s) more than your ideal amount.`
      );
    } else {
      console.log(
        `You should get some rest. You are ${
          idealSleepHours - actualSleepHours
        } hour(s) below your ideal sleep.`
      );
    }
  };
  
  
  calculateSleepDebt();