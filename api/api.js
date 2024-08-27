export async function getData() {

    fetch("./header/header.html")
    .then((response) => response.text())
    .then((html) => {
      document.getElementById("header-placeholder").innerHTML = html;
    })
    .then(() => {
      const regButton = document.querySelector("#reg_btn");
      const reg_form = document.querySelector("#signup_form");

      reg_form.addEventListener("submit", function (e) {
        e.preventDefault();
      });

      const formData = {
        email: document.getElementById("email").value,
        username: document.getElementById("newUsername").value,
        password: document.getElementById("newPassword").value,
        secret_phrase: document.getElementById("secretPhrase").value,
      };

    });


    if (!response.ok) {
        alert("Регистрация не удалась, что-то пошло не так(")
        throw new Error('Registration failed');
    }else{
        alert("Регистрация успешна!!!")
    }

    return await response.json();
}