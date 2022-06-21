function requestData() {
    fetch('/request_data').then(function (response) {
        return response.json();
    }).then(function (body) {
        var table = document.getElementById('table');

        // Clear old table
        while (table.firstChild) {
            table.removeChild(myNode.lastChild);
        }

        var tableBody = document.createElement('tbody');

        table.appendChild(tableBody);

        // Create table
        var datetime = body['datetime'];
        var values = body['values'];
        for (var i = 0; i < datetime.length; i++) {
            var row = document.createElement('tr');

            // Create datetime cell
            var dt_cell = document.createElement('td');
            dt_cell.appendChild(document.createTextNode(datetime[i]));
            row.appendChild(dt_cell);
            // Create value cell
            var value_cell = document.createElement('td');
            value_cell.appendChild(document.createTextNode(values[i]));
            row.appendChild(value_cell);

            tableBody.appendChild(row);
        }
    });
}