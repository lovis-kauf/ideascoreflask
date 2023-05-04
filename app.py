from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    texts = [request.form["step1"], request.form["step2"], request.form["step3"], request.form["step4"], request.form["step5"]]
    summary = get_summary(texts)
    return jsonify(summary=summary)

def get_summary(texts):
    openai.api_key = "your_openai_api_key"
    prompt = "Summarize the following steps:\n" + "\n".join(texts)
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=100, n=1, stop=None, temperature=0.7)
    summary = response.choices[0].text.strip()
    return summary

if __name__ == "__main__":
    app.run(debug=True)
