$("#new_message").submit(function (event) {
    event.preventDefault();
    let message_content = document.getElementById("message_content").value;
    console.log(message_content);
    let user_to_rate = document.getElementById('recipient').value;
    send_message(message_content, user_to_rate);
});

function send_message(message_content, user_to_message) {
    $.ajax({
        url: "/ajax/apply_rating/",
        type: "POST",
        data: {
            "message_recipient": user_to_message,
            "message_body": message_content
        },
        dataType: 'json',
        success: function (json) {
            closeForm();
            console.log('success!')
            console.log(json['rating'])
            alert("Rating submitted successfully")
            document.getElementById('ratingHeading').innerText = "Rating: " + json['rating']
        },
        error: function () {
            closeForm();
            console.log('Failure!')
            alert('Unable to submit rating')
        }
    });
}


