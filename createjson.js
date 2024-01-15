const fs = require('fs');
const csv = require('csv-parser');

let data = {};

// Define the categories
let categories = {
    'writing': ['OUTSTANDING WRITING FOR A COMEDY SERIES', 'OUTSTANDING WRITING FOR A DRAMA SERIES', 'OUTSTANDING WRITING FOR A LIMITED OR ANTHOLOGY SERIES OR MOVIE', 'OUTSTANDING WRITING FOR A VARIETY SERIES', 'OUTSTANDING WRITING FOR A VARIETY SPECIAL'],
    'program': ['OUTSTANDING COMEDY SERIES', 'OUTSTANDING DRAMA SERIES', 'OUTSTANDING LIMITED OR ANTHOLOGY SERIES', 'OUTSTANDING TELEVISION MOVIE', 'OUTSTANDING TALK SERIES', 'OUTSTANDING SCRIPTED VARIETY SERIES', 'OUTSTANDING VARIETY SPECIAL (LIVE)', 'OUTSTANDING VARIETY SPECIAL (PRE-RECORDED)', 'OUTSTANDING SHORT FORM COMEDY, DRAMA OR VARIETY SERIES', 'OUTSTANDING SHORT FORM NONFICTION OR REALITY SERIES'],
    'music': ['OUTSTANDING MUSIC COMPOSITION FOR A SERIES (ORIGINAL DRAMATIC SCORE)', 'OUTSTANDING MUSIC COMPOSITION FOR A LIMITED OR ANTHOLOGY SERIES, MOVIE OR SPECIAL (ORIGINAL DRAMATIC SCORE)', 'OUTSTANDING MUSIC COMPOSITION FOR A DOCUMENTARY SERIES OR SPECIAL (ORIGINAL DRAMATIC SCORE)', 'OUTSTANDING MUSIC DIRECTION', 'OUTSTANDING ORIGINAL MUSIC AND LYRICS', 'OUTSTANDING ORIGINAL MAIN TITLE THEME MUSIC', 'OUTSTANDING MUSIC SUPERVISION'],
    'directing': ['OUTSTANDING DIRECTING FOR A COMEDY SERIES', 'OUTSTANDING DIRECTING FOR A DRAMA SERIES', 'OUTSTANDING DIRECTING FOR A LIMITED OR ANTHOLOGY SERIES OR MOVIE', 'OUTSTANDING DIRECTING FOR A VARIETY SERIES', 'OUTSTANDING DIRECTING FOR A VARIETY SPECIAL', 'OUTSTANDING DIRECTING FOR A DOCUMENTARY/NONFICTION PROGRAM', 'OUTSTANDING DIRECTING FOR A REALITY PROGRAM']
};

fs.createReadStream('the_emmy_awards.csv')
  .pipe(csv())
  .on('data', (row) => {
    // Convert the data to lowercase
    row.category = row.category.toLowerCase();
    row.nominee = row.nominee.toLowerCase();
    row.win = row.win.toLowerCase();

    // Check if the category is in the list
    for (let key in categories) {
      if (categories[key].includes(row.category.toUpperCase())) {
        // Replace the category name with the key
        row.category = key;

        // Parse the staff field
        let staffMembers = row.staff.split(';');
        for (let i = 0; i < staffMembers.length; i++) {
          let staffMember = staffMembers[i].split(',')[0].trim().toLowerCase();

          // Add the data to the JSON object
          if (!data[row.year]) {
            data[row.year] = {};
          }
          if (!data[row.year][row.category]) {
            data[row.year][row.category] = {};
          }
          if (!data[row.year][row.category][staffMember]) {
            data[row.year][row.category][staffMember] = {};
          }
          data[row.year][row.category][staffMember] = {
            name_of_work: row.nominee,
            winner: row.win
          };
        }
      }
    }
  })
  .on('end', () => {
    // Write the JSON data to a file
    fs.writeFileSync('data.json', JSON.stringify(data, null, 2));
    console.log('Data written to data.json');
  });

// fs.createReadStream('the_emmy_awards.csv')
//   .pipe(csv())
//   .on('data', (row) => {
//     // Check if the category is in the list
//     for (let key in categories) {
//       if (categories[key].includes(row.category.toUpperCase())) {
//         // Replace the category name with the key
//         row.category = key;

        
//           // Parse the staff field
//           let staffMembers = row.staff.split(';');
//           for (let i = 0; i < staffMembers.length; i++) {
//             let staffMember = staffMembers[i].split(',')[0].trim();
  
//             // Add the data to the JSON object
//             if (!data[row.year]) {
//               data[row.year] = {};
//             }
//             if (!data[row.year][row.category]) {
//               data[row.year][row.category] = {};
//             }
//             if (!data[row.year][row.category][staffMember]) {
//               data[row.year][row.category][staffMember] = {};
//             }
//             data[row.year][row.category][staffMember] = {
//               name_of_work: row.nominee,
//               winner: row.win
//             };
//           }
//         }
//       }
//     })
//   .on('end', () => {
//     // Write the JSON data to a file
//     fs.writeFileSync('data.json', JSON.stringify(data, null, 2));
//     console.log('Data written to data.json');
//   });
  
