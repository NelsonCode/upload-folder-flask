from sys import path
from flask import Blueprint, request, jsonify
import os
routes_folder = Blueprint("routes_folder", __name__)

CURRENT_DIRECTORY = os.getcwd() + "/"

@routes_folder.route("/upload", methods=["POST"])
def upload_folder():
    try:
        files = request.files.getlist("files")
        for file in files:
            directory_file = file.filename.split("/")
            directory_file.pop()
            directory_file = "/".join(directory_file)
            print(directory_file)
            if os.path.exists(CURRENT_DIRECTORY + directory_file) == False:
                os.mkdir(path=CURRENT_DIRECTORY + directory_file)
                file.save(CURRENT_DIRECTORY + file.filename)
            else:
                file.save(CURRENT_DIRECTORY + file.filename)
        return jsonify({"message": "success"})
    except  FileNotFoundError:
        return jsonify({"message": "FileNotFoundError"})