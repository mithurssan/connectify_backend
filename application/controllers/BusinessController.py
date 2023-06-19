from application.models import Business


class BusinessController:
    def register_business(
        business_name, number, email, password, verify_token, verified
    ):
        business = Business(
            business_name, number, email, password, verify_token, verified
        )
        business.save()

    def get_all_businesses():
        return Business.get_all()

    @staticmethod
    def get_one_by_business_id(business_id):
        return Business.get_by_id(business_id)

    def get_one_by_business_verify_token(business_verify_token):
        return Business.get_by_token(business_verify_token)

    def update_business(business_id, business_email, business_name, business_password):
        business = Business.get_by_id(business_id)
        if business:
            business.business_email = business_email
            business.business_name = business_name
            business.password = business_password
            business.update()

    def delete_business(business_id):
        business = Business.get_by_id(business_id)
        if business:
            business.delete()
