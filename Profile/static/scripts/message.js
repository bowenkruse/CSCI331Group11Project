
$("#new_message").submit(function (event) {
    event.preventDefault();
    let message_content = document.getElementById("message_body").value;
    console.log(message_content);
    let user_to_message = document.getElementById('recipient').value;
    console.log(user_to_message)
    send_message(message_content, user_to_message);
});

function send_message(message_content, user_to_message) {
    $.ajax({
        url: "/ajax/send_message/",
        type: "POST",
        data: {
            "message_recipient": user_to_message,
            "message_body": message_content
        },
        dataType: 'json',
        success: function (json) {
            console.log('Success: ' + json['Success']);
            alert("Message Sent Successfully!");
            location.reload();
        },
        error: function () {
            console.log('Failure!');
            alert('Unable to submit rating');
        }
    });
}

