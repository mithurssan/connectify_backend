from application.models import Holiday

class HolidayController:
    @staticmethod
    def book_holiday(business_id, user_id, holiday_start_date, holiday_end_date, holiday_status):
        holiday = Holiday(business_id, user_id, holiday_start_date, holiday_end_date, holiday_status)
        holiday.save()

    def get_all_holidays():
        return Holiday.get_all()
