document.getElementById('resetPasswordForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const secretWord = 'секрет'; // Замените на секретное слово
    const enteredSecretWord = document.getElementById('secretWord').value;
    const newPassword = document.getElementById('newPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;
    const messageDiv = document.getElementById('message');

    if (enteredSecretWord !== secretWord) {
        messageDiv.textContent = 'Неверное секретное слово!';
        messageDiv.style.color = 'red';
    } else if (newPassword !== confirmPassword) {
        messageDiv.textContent = 'Пароли не совпадают, попробуйте еще раз.';
        messageDiv.style.color = 'red';
    } else {
        // Код для сохранения нового пароля на сервере
        const data = {
            secretWord: enteredSecretWord,
            newPassword: newPassword
      };
    };
});
