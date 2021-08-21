from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs_so
from scrapper2 import get_jobs_wwr
from scrapper3 import get_jobs_ro
from exporter import save_to_file


app = Flask("SuperScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/report")
def report():
    word = request.args.get('word')
    if word:
        word = word.lower()
        existingJobs = db.get(word)
        if existingJobs:
            jobs = existingJobs
        else:
            jobs = get_jobs_so(word) + get_jobs_wwr(word) + get_jobs_ro(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template("report.html",
    searchingBy = word,
    resultsNumber = len(jobs),
    jobs = jobs
    )
    
@app.route("/export")
def export():
    try:
        word = request.args.get('word')
        if not word:
            raise Exception()
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs, word)
        return send_file("{word}.csv")
    except:
        return redirect("/")
        


app.run(host="0.0.0.0")

