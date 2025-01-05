document.getElementById("signupform").addEventListener("submit", function (e) {
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    if (password !== confirmPassword) {
        e.preventDefault(); 
        alert("Passwords do not match! Please re-enter them.");
    }

    const strongPasswordRegex = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!strongPasswordRegex.test(password)) {
        e.preventDefault();
        alert("Password must be at least 8 characters long and include uppercase letters, numbers, and symbols.");
        return;
    }
});
