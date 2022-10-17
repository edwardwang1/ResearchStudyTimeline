from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__, static_folder='static')
print("def", os.getcwd())


@app.route('/')
def SendJson():
    print("abc", os.getcwd())
    df = pd.read_csv("studies.csv")

    events = []
    for i in range(len(df)):
        media = {"url": df.iloc[i]["Media"], "caption:":df.iloc[i]["Media Caption"]}
        start_date = {"month":int(df.iloc[i]["Month"]), "day":int(df.iloc[i]["Day"]), "year":int(df.iloc[i]["Year"])}
        text = {"headline":df.iloc[i]["Headline"], "text":df.iloc[i]["Text"]}
        event = {"media":media, "start_date":start_date, "text":text}
        events.append(event)
    all_events = {"events": events}
    data = all_events
    return render_template("index.html", data=data)


@app.route('/<patient_Id>',  methods=['GET', 'POST'])
def SendJsonIndividual(patient_Id):
    if request.method == 'POST': # POST request
        print("-----------------post--------------")
        print(request.get_text())  # parse as text
        return 'OK', 200

    else: # GET request
        ##return 'ID = %s'%(patient_Id)
        df = pd.read_csv("studies.csv")
        patientDf = pd.read_csv("patients.csv")

        row = patientDf[patientDf["Patient"] == patient_Id]
        row = row.loc[:, (row != 0).any(axis=0)]
        cols = list(patientDf.columns)
        cols.remove("Patient")

        df = df[df.apply(lambda x: x["Headline"] in cols, axis=1)]

        events = []
        for i in range(len(df)):
            media = {"url": df.iloc[i]["Media"], "caption:":df.iloc[i]["Media Caption"]}
            start_date = {"month":int(df.iloc[i]["Month"]), "day":int(df.iloc[i]["Day"]), "year":int(df.iloc[i]["Year"])}
            text = {"headline":df.iloc[i]["Headline"], "text":df.iloc[i]["Text"]}
            event = {"media":media, "start_date":start_date, "text":text}
            events.append(event)
        all_events = {"events": events}
        data = all_events
        #return render_template("index.html", data=data)
        #print(data)
        #return data
        return render_template("index.html", data=data)

# @app.route('/hello', methods=['GET', 'POST'])
# def updateWithID():
    # return render_template('index.html', patientid=request.form['patientid'])

if __name__ == '__main__':
    app.run(debug=True)
