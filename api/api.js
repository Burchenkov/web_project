export async function registerUser(userData) {
    const response = await fetch('https://yourbackend.com/api/signup/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
    });

    if (!response.ok) {
        throw new Error('Registration failed');
    }

    return await response.json();
}