def run():
    from app.app import create_app, load_users

    app = create_app()
    load_users()
    app.run(host='0.0.0.0', debug=True)

