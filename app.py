from application import app, db

app.app_context().push()

with app.app_context():
    db.create_all()
    print("Database tables created.")

if __name__ == '__main__':
    app.run()

