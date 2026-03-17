function toggleTheme() {
    const html = document.documentElement;
    const currentTheme = html.getAttribute('data-bs-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    html.setAttribute('data-bs-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
}

function updateThemeIcon(theme) {
    const icon = document.getElementById('theme-icon');
    if (icon) {
        icon.className = theme === 'dark' ? 'bi bi-moon-stars-fill' : 'bi bi-brightness-high-fill';
    }
}
function initGauge(el) {
    const risco = parseFloat(el.getAttribute('data-risco').replace(',', '.'));
    const ctx = el.getContext('2d');
    
    let corRisco = '#0ea5e9';
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

function initComp(el) {
    const ctx = el.getContext('2d');
    const d = { 
        atual: parseFloat(el.getAttribute('data-atual').replace(',', '.')),
        media: parseFloat(el.getAttribute('data-media').replace(',', '.')),
        falha: parseFloat(el.getAttribute('data-falha').replace(',', '.'))
    };

    let corDinamica = '#0ea5e9';
    if (d.atual >= d.falha) corDinamica = '#ef4444';
    else if (d.atual > d.media) corDinamica = '#f59e0b';

    new Chart(ctx, {
        type: 'bar',
        data: {
            labels: ['Ativo Atual', 'Média Real', 'Ponto Crítico'],
            datasets: [{
                data: [d.atual, d.media, d.falha],
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

function initTend() {
    const canvas = document.getElementById('canvasGraficoTendencia');
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    try {
        const dataElement = document.getElementById('dados-historico');
        if (!dataElement) return;

        const hist = JSON.parse(dataElement.textContent);

        console.log("Dados do Histórico carregados:", hist);

        if (!hist || hist.length === 0) {
            console.warn("Histórico vazio. O gráfico não será renderizado.");
            return;
        }

        new Chart(ctx, {
            type: 'line',
            data: {
                labels: hist.map((_, i) => `L${i + 1}`),
                datasets: [{
                    label: 'Evolução do Risco (%)',
                    data: hist.map(h => h.risco),
                    borderColor: '#0ea5e9',
                    backgroundColor: 'rgba(14, 165, 233, 0.1)',
                    fill: true,
                    tension: 0.4,
                    borderWidth: 3,
                    pointRadius: 5
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                scales: {
                    y: { beginAtZero: true, max: 100, ticks: { color: '#94a3b8' } },
                    x: { ticks: { color: '#94a3b8' } }
                },
                plugins: { legend: { display: false } }
            }
        });
    } catch (e) {
        console.error("ERRO AO PROCESSAR HISTÓRICO:", e);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-bs-theme', savedTheme);
    updateThemeIcon(savedTheme);

    const gRisco = document.getElementById('gaugeRisco');
    if (gRisco) initGauge(gRisco);

    const gComp = document.getElementById('canvasGraficoComparativo');
    if (gComp) initComp(gComp);

    const gTend = document.getElementById('canvasGraficoTendencia');
    if (gTend) initTend(gTend);
});