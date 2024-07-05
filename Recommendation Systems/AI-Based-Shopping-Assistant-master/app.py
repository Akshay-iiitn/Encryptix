import os
import pickle
import cv2
import numpy as np
import pandas as pd
from flask import Flask, request, render_template, url_for
from collections import Counter
import matplotlib.pyplot as plt

app = Flask(__name__)
app.config['DEBUG'] = True

# Load the trained model, labels, and cluster centers
with open('meanshift_model.pkl', 'rb') as f:
    ms, labels, cluster_centers, y, name = pickle.load(f)

# Function to find the cluster with the maximum number of points
def find_max(gg):
    max_count = gg[0]
    max_label = 0
    for label, count in gg.items():
        if count > max_count:
            max_count = count
            max_label = label
    return max_label

# Function to strip and convert list items
def stripp(rr):
    new = []
    for i in range(len(suggest)):
        p = str(rr[i]).replace('[', '').replace(']', '')
        new.append(int(p))
    return new

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        keyword = request.form['keyword']
        PATH = os.path.join(app.static_folder, "data")
        
        images = []
        for category in os.listdir(PATH):
            if category == keyword:
                path = os.path.join(PATH, category)
                images = [url_for('static', filename=f"data/{category}/{image}") for image in os.listdir(path)]
                return render_template('index.html', images=images, keyword=keyword)
        
        return render_template('index.html', error="Category not found.")
    
    return render_template('index.html')

@app.route('/recommendations', methods=['GET'])
def recommendations():
    gg = Counter(labels)
    max_label = find_max(gg)

    suggest = [y[i] for i in range(len(labels)) if labels[i] == max_label]
    new_Y = stripp(y)
    new_name = [name[i].replace('[', '').replace(']', '') for i in range(len(suggest))]

    recommendations = []
    for i in range(10):
        recommendations.append((new_Y[i], new_name[i]))

    return render_template('recommendations.html', recommendations=recommendations)

if __name__ == "__main__":
    app.run(debug=True)
