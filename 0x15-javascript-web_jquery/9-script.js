const uri3 = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(uri3, function (data, textStatus) {
  if (textStatus === 'success') {
    try {
      $('#hello').text(data.hello);
    } catch (error) {
      console.error(error.message);
    }
  } else {
    console.error('something went wrong..');
  }
});
