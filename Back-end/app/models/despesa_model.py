from app import db

class Despesa(db.Model):
    __tablename__ = 'despesa'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete='CASCADE'), nullable=True)
    empresa_id = db.Column(db.Integer, db.ForeignKey('empresa.id', ondelete='CASCADE'), nullable=True)
    valor = db.Column(db.Numeric(10,2), nullable=False)
    data = db.Column(db.Date, nullable=False)
    categoria = db.Column(db.String(100), nullable=False)
    descricao = db.Column(db.String(1000), nullable=True)
    criado_em = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())

    usuario = db.relationship('Usuario', backref=db.backref('despesas', lazy=True, cascade='all, delete-orphan'))
    empresa = db.relationship('Empresa', backref=db.backref('despesas', lazy=True, cascade='all, delete-orphan'))

    def __init__(self, valor, data, categoria, usuario_id=None, empresa_id=None, descricao=None):
        self.usuario_id = usuario_id
        self.empresa_id = empresa_id
        self.valor = valor
        self.data = data
        self.categoria = categoria
        self.descricao = descricao

    def to_dict(self):
        return {
            "id": self.id,
            "usuario_id": self.usuario_id,
            "empresa_id": self.empresa_id,
            "valor": float(self.valor),  # Converte Decimal para float
            "data": self.data.strftime("%Y-%m-%d") if self.data else None,  # Formata date
            "categoria": self.categoria,
            "descricao": self.descricao,
            "criado_em": self.criado_em.strftime("%Y-%m-%d %H:%M:%S") if self.criado_em else None  # Formata timestamp
        }