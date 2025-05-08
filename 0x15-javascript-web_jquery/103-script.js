$(document).ready(function () {
  // retrieve LANGUAGE CODE & optional IP address
  $('#btn_translate').click(function () {
    const LANGUAGECODE = $('#language_code').val();
    const uri = `http://172.21.68.106:5000/native-hello/${LANGUAGECODE}`;
    console.log('Requesting:', uri);
    $.get(uri, function (data, textStatus) {
      if (textStatus === 'success') {
        try {
          const translatedHello = data.hello;
          $('#hello').text(translatedHello);
        } catch (error) {
          console.error(error);
        }
      } else {
        console.error('something went wrong..');
      }
    });
  });
});
