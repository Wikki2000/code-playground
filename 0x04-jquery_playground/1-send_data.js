$(document).ready(function () {
    $("button").click(function () {
        // Data to be sent to server side
        const dataToSend = { name: "Wisdom", age: 23 };

        // AJAX call
        $.ajax({
            url: '1-get_data.php',
            type: 'POST',
            contentTYPE: 'application/json',    
            data: JSON.stringify(dataToSend),
            success: function(feedback) {
                alert(`Response from server: ${feedback}`);
            },
            error: function (xhr, status, error_msg) {
                alert(`${error_msg}`);
            }
        });
    });
});
