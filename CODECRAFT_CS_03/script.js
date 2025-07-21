function checkPasswordStrength() {
  const password = document.getElementById("password").value;
  const strengthText = document.getElementById("strengthText");

  const length = password.length >= 8;
  const upper = /[A-Z]/.test(password);
  const lower = /[a-z]/.test(password);
  const number = /\d/.test(password);
  const special = /[!@#$%^&*(),.?":{}|<>]/.test(password);

  updateCriteria("length", length);
  updateCriteria("uppercase", upper);
  updateCriteria("lowercase", lower);
  updateCriteria("number", number);
  updateCriteria("special", special);

  const passed = [length, upper, lower, number, special].filter(Boolean).length;

  if (password.length === 0) {
    strengthText.textContent = "";
  } else if (passed <= 2) {
    strengthText.textContent = "Weak ❌";
    strengthText.style.color = "red";
  } else if (passed === 3 || passed === 4) {
    strengthText.textContent = "Moderate ⚠️";
    strengthText.style.color = "orange";
  } else if (passed === 5) {
    strengthText.textContent = "Strong ✅";
    strengthText.style.color = "green";
  }
}

function updateCriteria(id, isValid) {
  const element = document.getElementById(id);
  element.className = isValid ? "valid" : "invalid";
}
