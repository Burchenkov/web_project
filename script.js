// Плашка Регистрации
document.addEventListener('DOMContentLoaded', () => {
    const toggleSignup = document.getElementById('toggle-signup');
      const toggleLogin = document.getElementById('toggle-login');
      const signupForm = document.getElementById('signup-form');
      const loginForm = document.getElementById('login-form');
  
      let isSignupVisible = false;
      let isLoginVisible = false;
  
      toggleSignup.addEventListener('click', () => {
          if (!isSignupVisible) {
              signupForm.style.top = '0%';
              signupForm.style.opacity = '1';
              isSignupVisible = true;
          } else {
              signupForm.style.top = '-20%';
              signupForm.style.opacity = '0';
              isSignupVisible = false;
          }
      });
  
      toggleLogin.addEventListener('click', () => {
          if (!isLoginVisible) {
              loginForm.style.top = '0%';
              loginForm.style.opacity = '1';
              isLoginVisible = true;
          } else {
              loginForm.style.top = '-20%';
              loginForm.style.opacity = '0';
              isLoginVisible = false;
          }
      });
  });