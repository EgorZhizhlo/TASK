from flask import Flask, request, jsonify, render_template, redirect, url_for
from elasticsearch import Elasticsearch
import pandas as pd
from utils import Index


app = Flask(__name__)
es = Elasticsearch(hosts=["http://elasticsearch:9200"])
INDEX_NAME = 'documents'
df = pd.read_csv("posts.csv", converters={"rubrics": eval})
print

@app.route("/", methods=['GET', 'POST'])
def home_route():
    if request.method == 'POST':
        query = request.form.get('query')
        if 'search' in request.form:
            return redirect(url_for('search', query=query))
        elif 'delete' in request.form:
            return redirect(url_for('delete', query=query))
    return render_template('home_template.html')


@app.route('/search', methods=['GET', 'POST'])
def search():
    text = request.args.get('query')
    if not text:   
        return f'ERROR'
    query = {
        "query": {
            "match": {
                "text": text
            }
        },
        "_source": False,
        "size": 20
    }

    response = es.search(index=INDEX_NAME, body=query)
    ids = [int(hit['_id']) for hit in response['hits']['hits']]
    query_df = df.loc[ids]
    query_df['created_date'] = pd.to_datetime(query_df['created_date'])
    return query_df.sort_values(by='created_date').to_json(orient="records", force_ascii=False)

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    global df 
    try:
        id = request.args.get('query')
        response = es.delete_by_query(
            index=INDEX_NAME,
            body={
                "query": {
                    "match": {
                        "_id": int(id)
                    }
                }
            }
        )
        df = df[df["id"] != int(id)]
        df.to_csv("posts.csv")
        return f'#{id} was deleted.'
    except Exception:
        return Exception

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    Index(es, INDEX_NAME, df)