const uri = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(uri, function (data, textStatus) {
  if (textStatus === 'status') {
    try {
      const name = data.name;
      $('#character').text(name);
    } catch (error) {
      console.error(error);
    }
  }
});
