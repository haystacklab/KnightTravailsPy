from app import app
from app import service
from flask import request, jsonify
from flask_cors import CORS

CORS(app)

@app.route('/', methods=["POST"])
def index():
    startPosition = request.json.get('start')
    finishPosition = request.json.get('end')
    if startPosition is None or finishPosition is None:
        response = jsonify({'success': False, 'message': 'start of finsh required'})
        return response, 400
    elif len(startPosition) != 2 or len(finishPosition) != 2:
        response = jsonify({
            'success': 'false',
            'message': 'exactly 2 numbers required in start and finish'
        })
        return response, 400
    solutions = service.runKnightTravails(startPosition, finishPosition)
    response = jsonify({'success': True, 'solutions': solutions})
    # response.headers.add('Access-Control-Allow-Origin', '*')
    return response, 200
