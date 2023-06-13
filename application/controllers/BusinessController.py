from application.models import Business


class BusinessController:
    @staticmethod
    def register_business(business_name, number, email, password):
        business = Business(business_name, number, email, password)

        business.save()

    @staticmethod
    def get_all_businesses():
        return Business.get_all()

    @staticmethod
    def get_one_by_business_id(business_id):
        return Business.get_by_id(business_id)

    @staticmethod
    def update_business(business_id, business_name, password):
        business = Business.get_by_id(business_id)
        if business:
            business.business_name = business_name
            business.password = password
            business.update()

    def delete_business(business_id):
        business = Business.get_by_id(business_id)
        if business:
            business.delete()
