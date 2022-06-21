var page_number = 0;

function requestData() {
    var page_size_select = document.getElementById('page_size');
    var page_size = page_size_select.options[page_size_select.selectedIndex].value;

    fetch('/request_data?' + 
          new URLSearchParams({'page_number': page_number, 
                               'page_size': page_size})
    ).then(function (response) {
        return response.json();
    }).then(function (body) {
        var table = document.getElementById('table');

        // Clear old table
        while (table.firstChild) {
            table.removeChild(table.lastChild);
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

        // Data successfully loaded we can now use next and prev buttons
        document.getElementById('next_btn').disabled = false;
        if (page_number !== 0) {
            document.getElementById('prev_btn').disabled = false;
        }
        
        // If there's no more data then we disable next button
        if (body['more'] === false) {
            document.getElementById('next_btn').disabled = true;
        }
    });
}

function nextPage() {
    page_number++;
    if (page_number > 0) {
        document.getElementById('prev_btn').disabled = false;
    }
    requestData();
}

function prevPage() {
    page_number--;
    if (page_number < 0) {
        page_number = 0;
    }
    if (page_number === 0) {
        document.getElementById('prev_btn').disabled = true;
    }
    requestData();
}

// On page size change reset page number to 0
function resetPageNumber() {
    page_number = 0;
    document.getElementById('prev_btn').disabled = true;
    requestData();
}