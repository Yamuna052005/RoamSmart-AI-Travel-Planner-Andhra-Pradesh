import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


def train_cost_model(data):

    df = pd.DataFrame(data)

    X = df[["rating", "category", "city", "distance", "season"]]
    y = df["estimated_cost"]

    categorical_features = ["category", "city", "season"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
        ],
        remainder="passthrough"
    )

    model = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("regressor", LinearRegression())
        ]
    )

    model.fit(X, y)

    return model


def predict_cost(model, rating, category, city, distance, season):

    input_data = pd.DataFrame([{
        "rating": rating,
        "category": category,
        "city": city,
        "distance": distance,
        "season": season
    }])

    prediction = model.predict(input_data)

    return float(prediction[0])