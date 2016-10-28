function post(uri, dataToSend) {
    $.post({
        url: uri,
        contentType: "application/json",
        dataType: 'json',
        data: JSON.stringify(dataToSend),
        success: function(data) {
            return {
                "success": data
            };
        },
        error: function(data) {
            return {
                "error": data
            };
        }
    });
}
