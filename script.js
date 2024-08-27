import { initPopup } from "./header/header.js";
import { registerUser } from "./api/api.js";

document.addEventListener("DOMContentLoaded", (e) => {
  initPopup();

  const regButton = document.querySelector("#reg_btn")
  const reg_form = document.querySelector("#signup_form")

  reg_form.addEventListener("submit", function(e) {
    e.preventDefault();
  })

  const formData = {
    email: document.getElementById("email").value,
    username: document.getElementById("newUsername").value,
    password: document.getElementById("newPassword").value,
    secret_phrase: document.getElementById("secretPhrase").value
  };

  regButton.addEventListener("click", registerUser(formData))

});
