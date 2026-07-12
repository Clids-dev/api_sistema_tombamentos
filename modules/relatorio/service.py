import pandas as pd
from io import BytesIO
from fpdf import FPDF
from fpdf.fonts import FontFace
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

        pdf.set_font("helvetica", size=8)
        headings_style = FontFace(emphasis="BOLD", color=(255, 255, 255), fill_color=(130, 10, 209))
        with pdf.table(
            col_widths=(18, 30, 18, 18, 12, 16, 10),
            headings_style=headings_style,
            line_height=5,
            padding=1,
            text_align=("L", "L", "L", "L", "R", "C", "C"),
        ) as table:
            header = table.row()
            for label in ("Cód. Tombamento", "Nome do Bem", "Categoria", "Setor Atual", "Valor", "Status", "Sit."):
                header.cell(label)

            for row in data:
                report_row = table.row()
                for value in (
                    row[2], row[1], row[3] or "Sem categoria", row[4] or "Não alocado",
                    f"R$ {row[5]:.2f}", row[6], row[7],
                ):
                    report_row.cell(str(value))

        return bytes(pdf.output())
