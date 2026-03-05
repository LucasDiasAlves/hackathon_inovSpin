function initDashboard(riscoValue) {
    const ctx = document.getElementById('gaugeRisco').getContext('2d');
    const risco = parseFloat(riscoValue);
    
    let corRisco = '--status-stable';
    if (risco > 20) corRisco = '#22c55e';
    if (risco > 40) corRisco = '#eab308';
    if (risco > 75) corRisco = '#ef4444';

    new Chart(ctx, {
        type: 'doughnut',
        data: {
            datasets: [{
                data: [risco, 100 - risco],
                backgroundColor: [corRisco, 'rgba(200, 200, 200, 0.2)'],
                borderWidth: 0,
                circumference: 180,
                rotation: 270,
                cutout: '85%'
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
    const htmlElement = document.documentElement;
    const currentTheme = htmlElement.getAttribute('data-bs-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    htmlElement.setAttribute('data-bs-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    
    const icon = document.getElementById('theme-icon');
    icon.className = newTheme === 'dark' ? 'bi bi-moon-stars-fill' : 'bi bi-brightness-high-fill';
}

document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-bs-theme', savedTheme);
});

function initGraficoComparativo(dados) {
    const ctx = document.getElementById('canvasGraficoComparativo').getContext('2d');
    
    let corDinamica = '#0ea5e9';
    if (dados.atual >= dados.media_falha) corDinamica = '#ef4444';
    else if (dados.atual > dados.media_cat) corDinamica = '#f59e0b';

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Ativo Atual', 'Média Real (Base)', 'Ponto Crítico (Histórico)'],
            datasets: [{
                data: [dados.atual, dados.media_cat, dados.media_falha],
                backgroundColor: [corDinamica, '#22c55e', '#64748b'],
                borderRadius: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } }
        }
    });
}