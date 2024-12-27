"""To do this project I take help from this resources
https://www.kaggle.com/datasets/arshid/iris-flower-dataset/data
and https://github.com/Apaulgithub/oibsip_taskno1/blob/main/Iris_Flower_Classification.ipynb
"""



import joblib
import tkinter as tk
from tkinter import messagebox
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Function to build and save the model
def build_model():
    iris = load_iris()
    X, y = iris.data, iris.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

    # Create and train Decision Tree classifier
    clf = DecisionTreeClassifier()
    clf.fit(X_train, y_train)

    # Save the trained model to disk
    joblib.dump(clf, "iris_model.pkl")

# Function to classify the input data
def classify():
    try:
        # Load the trained model
        model = joblib.load("iris_model.pkl")
        iris = load_iris()

        # Get the input values from the user
        sepal_length = float(sepal_length_entry.get())
        sepal_width = float(sepal_width_entry.get())
        petal_length = float(petal_length_entry.get())
        petal_width = float(petal_width_entry.get())

        # Create the feature vector
        features = [sepal_length, sepal_width, petal_length, petal_width]

        # Make prediction
        result = iris.target_names[model.predict([features])[0]]
        
        # Display the result in a message box
        messagebox.showinfo("Result", f"The Iris flower is classified as: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Function to create and show the tkinter GUI
def show_dialogue():
    global sepal_length_entry, sepal_width_entry, petal_length_entry, petal_width_entry

    # Create the main application window
    app = tk.Tk()
    app.title("Iris Flower Classification")

    # Create labels and entry fields for input
    tk.Label(app, text="Sepal Length (cm):").grid(row=0, column=0, padx=10, pady=10)
    sepal_length_entry = tk.Entry(app)
    sepal_length_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(app, text="Sepal Width (cm):").grid(row=1, column=0, padx=10, pady=10)
    sepal_width_entry = tk.Entry(app)
    sepal_width_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(app, text="Petal Length (cm):").grid(row=2, column=0, padx=10, pady=10)
    petal_length_entry = tk.Entry(app)
    petal_length_entry.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(app, text="Petal Width (cm):").grid(row=3, column=0, padx=10, pady=10)
    petal_width_entry = tk.Entry(app)
    petal_width_entry.grid(row=3, column=1, padx=10, pady=10)

    # Button to trigger classification
    classify_btn = tk.Button(app, text="Classify", command=classify)
    classify_btn.grid(row=4, column=0, columnspan=2, pady=20)

    # Run the tkinter main loop
    app.mainloop()

# Main section
if __name__ == "__main__":
    build_model()  # Build and save the model
    show_dialogue()  # Display the GUI