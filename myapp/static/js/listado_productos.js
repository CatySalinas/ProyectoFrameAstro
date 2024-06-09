$(document).ready(function() {
    $('#search-form').on('submit', function(e) {
        e.preventDefault();
        var query = $('#search-input').val();

        $.ajax({
            url: '{% url "ajax_buscador" %}',
            data: {
                'buscar': query
            },
            success: function(data) {
                $('#product-list').html(data);
            }
        });
    });
});