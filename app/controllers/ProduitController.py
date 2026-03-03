from flask import render_template, redirect, url_for, request, current_app, flash
from app import app
import os
from werkzeug.utils import secure_filename
from app.services.ProduitService import ProduitService

class ProduitController:

    @app.route('/', methods=['GET'])
    def index():
        ps = ProduitService()
        produits = ps.getAll()
        return render_template('index.html', metadata={'title': "Accueil"}, produits=produits)

    @app.route('/vendre', methods=['GET', 'POST'])
    def vendre():
        if request.method == 'GET':
            return render_template('vendre.html', metadata={'title': "Vendre"})

        ps = ProduitService()
        nom = request.form.get('nom','').lower()
        prix = request.form.get('prix')
        description = request.form.get('description')
        categorie = request.form.get('categorie')
        statut = request.form.get('statut')

        filename = None
        photo = request.files.get('photo')
        if photo and photo.filename:
            filename = secure_filename(photo.filename).lower()
            photo.save(os.path.join(current_app.static_folder, 'img', filename))

        if statut not in ["nouveau", "tres_bon", "bon", "occasion"]:
            flash('Statut invalide.', 'error')
            return redirect(url_for('vendre'))

        if categorie not in ["electronique", "vetements", "meubles", "vehicules", "jeux", "autre"]:
            flash("Catégorie invalide.", "error")
            return redirect(url_for('vendre'))

        ps.addProduit(nom, prix, description, categorie, statut, filename)
        return redirect(url_for('index'))
