document.addEventListener('DOMContentLoaded', function() {
    // Анимация появления карточек при прокрутке
    const observeCards = () => {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.animation = 'fadeIn 0.6s ease forwards';
                    observer.unobserve(entry.target);
                }
            });
        }, { threshold: 0.1 });

        document.querySelectorAll('.book-card').forEach(card => {
            card.style.opacity = '0';
            observer.observe(card);
        });
    };
    observeCards();

    // Форма регистрации и входа
    const loginForm = document.getElementById('loginForm');
    const registerForm = document.getElementById('registerForm');
    const registerModal = document.getElementById('registerModal');
    const registerLink = document.getElementById('registerLink');
    const closeBtn = document.querySelector('.close-btn');

    if (registerLink && registerModal && closeBtn) {
        // Открытие модального окна регистрации
        registerLink.addEventListener('click', function(e) {
            e.preventDefault();
            registerModal.style.display = 'block';
        });

        // Закрытие модального окна
        closeBtn.addEventListener('click', function() {
            registerModal.style.display = 'none';
        });

        // Закрытие при клике вне модального окна
        window.addEventListener('click', function(e) {
            if (e.target === registerModal) {
                registerModal.style.display = 'none';
            }
        });
    }

    // Функция настройки валидации формы
    function setupFormValidation(form, inputs, submitButton, checkFunc) {
        if (!form) return;

        inputs.forEach(input => {
            if (!input) return;

            input.addEventListener('focus', function() {
                this.parentElement.classList.add('active');
            });

            input.addEventListener('blur', function() {
                this.parentElement.classList.remove('active');
                validateInput(this);
            });

            input.addEventListener('input', function() {
                validateInput(this);
                checkFunc();
            });
        });

        form.addEventListener('submit', function(e) {
            if (submitButton && submitButton.disabled) {
                e.preventDefault();
                return;
            }
        });
    }

    // Валидация полей ввода
    function validateInput(input) {
        const formGroup = input.parentElement;
        formGroup.classList.remove('valid', 'invalid');
        let isValid = input.checkValidity();

        if (input.id === 'email' || input.id === 'regEmail') {
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            isValid = emailPattern.test(input.value);
        }

        if (input.id === 'regConfirmPassword') {
            const regPasswordInput = document.getElementById('regPassword');
            if (regPasswordInput && regPasswordInput.value !== input.value) {
                document.getElementById('regConfirmPasswordGroup').classList.add('invalid');
                isValid = false;
            }
        }

        if (input.value) {
            formGroup.classList.add(isValid ? 'valid' : 'invalid');
        }

        return isValid;
    }

    // Проверка формы входа
    if (loginForm) {
        const emailInput = document.getElementById('email');
        const passwordInput = document.getElementById('password');
        const submitBtn = loginForm.querySelector('.submit-btn');

        function checkLoginFormValidity() {
            if (!emailInput || !passwordInput || !submitBtn) return;
            
            // Проверяем, что оба поля не пустые
            const isEmailValid = emailInput.value.trim() !== '';
            const isPasswordValid = passwordInput.value.trim() !== '';
            
            // Активируем/деактивируем кнопку
            submitBtn.disabled = !(isEmailValid && isPasswordValid);
            
            // Добавляем/убираем классы валидации
            emailInput.parentElement.classList.toggle('valid', isEmailValid);
            emailInput.parentElement.classList.toggle('invalid', !isEmailValid);
            passwordInput.parentElement.classList.toggle('valid', isPasswordValid);
            passwordInput.parentElement.classList.toggle('invalid', !isPasswordValid);
        }

        // Добавляем обработчики событий для полей ввода
        [emailInput, passwordInput].forEach(input => {
            if (input) {
                input.addEventListener('input', checkLoginFormValidity);
                input.addEventListener('blur', checkLoginFormValidity);
            }
        });

        // Инициализируем состояние кнопки
        checkLoginFormValidity();
    }

    // Проверка формы регистрации
    if (registerForm) {
        const regInputs = {
            firstName: document.getElementById('regFirstName'),
            lastName: document.getElementById('regLastName'),
            email: document.getElementById('regEmail'),
            password: document.getElementById('regPassword'),
            confirmPassword: document.getElementById('regConfirmPassword')
        };
        const regSubmitBtn = document.getElementById('regSubmitBtn');

        function checkRegisterFormValidity() {
            if (!regSubmitBtn) return;
            const isValid = Object.values(regInputs).every(input => 
                input && validateInput(input)
            );
            const doPasswordsMatch = regInputs.password.value === regInputs.confirmPassword.value;
            regSubmitBtn.disabled = !(isValid && doPasswordsMatch);
        }

        if (regSubmitBtn) regSubmitBtn.disabled = true;
        setupFormValidation(
            registerForm,
            Object.values(regInputs),
            regSubmitBtn,
            checkRegisterFormValidity
        );
    }
});
