const fs = require('fs');
const lines = fs.readFileSync('c:/Users/Jesus/Desktop/voidProject/index.html', 'utf8').split('\n');
lines.forEach((line, index) => {
    if (line.toLowerCase().includes('ranking')) {
        console.log(`${index + 1}: ${line.trim()}`);
    }
});
