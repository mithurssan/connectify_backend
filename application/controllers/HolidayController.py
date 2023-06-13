from application.models import Holiday

class HolidayController:
    @staticmethod
    def book_holiday(business_id, user_id, holiday_start_date, holiday_end_date, holiday_status):
        holiday = Holiday(business_id, user_id, holiday_start_date, holiday_end_date, holiday_status)
        holiday.save()

    def get_all_holidays():
        return Holiday.get_all()

    @staticmethod
    def get_one_by_user_id(user_id):
        return Holiday.get_by_id(user_id)

    @staticmethod
    def update_user(holiday_id, business_id, user_id, holiday_start_date, holiday_end_date, holiday_status):
        user = Holiday.get_by_id(user_id)
        if user:
            user.username = username
            user.password = password
            user.update()
