from app import db

class Empresa(db.Model):
    __tablename__ = 'empresa'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete='CASCADE'), nullable=False)
    nome = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.Text, nullable=True)
    criado_em = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    usuario = db.relationship('Usuario', backref=db.backref('empresas', lazy=True, cascade='all, delete-orphan'))

    def __init__(self, usuario_id, nome, descricao=None):
        self.usuario_id = usuario_id
        self.nome = nome
        self.descricao = descricao

    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "nome": self.nome,
            "descricao": self.descricao,
            "criado_em": self.criado_em.strftime("%Y-%m-%d %H:%M:%S") if self.criado_em else None  # Formata timestamp
        }
