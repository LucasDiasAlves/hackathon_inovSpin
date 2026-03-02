function initDashboard(riscoValue) {
    const ctx = document.getElementById('gaugeRisco').getContext('2d');
    const risco = parseFloat(riscoValue);
    const corRisco = risco > 70 ? '#dc3545' : (risco > 30 ? '#ffc107' : '#198754');

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [risco, 100 - risco],
                backgroundColor: [corRisco, '#e9ecef'],
                borderWidth: 0,
                circumference: 180,
                rotation: 270,
                cutout: '80%'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false }, tooltip: { enabled: false } }
        }
    });
}

function toggleTheme() {
    const body = document.body;
    const icon = document.getElementById('theme-icon');
    if (body.getAttribute('data-bs-theme') === 'light') {
        body.setAttribute('data-bs-theme', 'dark');
        icon.className = 'bi bi-moon-stars-fill';
    } else {
        body.setAttribute('data-bs-theme', 'light');
        icon.className = 'bi bi-brightness-high-fill';
    }
}