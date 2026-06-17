import { $, api } from '/static/js/utils.js';

/**
 * Dashboard.js - Lógica da página inicial com visualização de dados
 */

async function init() {
    await Promise.all([
        renderizarGraficoCategorias(),
        renderizarGraficoStatus(),
        renderizarUltimosRegistros()
    ]);
}

async function renderizarGraficoCategorias() {
    try {
        const stats = await api.get('/api/v1/bem/stats/categoria');
        const labels = stats.map(s => s[0]);
        const data = stats.map(s => s[1]);

        const ctx = document.getElementById('chartCategorias');
        if (!ctx) return;

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Quantidade de Bens',
                    data: data,
                    backgroundColor: 'rgba(130, 10, 209, 0.7)',
                    borderColor: 'rgba(130, 10, 209, 1)',
                    borderWidth: 1,
                    borderRadius: 8
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: { beginAtZero: true, grid: { display: false } },
                    x: { grid: { display: false } }
                }
            }
        });
    } catch (error) {
        console.error("Erro ao carregar gráfico de categorias:", error);
    }
}

async function renderizarGraficoStatus() {
    try {
        const stats = await api.get('/api/v1/bem/stats/status');
        const labels = stats.map(s => s[0]);
        const data = stats.map(s => s[1]);

        const ctx = document.getElementById('chartStatus');
        if (!ctx) return;

        new Chart(ctx, {
            type: 'doughnut',
            data: {
                labels: labels,
                datasets: [{
                    data: data,
                    backgroundColor: [
                        '#42b72a', // Sucesso
                        '#820ad1', // Primária
                        '#f1c40f', // Alerta
                        '#f02849'  // Perigo
                    ],
                    hoverOffset: 4,
                    borderWidth: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: 'bottom' }
                },
                cutout: '70%'
            }
        });
    } catch (error) {
        console.error("Erro ao carregar gráfico de status:", error);
    }
}

async function renderizarUltimosRegistros() {
    try {
        const bens = await api.get('/api/v1/bem/');
        // Ordena por ID desc e pega os 5 primeiros
        const recentes = bens.sort((a, b) => b.id - a.id).slice(0, 5);
        
        const tbody = $('#listaRecentes');
        if (!tbody) return;

        tbody.innerHTML = recentes.map(bem => `
            <tr>
                <td class="ps-4"><span class="text-muted">#${bem.id}</span></td>
                <td><span class="fw-bold text-dark">${bem.nome}</span></td>
                <td><span class="badge ${bem.ativo ? 'bg-success-subtle text-success' : 'bg-danger-subtle text-danger'} rounded-pill px-3">${bem.ativo ? 'Ativo' : 'Inativo'}</span></td>
                <td class="text-end pe-4">
                    <a href="/bens" class="btn btn-sm btn-light"><i class="fas fa-arrow-right"></i></a>
                </td>
            </tr>
        `).join('');
    } catch (error) {
        console.error("Erro ao carregar últimos registros:", error);
    }
}

// Inicializa quando o DOM estiver pronto
document.addEventListener('DOMContentLoaded', init);
