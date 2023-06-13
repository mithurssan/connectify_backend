from application.controllers import HolidayController
from flask import Blueprint, request
from flask import jsonify
holiday = Blueprint('holiday', __name__)

@holiday.route('/', methods=["GET"])
def get_users():
    holidays = HolidayController.get_all_holidays()
    holiday_list=[]
    for holiday in holidays:
        holiday_list.append(format_holidays(holiday))
    return jsonify(holiday_list)

def format_holidays(holiday):
    return {
        "holiday_id": holiday.holiday_id,
        "business_id": holiday.business_id,
        "user_id": holiday.user_id,
        "holiday_start_date": holiday.holiday_start_date,
        "holiday_end_date": holiday.holiday_end_date,
        "holiday_status": holiday.holiday_status
    }

@holiday.route('/book', methods=['POST'])
def create_holiday():
    data = request.get_json()
    business_id = data['business_id']
    user_id = data['user_id']
    holiday_start_date = data['holiday_start_date']
    holiday_end_date = data['holiday_end_date']
    holiday_status = data['holiday_status']

    HolidayController.book_holiday(business_id, user_id, holiday_start_date, holiday_end_date, holiday_status)
    return jsonify({'message': 'Holiday booked.'})

