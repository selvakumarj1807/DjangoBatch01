function validateForm() {
    let valid = true;

    document.getElementById("nameError").innerText = "";
    document.getElementById("emailError").innerText = "";
    document.getElementById("passwordError").innerText = "";
    document.getElementById("confirmError").innerText = "";

    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    if (name.length < 3) {
        document.getElementById("nameError").innerText = "Name must be at least 3 characters";
        valid = false;
    }

    if (!email.includes("@")) {
        document.getElementById("emailError").innerText = "Invalid email address";
        valid = false;
    }

    if (password.length < 6) {
        document.getElementById("passwordError").innerText = "Password must be at least 6 characters";
        valid = false;
    }

    if (password !== confirmPassword) {
        document.getElementById("confirmError").innerText = "Passwords do not match";
        valid = false;
    }

    if (valid) {
        alert("Registration Successful!");
    }

    return false; // prevent form submit
}
