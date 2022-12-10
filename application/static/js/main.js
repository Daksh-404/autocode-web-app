function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#imageResult')
                .attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
        document.getElementById( 'upload-label' ).innerHTML = input.files[0].name;
    }
}

$(function () {
$('#upload').on('change', function () {
    readURL(input);
});
});

var input = document.getElementById( 'upload' );

