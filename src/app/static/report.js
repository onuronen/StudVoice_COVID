url = "https://studvoicecovid.herokuapp.com/"
document.querySelector("#problem_form").addEventListener("submit", function(evt) {
    evt.preventDefault();

    document.querySelector(".form_error").innerHTML = null;
    var short_description = document.querySelector("#short_description").value;
    var description = document.querySelector("#description_text_area").value;
    
    if (!short_description || !description) {
        var error_message = "Form not submitted. Short description and Description fields cannot be empty!";
        document.querySelector(".form_error").innerHTML = error_message;
        return;
    }


    fetch(url + "report_data", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
            'short_description': short_description,
            'description': description
        }
    })
    .then(response => response.json())
    .then(data => console.log(data));

    document.querySelector(".form_error").innerHTML = "Congrats! Submission succesful for review";
    document.querySelector("#short_description").value = null;
    document.querySelector("#description_text_area").value = null;


})