function changeLabelBarang(){
    $('#exampleModalLabel').html('Donasi Barang');
    $('#label_input').html('Input Barang');
    $('#input_type').val(2);
}

function changeLabelUang(){
    $('#exampleModalLabel').html('Donasi Uang');
    $('#label_input').html('Input Uang');
    $('#input_type').val(1);
}

function submit(){
    var tipe = $('#input_type').val()
    if (tipe == 1){
        var donasi = false;
        $.ajax({
            url:'.',
            method:'POST',
            data: {
                input: $('#input_donasi').val(),
                type: donasi,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
            },
            success: function(data) {
                alert("Donasi Uang berhasil dilakukan!")
            }
        });
    } else {
        var donasi = true;
        $.ajax({
            url:'.',
            method:'POST',
            data: {
                input: $('#input_donasi').val(),
                type: donasi,
                csrfmiddlewaretoken: $("input[name=csrfmiddlewaretoken]").val(),
            },
            success: function(data) {
                alert("Donasi Barang berhasil dilakukan!")
            }
        });
    }
}