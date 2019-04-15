$( document ).ready(function() {

    // filter action
    $(document).on('change', '#order_by', function() {

        var filterValue = $(this).val();

        window.location.href = url + '?order_by=' + filterValue;

    });

});