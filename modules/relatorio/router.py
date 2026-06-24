from typing import Optional
from fastapi import APIRouter, Response, Query
from .service import RelatorioService

router = APIRouter(prefix="/relatorio", tags=["Relatorio"])

@router.get("/exportar")
def exportar_relatorio(
    formato: str = Query(..., regex="^(xlsx|pdf)$"),
    categoria_id: Optional[int] = None,
    setor_id: Optional[int] = None,
    status: Optional[str] = None
):
    service = RelatorioService()
    
    if formato == "xlsx":
        buffer = service.gerar_excel(categoria_id, setor_id, status)
        headers = {
            'Content-Disposition': 'attachment; filename="inventario_patriflow.xlsx"'
        }
        return Response(
            buffer.getvalue(), 
            headers=headers, 
            media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
    
    else: # pdf
        pdf_bytes = service.gerar_pdf(categoria_id, setor_id, status)
        headers = {
            'Content-Disposition': 'attachment; filename="inventario_patriflow.pdf"'
        }
        return Response(
            pdf_bytes, 
            headers=headers, 
            media_type='application/pdf'
        )
