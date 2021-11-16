$("#rating").submit(function (event) {
    let val = document.getElementById("slider").value;
    let user_to_rate = document.getElementById('user_viewed').value;
    event.preventDefault();
    apply_rating(val, user_to_rate);
});
function openForm() {
    document.getElementById('ratingForm').style.display = "block";
}
function closeForm() {
    document.getElementById('ratingForm').style.display = "none";
}
function apply_rating(val, user_to_rate) {
    $.ajax({
        url: "/ajax/apply_rating/",
        type: "POST",
        data: {
            "given_rating" : val,
            "rated_user": user_to_rate
        },
        dataType: 'json',
        success : function (json) {
            closeForm();
            console.log('success!')
            console.log(json['rating'])
            alert("Rating submitted successfully")
            document.getElementById('ratingHeading').innerText = "Rating: " + json['rating']
        },
        error : function () {
            closeForm();
            console.log('Failure!')
            alert('Unable to submit rating')
        }
    });
}
