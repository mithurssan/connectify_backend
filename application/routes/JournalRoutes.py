from application.controllers import JournalController, UserController
from application.models import User, Journal
from flask import Blueprint, abort, request
from flask import jsonify
# from flask_jwt_extended import jwt_required, get_jwt_identity
entry = Blueprint('entry', __name__)

@entry.route('/', methods=["GET"])
def get_users():
    entries = JournalController.get_all_entries()
    entry_list=[]
    for entry in entries:
        entry_list.append(format_entries(entry))
    return jsonify(entry_list)

def format_entries(entry):
    return {
        "entry_id": entry.entry_id,
        "user_id": entry.user_id,
        "entry_date": entry.entry_date,
        "entry_title": entry.entry_title,
        "entry_content": entry.entry_content
    }

@entry.route('/user/<user_id>', methods=["GET"])
def get_user_entries(user_id):
    entries = Journal.query.filter_by(user_id=user_id).order_by(Journal.entry_id.desc()).all()
    entry_list = [format_entry(entry) for entry in entries]
    return jsonify(entry_list)

def format_entry(entry):
    return {
        "entry_id": entry.entry_id,
        "user_id": entry.user_id,
        "entry_date": entry.entry_date,
        "entry_title": entry.entry_title,
        "entry_content": entry.entry_content
    }


@entry.route('/add', methods=['POST'])
def create_entry():
    data = request.get_json()
    user_id = data['user_id']
    entry_date = data['entry_date']
    entry_title = data['entry_title']
    entry_content = data['entry_content']

    # Create the journal entry with the obtained user_id
    JournalController.post_entry(user_id, entry_date, entry_title, entry_content)
    return jsonify({'message': 'Entry submitted.'})

@entry.route('/<entry_id>', methods=['GET'])
def get_user_by_id(entry_id):
    entry = JournalController.get_one_by_entry_id(entry_id)
    if entry:
        return jsonify(format_entries(entry))
    else:
        abort(404, 'Entry not found')


@entry.route('/update/<int:entry_id>', methods=['PUT'])
def update_entry(entry_id):
    data = request.json
    user_id = data['user_id']
    entry_date = data['entry_date']
    entry_title = data['entry_title']
    entry_content = data['entry_content']
    JournalController.update_entry(entry_id, user_id, entry_date, entry_title, entry_content)
    return jsonify({"message": "Entry updated successfully"})


@entry.route('/delete/<int:entry_id>', methods=['DELETE'])
def delete_entry(entry_id):
    JournalController.delete_entry(entry_id)
    return jsonify({"message": "Entry deleted successfully"})
