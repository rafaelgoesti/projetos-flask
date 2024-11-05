from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'chave-secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    with app.app_context():
        from .models import User
        try:
            db.create_all()  # Cria todas as tabelas
            inspector = inspect(db.engine)
            print("Tabelas criadas:", inspector.get_table_names())
        except Exception as e:
            print(f"Ocorreu um erro ao criar as tabelas: {e}")
    
    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app