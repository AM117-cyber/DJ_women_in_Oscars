// const fs = require('fs');
// const csv = require('csv-parser');

// let categories = new Set();

// fs.createReadStream('the_emmy_awards.csv')
//   .pipe(csv())
//   .on('data', (row) => {
//     categories.add(row.category);
//   })
//   .on('end', () => {
//     fs.writeFileSync('categories.txt', Array.from(categories).join('\n'));
//     console.log('Categories written to categories.txt');
//   });
const fs = require('fs');

// Read the file
let categories = fs.readFileSync('categories.txt', 'utf-8').split('\n');

// Filter out categories that contain "actress" or "actor"
categories = categories.filter(category => !category.toLowerCase().includes('hairstyling') && !category.toLowerCase().includes('individual') && !category.toLowerCase().includes('female') && !category.toLowerCase().includes('choreograph') && !category.toLowerCase().includes('editing') && !category.toLowerCase().includes('technical') && !category.toLowerCase().includes('camera'));

// Write the remaining categories back to the file
fs.writeFileSync('categories.txt', categories.join('\n'));

console.log('Categories updated');

