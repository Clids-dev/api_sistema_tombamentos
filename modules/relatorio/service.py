import pandas as pd
from io import BytesIO
from fpdf import FPDF
from .repository import RelatorioRepository

class RelatorioService:
    def __init__(self):
        self.repository = RelatorioRepository()

    def gerar_excel(self, categoria_id=None, setor_id=None, status=None):
        data = self.repository.get_data_for_report(categoria_id, setor_id, status)
        
        df = pd.DataFrame(data, columns=[
            'ID', 'Nome', 'Código Tombamento', 'Categoria', 
            'Setor Atual', 'Valor (R$)', 'Status', 'Situação'
        ])

        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Inventário')
        
        output.seek(0)
        return output

    def gerar_pdf(self, categoria_id=None, setor_id=None, status=None):
        data = self.repository.get_data_for_report(categoria_id, setor_id, status)
        
        pdf = FPDF(orientation='L', unit='mm', format='A4')
        pdf.add_page()
        pdf.set_font("helvetica", "B", 16)
        pdf.cell(0, 10, "PatriFlow - Relatório de Inventário de Bens", ln=True, align='C')
        pdf.ln(10)

        # Cabeçalho da tabela
        pdf.set_font("helvetica", "B", 10)
        pdf.set_fill_color(130, 10, 209) # Cor primária do PatriFlow
        pdf.set_text_color(255, 255, 255)
        
        cols = [
            ('Cód. Tombamento', 40), ('Nome do Bem', 70), 
            ('Categoria', 40), ('Setor Atual', 40), 
            ('Valor', 25), ('Status', 30), ('Sit.', 20)
        ]

        for col_name, width in cols:
            pdf.cell(width, 10, col_name, border=1, align='C', fill=True)
        pdf.ln()

        # Dados
        pdf.set_font("helvetica", "", 9)
        pdf.set_text_color(0, 0, 0)
        
        for row in data:
            # row indices based on QUERY_REPORT_BENS: 
            # 0:id, 1:nome, 2:codigo, 3:cat, 4:setor, 5:valor, 6:status, 7:situacao
            pdf.cell(40, 8, str(row[2]), border=1)
            pdf.cell(70, 8, str(row[1])[:35], border=1)
            pdf.cell(40, 8, str(row[3]), border=1)
            pdf.cell(40, 8, str(row[4] or 'Não Alocado'), border=1)
            pdf.cell(25, 8, f"R$ {row[5]:.2f}", border=1, align='R')
            pdf.cell(30, 8, str(row[6]), border=1)
            pdf.cell(20, 8, str(row[7]), border=1, align='C')
            pdf.ln()

        return bytes(pdf.output())
