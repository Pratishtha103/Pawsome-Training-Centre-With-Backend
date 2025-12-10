document.getElementById("loginform").addEventListener("submit", function (e) {
    const email = document.querySelector("#loginform input[name='email']").value;
    const username = document.querySelector("#loginform input[name='username']").value;

    // Basic validation for empty fields
    if (email.trim() === "" || username.trim() === "") {
        e.preventDefault(); // Prevent form submission
        alert("All fields are required.");
    }
});

document.querySelector("a").addEventListener("click", function (e) {
    e.preventDefault();
    alert("Forgot password feature is under construction!");
});