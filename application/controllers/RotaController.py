from application.models import Rota

class RotaController:
    def post_rota(business_id, rota_start_date, rota_end_date, rota_content):
        rota = Rota(business_id, rota_start_date, rota_end_date, rota_content)
        rota.save()

    def get_all_rotas():
        return Rota.get_all()

    def get_one_by_rota_id(rota_id):
        return Rota.get_by_id(rota_id)

    def get_rotas_by_business_id(business_id):
        return Rota.get_all_by_business_id(business_id)

    def update_rota(rota_id, business_id, rota_start_date, rota_end_date, rota_content):
        rota = Rota.get_by_id(rota_id)
        if rota:
            rota.business_id = business_id
            rota.rota_start_date = rota_start_date
            rota.rota_end_date = rota_end_date
            rota.rota_content = rota_content
            rota.update()

    def delete_rota(rota_id):
        rota = Rota.get_by_id(rota_id)
        if rota:
            rota.delete()
