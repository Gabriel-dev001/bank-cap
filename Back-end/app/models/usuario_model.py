from app import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=True)
    google_id = db.Column(db.String(255), unique=True, nullable=True)
    criado_em = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __init__(self, nome, email, senha=None, google_id=None):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.google_id = google_id

    from app import db

class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    senha = db.Column(db.String(255), nullable=True)  # Não será incluída no JSON
    google_id = db.Column(db.String(255), unique=True, nullable=True)
    criado_em = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    def __init__(self, nome, email, senha=None, google_id=None):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.google_id = google_id

    def to_dict(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "email": self.email,
            "google_id": self.google_id,
            "criado_em": self.criado_em.strftime("%Y-%m-%d %H:%M:%S") if self.criado_em else None
        }