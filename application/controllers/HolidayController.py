from application.models import Holiday

class HolidayController:
    @staticmethod
    def book_holiday(business_id, user_id, holiday_start_date, holiday_end_date, holiday_status):
        holiday = Holiday(business_id, user_id, holiday_start_date, holiday_end_date, holiday_status)
        holiday.save()

    def get_all_holidays():
        return Holiday.get_all()

    @staticmethod
    def get_one_by_user_id(holiday_id):
        return Holiday.get_by_id(holiday_id)

    @staticmethod
    def update_holiday(holiday_id, business_id, user_id, holiday_start_date, holiday_end_date, holiday_status):
        holiday = Holiday.get_by_id(holiday_id)
        if holiday:
            holiday.business_id = business_id
            holiday.user_id = user_id
            holiday.holiday_start_date = holiday_start_date
            holiday.holiday_end_date = holiday_end_date
            holiday.holiday_status = holiday_status
            holiday.update()
