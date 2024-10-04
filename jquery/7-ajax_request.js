/**
 * Sends an AJAX request.
 *
 * @param {string} url - The URL to which the request is sent.
 * @param {string} method - The HTTP method to use for request.
 * @param {object} data - The data to send with the request. Default is an empty object.
 * @param {function} onSuccess - Callback function to execute if the request succeeds.
 * @param {function} onError - Callback function to execute if the request fails.
 */
function ajaxRequest(url, method, data = {}, onSuccess, onError) {
  $.ajax({
    url: url,
    method: method,
    Content-Type: 'application/json',
    data: method !== 'GET' ? data : undefined,
    success: onSuccess,
    error: onError
  });
}
