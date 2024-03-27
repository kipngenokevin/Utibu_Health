#!/usr/bin/python3
"""
Objects that haldle all default RESTFul API actions for FoodItems
"""
from models.medicine_records import Medicine
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request


@app_views.route('/medicine_items', methods=['GET'], strict_slashes=False)
def get_medical_items():
    """
    Retrieves the list of all medical items
    """
    all_medical_items = storage.all(Medicine).values()
    list_medical_items = [medical_item.to_dict() for medical_item in all_medical_items]
    return jsonify(list_medical_items)


