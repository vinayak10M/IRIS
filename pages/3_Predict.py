import pickle
from pathlib import Path

import pandas as pd
import streamlit as st

from iris_theme import apply_theme

apply_theme()


@st.cache_resource
def load_model():
    model_path = Path(__file__).resolve().parents[1] / "model.pkl"
    with model_path.open("rb") as model_file:
        return pickle.load(model_file)


model = load_model()
st.markdown('<div class="eyebrow">FIELD NOTES / 03</div>', unsafe_allow_html=True)
st.title("Identify a flower")
st.write("Enter the four measurements to get a species prediction.")

with st.form("iris_prediction"):
    input_columns = st.columns(4)
    with input_columns[0]:
        sepal_length = st.slider("Sepal length (cm)", 4.0, 8.0, 5.0, 0.1)
    with input_columns[1]:
        sepal_width = st.slider("Sepal width (cm)", 2.0, 5.0, 3.0, 0.1)
    with input_columns[2]:
        petal_length = st.slider("Petal length (cm)", 1.0, 7.0, 3.0, 0.1)
    with input_columns[3]:
        petal_width = st.slider("Petal width (cm)", 0.1, 2.5, 1.0, 0.1)
    submitted = st.form_submit_button("Predict species", type="primary")

if submitted:
    feature_names = getattr(
        model,
        "feature_names_in_",
        [
            "sepal length (cm)",
            "sepal width (cm)",
            "petal length (cm)",
            "petal width (cm)",
        ],
    )
    measurements = pd.DataFrame(
        [[sepal_length, sepal_width, petal_length, petal_width]],
        columns=feature_names,
    )
    species = model.predict(measurements)[0]
    st.divider()
    result_column, measurement_column = st.columns([1.1, 0.9], gap="large")
    with result_column:
        st.markdown('<div class="eyebrow">MODEL RESULT</div>', unsafe_allow_html=True)
        st.success(f"Predicted species: {str(species).title()}")
        st.caption(
            "Prediction is based on the measurements entered above and the bundled "
            "Iris classification model."
        )
    with measurement_column:
        st.subheader("Submitted measurements")
        st.dataframe(
            measurements.T.rename(columns={0: "Value (cm)"}),
            width="stretch",
        )
