import { $, $$, api, ui } from './utils.js';

let todosSetores = [];
let todosResponsaveis = [];

document.addEventListener('DOMContentLoaded', async () => {
    await Promise.all([carregarSetores(), carregarResponsaveis()]);
    configurarEventos();
});

async function carregarSetores() {
    try {
        todosSetores = await api.get('/api/v1/setores/');
        renderizarSetores(todosSetores);
    } catch (error) {
        ui.showNotification('Erro ao carregar setores', 'error');
    }
}

async function carregarResponsaveis() {
    try {
        todosResponsaveis = await api.get('/api/v1/responsavel/');
        const select = $('#responsavel_id');
        if (select) {
            select.innerHTML = '<option value="">Selecione um responsável...</option>' + 
                todosResponsaveis
                    .filter(r => r.ativo)
                    .map(r => `<option value="${r.id}">${r.nome}</option>`)
                    .join('');
        }
    } catch (error) {}
}

function renderizarSetores(setores) {
    const lista = $('#listaSetores');
    if (!lista) return;

    if (setores.length === 0) {
        lista.innerHTML = `<tr><td colspan="5" class="text-center py-5 text-muted">Nenhum setor encontrado.</td></tr>`;
        return;
    }

    lista.innerHTML = setores.map(setor => `
        <tr>
            <td class="px-4 fw-bold text-muted">#${setor.id}</td>
            <td><div class="fw-bold text-dark">${setor.nome}</div></td>
            <td><span class="text-muted small">${setor.responsavel_nome || 'Não definido'}</span></td>
            <td>
                <span class="badge ${setor.ativo ? 'bg-success-subtle text-success' : 'bg-danger-subtle text-danger'} rounded-pill px-3">
                    ${setor.ativo ? 'Ativo' : 'Inativo'}
                </span>
            </td>
            <td class="px-4 text-end">
                <button class="btn btn-sm btn-light btn-edit me-1" data-id="${setor.id}"><i class="fas fa-edit text-primary"></i></button>
                <button class="btn btn-sm btn-light btn-delete" data-id="${setor.id}"><i class="fas fa-trash-alt text-danger"></i></button>
            </td>
        </tr>
    `).join('');

    vincularAcoesTabela();
}

function configurarEventos() {
    $('#formSetor')?.addEventListener('submit', async (e) => {
        e.preventDefault();
        await salvarSetor();
    });

    $('#modalSetor')?.addEventListener('hidden.bs.modal', () => {
        $('#formSetor').reset();
        $('#setorId').value = '';
        $('#tituloModal').innerText = 'Novo Setor';
    });
}

async function salvarSetor() {
    const id = $('#setorId').value;
    const dados = {
        nome: $('#nome').value,
        responsavel_id: parseInt($('#responsavel_id').value)
    };

    ui.setLoading('btnSalvar', true);

    try {
        if (id) {
            // Rota: PUT /setores/{id}?novo_nome=...&novo_responsavel_id=...
            await api.put(`/api/v1/setores/${id}?novo_nome=${encodeURIComponent(dados.nome)}&novo_responsavel_id=${dados.responsavel_id}`);
            ui.showNotification('Setor atualizado!');
        } else {
            await api.post('/api/v1/setores/', dados);
            ui.showNotification('Setor cadastrado!');
        }

        bootstrap.Modal.getInstance($('#modalSetor')).hide();
        await carregarSetores();
    } catch (error) {
        ui.showNotification(error.message, 'error');
    } finally {
        ui.setLoading('btnSalvar', false);
    }
}

function vincularAcoesTabela() {
    $$('.btn-edit').forEach(btn => {
        btn.addEventListener('click', () => {
            const setor = todosSetores.find(s => s.id == btn.dataset.id);
            if (setor) {
                $('#setorId').value = setor.id;
                $('#nome').value = setor.nome;
                $('#responsavel_id').value = setor.responsavel_id;
                $('#tituloModal').innerText = 'Editar Setor';
                new bootstrap.Modal($('#modalSetor')).show();
            }
        });
    });

    $$('.btn-delete').forEach(btn => {
        btn.addEventListener('click', async () => {
            if (confirm('Deseja inativar este setor?')) {
                try {
                    await api.delete(`/api/v1/setores/?id=${btn.dataset.id}`);
                    ui.showNotification('Setor inativado!');
                    await carregarSetores();
                } catch (error) {
                    ui.showNotification(error.message, 'error');
                }
            }
        });
    });
}
