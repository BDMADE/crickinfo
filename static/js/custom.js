$("input:checkbox").change(function() {
    var column = $('.playerTable').find('.' + $(this).attr("name"));
    $(column).toggle(this.checked);

    var customerTrs = $('.playerTable tbody tr'),
        summaryTable = $('.summaryTable tbody').empty();

    customerTrs.each(function() {
        var tr = $(this),
            year = tr.find('td').first().text();

        var visibleQuantities = tr.find('td:gt(0):visible').map(function() {
            return +$(this).text();
        }).get();

        var total = visibleQuantities.reduce(function(a, b) {
            return a + b;
        }, 0);

        var avg = total && total / visibleQuantities.length;

        var summaryTrs = '<tr><td>'+year+'</td><td>'+(avg > 499 ? 'Good' : 'Bad')+'</td><td>'+avg+'</td></tr>';

        summaryTable.append(summaryTrs);
    });
});

$("input:checkbox").last().change();
