from pathlib import Path
from flask import Flask, abort
app = Flask(__name__, static_url_path="")

@app.route("/")
def root():
  return app.send_static_file("index.html")

# @app.route("/<page>")
# def send_page(page):
#   extensions_to_try = ["", ".htm", ".html"]
#   for extension in extensions_to_try:
#     path_to_try = (Path(app.static_folder) / page).with_suffix(extension)
#     print(path_to_try)
#     if path_to_try.is_file():
#       return app.send_static_file(str(path_to_try.relative_to(Path(app.static_folder))))
  
#   abort(404)
