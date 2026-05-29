import { $, api } from '/static/js/utils.js';

/**
 * Dashboard.js - Lógica da página inicial
 */

async function init() {
    // Aqui poderíamos carregar dados dinâmicos caso o backend não os enviasse via Jinja2
    // Por enquanto, o dashboard usa dados passados pelo servidor
    setupListeners();
}

function setupListeners() {
    // Mobile toggle já é tratado no base.html via script compartilhado
}

// Inicializa quando o DOM estiver pronto
document.addEventListener('DOMContentLoaded', init);
