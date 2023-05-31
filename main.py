import flask, waitress

app = flask.Flask("RBXDatastoreManager_App")

@app.route("/")
def index():
    return "RBXDatastoreManager yay :3"

if __name__ == "__main__":
    waitress.run()