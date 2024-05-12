from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

# Variable to keep track of the process
process = None


@app.route("/start", methods=["GET"])
def start_process():
    global process
    if process is None:
        # Replace 'your_command_here' with the command you want to run
        process = subprocess.Popen(
            [
                "python",
                "-c",
                'import sys; sys.path.append("."); import script; script.start()',
            ]
        )
        return jsonify({"status": "Process started"}), 200
    else:
        return jsonify({"status": "Process is already running"}), 200


@app.route("/stop", methods=["GET"])
def stop_process():
    global process
    if process is not None:
        process.terminate()  # Sends SIGTERM
        process = None
        return jsonify({"status": "Process stopped"}), 200
    else:
        return jsonify({"status": "No process is running"}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5000)
