function sellerSignUp() {
    $.ajax({
        type: 'POST',
        url: './seller/',
        data: $('#seller-form').serialize(),
        
        success: function(response) {
            if (response['success']) {
                var message = "You have succesfully signed up!";
                alert(message);
                document.getElementById("seller-form").reset();
                window.location.href = "../login/";
            }
            else {
                if ("warning" in response) {
                    alert(response['warning']);
                }
                else {
                    let req = false;
                    var message = "";
                    for (msg in response['error']) {
                        if (response['error'][msg]=="This field is required.") req = true;
                        else message += (response['error'][msg] + "\n");
                    }
                    if (req) var newMessage = "All fields are required to be filled."
                    else {
                      var newMessage = message.replaceAll(".,", ".\n")
                    }
                    alert(newMessage)
                }
            }
        },
    })
  }
  
  function buyerSignUp() {
    $.ajax({
        type: 'POST',
        url: './buyer/',
        data: $('#buyer-form').serialize(),
        
        success: function(response) {
            if (response['success']) {
                var message = "You have succesfully signed up!";
                alert(message);
                document.getElementById("buyer-form").reset();
                window.location.href = "../login/";
            }
            else {
                if ("warning" in response) {
                    alert(response['warning']);
                }
                else {
                    let req = false;
                    var message = "";
                    for (msg in response['error']) {
                        if (response['error'][msg]=="This field is required.") req = true;
                        else message += (response['error'][msg] + "\n");
                    }
                    if (req) var newMessage = "All fields are required to be filled."
                    else {
                      var newMessage = message.replaceAll(".,", ".\n")
                      newMessage = newMessage.replace(/@/g, "")
                    }
                    alert(newMessage)
                }
            }
        },
    })
  }
  
  let kategorilist = [
    "Makanan",
    "Pakaian",
    "Perlengkapan",
    "Rumah Tangga",
    "Otomotif",
    "Alat Tulis",
    "Kantor",
    "Kesehatan",
    "Kecantikan",
    "Alat Musik",
    "Gadget",
    "Aksesoris",
    "Footwear",
    "Tas"
  ];
  
  //Sort names in ascending order
  let sortedkategori = kategorilist.sort();
  var st = '<option disabled selected>--- Pilih Kategori ---</option>'; // variable to store the options
  for (var j = 0; j < sortedkategori.length; ++j) {
    st += '<option value="' + sortedkategori[j] + '" >' + sortedkategori[j] + '</option>'; // Storing options in variable
  }
  
  document.getElementById("select1").innerHTML = st;