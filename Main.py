    from flask import Flask, request, jsonify, send_from_directory
    import openai
    import os

    app = Flask(__name__)
    openai.api_key = "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"  # Replace with your key

    @app.route("/")
    def serve_index():
        return send_from_directory('.', 'index.html')

    @app.route("/<path:path>")
    def serve_static_file(path):
        return send_from_directory('.', path)

    @app.route("/generate", methods=["POST"])
    def generate():
        data = request.get_json()
        user_message = data.get("message")

        if not user_message:
            return jsonify({"error": "No message provided"}), 400

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or gpt-4 if you have access
                messages=[
                    {"role": "system", "content": "You are an expert in immigration bio writing. Respond concisely."},
                    {"role": "user", "content": user_message}
                ]
            )
            return jsonify({"reply": response.choices[0].message.content.strip()})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    app.run(host="0.0.0.0", port=81)
