
document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("frmEmployee").addEventListener("submit", function(event) {
        if (!validateForm()) {
            event.preventDefault(); // Prevent form submission if validation fails
        }
    });
});
function validateForm() {
    let isValid = true;

    // Clear previous error messages
    document.querySelectorAll('.error-message').forEach(el => el.textContent = '');

    // Validate name
    const firstName = document.getElementById("FirstName").value;
    if (firstName.trim() === "") {
        document.getElementById("firstNameError").textContent = "Please enter first name";
        isValid = false;
    }
    const lastName = document.getElementById("LastName").value;
    if (lastName.trim() === "") {
        document.getElementById("lastNameError").textContent = "Please enter last name";
        isValid = false;
    }

    // Validate email
    const email = document.getElementById("EmailId").value;
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        document.getElementById("emailError").textContent = "Please enter a valid email address";
        isValid = false;
    }
    // Validate phone number
    const phone = document.getElementById("MobileNo").value;
    const phonePattern = /^\d{10}$/;
    if (!phonePattern.test(phone)) {
        document.getElementById("phoneError").textContent = "Please enter a valid 10-digit phone number";
        isValid = false;
    }

    return isValid;
}
