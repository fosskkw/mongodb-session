function getCredentials() {
    const emailElement = document.querySelector('.email-input');
    const passwordElement = document.querySelector('.password-input');

    const email = emailElement.value;
    const password = passwordElement.value;

    const userCredentials = {
        email: email,
        password: password
    };

    const jsonData = JSON.stringify(userCredentials);

    fetch('http://127.0.0.1:8000/login_in', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: jsonData
    })
    .then(response => response.json())
    .then(responseData => {
        console.log(responseData);
        window.location.href = 'login.html';
    })
    .catch(error => {
        console.error('Error:', error);
    });

    emailElement.value = null;
    passwordElement.value = null;
}