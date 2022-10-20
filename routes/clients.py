from flask import Blueprint, render_template, request, redirect, url_for, flash

from models.contact import Contact
from utils.db import db

clients = Blueprint('clients', __name__)


@clients.route('/')
def index():
    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)


@clients.route('/new', methods=['POST'])
def add_contact():
    full_name = request.form.get('full_name')
    email = request.form.get('email')
    phone = request.form.get('phone')

    new_contact = Contact(full_name, email, phone)
    db.session.add(new_contact)
    db.session.commit()

    flash(f'Contact {new_contact.full_name} added successfully to the database!')
    return redirect(url_for('clients.index'))


@clients.route('/update/<id_contact>',  methods=['GET', 'POST'])
def update(id_contact):
    contact = Contact.query.get(id_contact)

    if request.method == 'POST':
        contact.full_name = request.form.get('full_name')
        contact.email = request.form.get('email')
        contact.phone = request.form.get('phone')
        db.session.commit()

        flash(f'Contact {contact.full_name} updated successfully!')

        return redirect(url_for('clients.index'))

    else:
        return render_template('update.html', contact=contact)


@clients.route('/delete/<id_contact>')
def delete(id_contact):
    contact = Contact.query.get(id_contact)
    db.session.delete(contact)
    db.session.commit()

    flash(f'Contact {contact.full_name} deleted successfully!')

    return redirect(url_for('clients.index'))


@clients.route('/about')
def about():
    return render_template('about.html')
