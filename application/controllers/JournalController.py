from application.models import Journal

class JournalController:
    @staticmethod
    def post_entry(user_id, entry_date, entry_title, entry_content):
        entry = Journal(user_id, entry_date, entry_title, entry_content)
        entry.save()

    def get_all_entries():
        return Journal.get_all()

    @staticmethod
    def get_one_by_entry_id(entry_id):
        return Journal.get_by_id(entry_id)

    @staticmethod
    def update_entry(entry_id, user_id, entry_date, entry_title, entry_content):
        entry = Journal.get_by_id(entry_id)
        if entry:
            entry.user_id = user_id
            entry.entry_date = entry_date
            entry.entry_title = entry_title
            entry.entry_content = entry_content
            entry.update()

    def delete_entry(entry_id):
        entry = Journal.get_by_id(entry_id)
        if entry:
            entry.delete()
