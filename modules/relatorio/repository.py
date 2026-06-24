from core.database import DataBase
from .queries import QUERY_REPORT_BENS

class RelatorioRepository:
    def __init__(self):
        self.db = DataBase()

    def get_data_for_report(self, categoria_id=None, setor_id=None, status=None):
        query = QUERY_REPORT_BENS
        params = []

        if categoria_id:
            query += " AND b.id_categoria = %s"
            params.append(categoria_id)
        
        if setor_id:
            query += " AND s.id = %s"
            params.append(setor_id)
        
        if status:
            if status.lower() == 'baixado':
                query += " AND b.ativo = FALSE"
            else:
                query += " AND b.status = %s AND b.ativo = TRUE"
                params.append(status)

        query += " ORDER BY b.codigo_tombamento ASC"
        
        return self.db.execute(query, tuple(params))
