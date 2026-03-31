class UsuarioService:
    def __init__(self, repo):
        self.repo = repo

    def login(self, username, senha):
        user = self.repo.buscar_por_username(username)

        if not user:
            return None

        if user[2] != senha:  # senha
            return None

        if not user[4]:  # ativo
            return None

        return user