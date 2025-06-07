from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory storage for notes (could be replaced with a real DB)
notes = []
next_id = 1

# Get all notes
@app.route('/notes', methods=['GET'])
def get_notes():
    return jsonify(notes), 200

# Get a single note by ID
@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = next((note for note in notes if note['id'] == note_id), None)
    if note is None:
        abort(404, description="Note not found")
    return jsonify(note), 200

# Create a new note
@app.route('/notes', methods=['POST'])
def create_note():
    global next_id
    data = request.get_json()
    if not data or 'title' not in data or 'content' not in data:
        abort(400, description="Invalid request: 'title' and 'content' required")

    note = {
        'id': next_id,
        'title': data['title'],
        'content': data['content']
    }
    notes.append(note)
    next_id += 1
    return jsonify(note), 201

# Update a note
@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    data = request.get_json()
    note = next((note for note in notes if note['id'] == note_id), None)
    if note is None:
        abort(404, description="Note not found")

    note['title'] = data.get('title', note['title'])
    note['content'] = data.get('content', note['content'])
    return jsonify(note), 200

# Delete a note
@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    global notes
    note = next((note for note in notes if note['id'] == note_id), None)
    if note is None:
        abort(404, description="Note not found")

    notes = [note for note in notes if note['id'] != note_id]
    return jsonify({'message': 'Note deleted'}), 200

if __name__ == '__main__':
    app.run(debug=True)
  
