/**
 * Sends an AJAX request to retrieve user data from the server.
 * 
 * @param {string} url - The URL of the PHP file to request from.
 * @param {string} method - The HTTP method used for the request (default is 'POST').
 * @param {string} dataType - The expected data type of the response (default is 'json').
 */
$(document).ready(function() {
    $.ajax({
        url: '0-send_data.php',
        dataType: 'json',
        method: 'POST',
        success: function(response) {
            // Display an alert with user's name and age from the response
            alert(`The value ${response.name} and I\'m ${response.age} years old`);
        },
        error: function(xhr, status, error) {
            alert(`AJAX request failed: ${status}, ${error}`);
        }
    });
});

/**
SOME IMPORTANT NOTE

In the context of an AJAX request, the xhr (XMLHttpRequest) object represents the XMLHttpRequest that was used to make the request. The status property of the xhr object provides information about the HTTP status of the request.

The status property typically holds an HTTP status code, which is a three-digit code returned by the server indicating the outcome of the request. Here are some common HTTP status codes and their meanings:

200: OK - The request was successful.
404: Not Found - The requested resource could not be found on the server.
500: Internal Server Error - The server encountered an unexpected condition that prevented it from fulfilling the request.
 */
