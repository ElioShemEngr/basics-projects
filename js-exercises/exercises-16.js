let secretMessage = ['Learning', 'is', 'not', 'about', 'what', 'you', 'get', 'easily', 'the', 'first', 'time,', 'it', 'is', 'about', 'what', 'you', 'can', 'figure', 'out.', '-2015,', 'Chris', 'Pine,', 'Learn', 'JavaScript'];

console.log(secretMessage.length);

secretMessage.pop();

console.log(secretMessage.length);
console.log(secretMessage);

secretMessage.push('to', 'Program');
console.log(secretMessage);

console.log(secretMessage.indexOf('easily'));
secretMessage[7] = 'right';

secretMessage.shift();

secretMessage.unshift('Programming');
console.log(secretMessage);

secretMessage[secretMessage.indexOf('get')] = 'know';
secretMessage[secretMessage.indexOf('right')] = 'know';
secretMessage[secretMessage.indexOf('the')] = 'know';
secretMessage[secretMessage.indexOf('first')] = 'know';
secretMessage[secretMessage.indexOf('time,')] = 'know';
console.log(secretMessage);

console.log(secretMessage.join());