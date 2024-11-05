from flask import render_template, request, redirect, url_for, flash
from flask import Blueprint
from .models import User
from . import db

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    users = User.query.all()
    return render_template('list.html', users=users)

@main_bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        if nome and email:
            user = User(nome=nome, email=email)
            db.session.add(user)
            db.session.commit()
            flash('Usuário salvo com sucesso!')
            return redirect(url_for('.index'))
        else:
            flash('Por favor, preencha todos os campos!')
    return render_template('create.html')


@main_bp.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        user.nome = request.form.get('nome')
        user.email = request.form.get('email')
        db.session.commit()
        flash('Usuário atualizado com sucesso!')
        return redirect(url_for('.index'))
    return render_template('update.html', user=user)

@main_bp.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    flash('Usuário deletado com sucesso!')
    return redirect(url_for('.index'))