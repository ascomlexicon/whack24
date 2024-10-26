from flask import flash, redirect, url_for
from website import create_app

app = create_app()

@app.errorhandler(404)
def handle_404(error):
    print(f"Error: {error}")
    flash("That page does not exist. Redirecting to the home page...", category="error")
    return redirect(url_for("home.index"))


# @app.errorhandler(Exception)
# def handle_generic(error):
#     print(f"Error: {error}")
#     flash(f"We encountered an unknown error: {error}. Redirecting...")
#     return redirect(url_for("home.index"))

if __name__ == "__main__":
    app.run(debug=True)
