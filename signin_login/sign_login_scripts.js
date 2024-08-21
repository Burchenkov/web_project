export function initPopup() {
  const toggleSignup = document.getElementById("toggle-signup"); //Создаем константы элементов
  const toggleLogin = document.getElementById("toggle-login");
  const signupForm = document.getElementById("signup-form");
  const loginForm = document.getElementById("login-form");
  const overlay = document.getElementById("overlay");

  toggleSignup.addEventListener("click", () => {
    openForm(signupForm);
  });

  toggleLogin.addEventListener("click", () => {
    openForm(loginForm);
  });

  overlay.addEventListener("click", closeAllForms);

  function openForm(form) {
    // Показываем контейнер с формами
    overlay.classList.add("active"); // Показываем затемнение
    form.classList.add("active"); // Показываем выбранную форму
  }

  function closeAllForms() {
    // Скрываем контейнер с формами
    signupForm.classList.remove("active"); // Скрываем форму регистрации
    loginForm.classList.remove("active"); // Скрываем форму входа
    overlay.classList.remove("active"); // Убираем затемнение
  }
}
