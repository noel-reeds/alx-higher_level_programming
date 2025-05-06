const uri = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(uri, function (data, textStatus) {
  if (textStatus === 'success') {
    try {
      const movies = data.results;
      for (const movie of movies) {
        if ('title' in movie) {
          $('<li></li>').text(movie.title).appendTo('#list_movies');
        } else {
          console.error('movie has no title');
        }
      }
    } catch (error) {
      console.error(error.message);
    }
  }
});
