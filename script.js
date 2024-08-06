document.addEventListener('DOMContentLoaded', () => {
    const toggleSignup = document.getElementById('toggle-signup');
    const toggleLogin = document.getElementById('toggle-login');
    const signupForm = document.getElementById('signup-form');
    const loginForm = document.getElementById('login-form');
    const overlay = document.getElementById('overlay');
    const signupButton = document.querySelector('#signup-form button'); // Получаем кнопку регистрации
    const errorMessage = document.createElement('div'); // Создаем элемент для сообщения об ошибке
    errorMessage.style.color = 'red'; // Задаем цвет текста
    errorMessage.style.display = 'none'; // Скрываем сообщение по умолчанию
    signupForm.appendChild(errorMessage); // Добавляем сообщение в форму

    toggleSignup.addEventListener('click', () => {
        if (!signupForm.classList.contains('active')) {
            signupForm.classList.add('active');
            loginForm.classList.remove('active');
            overlay.classList.add('active');
        } else {
            signupForm.classList.remove('active');
            overlay.classList.remove('active');
        }
    });

    toggleLogin.addEventListener('click', () => {
        if (!loginForm.classList.contains('active')) {
            loginForm.classList.add('active');
            signupForm.classList.remove('active');
            overlay.classList.add('active');
        } else {
            loginForm.classList.remove('active');
            overlay.classList.remove('active');
        }
    });

    overlay.addEventListener('click', () => {
        signupForm.classList.remove('active');
        loginForm.classList.remove('active');
        overlay.classList.remove('active');
    });

    signupButton.addEventListener('click', (e) => {
        e.preventDefault(); // Предотвращаем отправку формы
        const email = document.getElementById('email').value.trim();
        const username = document.getElementById('newUsername').value.trim();
        const password = document.getElementById('newPassword').value.trim();
        const secretPhrase = document.getElementById('secretPhrase').value.trim();

        // Проверка на заполнение полей
        if (!email || !username || !password || !secretPhrase) {
            errorMessage.textContent = 'Заполните данные'; // Устанавливаем сообщение об ошибке
            errorMessage.style.display = 'block'; // Показываем сообщение
        } else {
            errorMessage.style.display = 'none'; // Скрываем сообщение, если все поля заполнены
            console.log('Форма отправлена', { email, username, password, secretPhrase });
        }
    });
});
