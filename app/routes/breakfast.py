from flask import Blueprint, jsonify

class Breakfast():
    def __init__(self, id, name, rating, prep_time): # items, calories, 
        self.id = id
        self.name = name
        self.rating = rating
        self.prep_time = prep_time

breakfast_items = [
    Breakfast(1, "omelette", 4, 10),
    Breakfast(2, "french toast", 3, 15),
    Breakfast(3, "cereal", 1, 1),
    Breakfast(4, "oatmeal", 3, 10)
]

breakfast_bp = Blueprint("breakfast", __name__, url_prefix="/breakfast")

@breakfast_bp.route('', methods=['GET'])
def get_all_breakfasts():
    #return("hello world")
    result = []
    for item in breakfast_items:
        item_dict = {"id":item.id, "name":item.name, 
                    "rating":item.rating, "prep_time":item.prep_time}
        result.append(item_dict)
    
    return jsonify(result), 200

@breakfast_bp.route('/<breakfast_id>', methods=['GET'])
def get_one_breakfast(breakfast_id):
    try:
        breakfast_id = int(breakfast_id)
    except ValueError:
        return jsonify({"msg": f"invalid data type: {breakfast_id}"}), 400

    chosen_breakfast = None
    for breakfast in breakfast_items:
        if breakfast.id == breakfast_id:
            chosen_breakfast = breakfast

    if chosen_breakfast is None:
        return jsonify({"msg": f"Could not find breakfast item with id: {breakfast_id}"}), 404

    return_breakfast = {
        "id": chosen_breakfast.id,
        "name": chosen_breakfast.name,
        "rating": chosen_breakfast.rating,
        "prep_time": chosen_breakfast.prep_time
    }
    return jsonify(return_breakfast), 200

