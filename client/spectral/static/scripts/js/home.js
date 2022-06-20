function requestData() {
    fetch('/request_data').then(function (response) {
        return response.json();
    }).then(function (body) {
        console.log(body);
    });
}