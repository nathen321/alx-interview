#!/usr/bin/node
const request = require('request');
const args = process.argv;

function addToUrl (url, addition) {
  // Remove trailing slash from URL if it exists
  const cleanedUrl = url.endsWith('/') ? url.slice(0, -1) : url;

  // Combine with a single slash
  return `${cleanedUrl}/${addition}`;
}

function fetchMovie (movieUrl) {
  return new Promise((resolve, reject) => {
    request(movieUrl, { json: true }, (error, response, body) => {
      if (error) reject(error);
      else resolve(body);
    });
  });
}

function fetchCharacters (URL) {
  return new Promise((resolve, reject) => {
    request(URL, { json: true }, (error, response, body) => {
      if (error) {
        reject(error); // Network errors (e.g., no internet)
      } else if (response.statusCode !== 200) {
        reject(new Error(`HTTP ${response.statusCode}: ${body?.message || 'Unknown error'}`)); // API errors
      } else {
        resolve(body?.name || body); // Safely return `name` or fallback to `body`
      }
    });
  });
}

async function fetchAll (URLs) {
  try {
    // Create an array of promises
    const promises = URLs.map(url => fetchCharacters(url));

    // Wait for all promises to resolve
    const names = await Promise.all(promises);

    return names;
  } catch (error) {
    console.error('Failed to fetch one or more characters:', error);
    throw error; // Re-throw to let caller handle it
  }
}

// Now you can use async/await!
async function main () {
  try {
    const movieUrl = addToUrl('https://swapi-api.alx-tools.com/api/films/', args[2]);
    const movie = await fetchMovie(movieUrl);
    const names = await fetchAll(movie.characters);
    for (let i = 0; i < names.length; i++) {
      console.log(names[i]);
    }
  } catch (error) {
    console.error('Error:', error);
  }
}

main();