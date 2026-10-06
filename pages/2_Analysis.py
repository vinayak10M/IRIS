import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris

from iris_theme import apply_theme

apply_theme()


@st.cache_data
def load_iris_data():
    dataset = load_iris(as_frame=True)
    data = dataset.frame.drop(columns="target")
    data["species"] = dataset.frame["target"].map(
        dict(enumerate(dataset.target_names))
    ).str.title()
    return data


data = load_iris_data()
species_names = sorted(data["species"].unique())
feature_names = [column for column in data.columns if column != "species"]

st.markdown('<div class="eyebrow">FIELD NOTES / 02</div>', unsafe_allow_html=True)
st.title("Measurements in context")
st.write("Compare species, explore relationships, and inspect the sample averages.")

selected_species = st.multiselect(
    "Include species",
    species_names,
    default=species_names,
)
filtered_data = data[data["species"].isin(selected_species)]

if not selected_species:
    st.info("Select at least one species to display the analysis.")
    st.stop()

st.caption(
    f"Showing {len(filtered_data)} flower measurements across "
    f"{len(selected_species)} species."
)

petal_averages = (
    filtered_data.groupby("species", observed=True)["petal length (cm)"]
    .mean()
    .sort_values(ascending=False)
    .rename("Mean petal length (cm)")
    .rename_axis("Species")
    .reset_index()
)
st.subheader("Average petal length")
st.bar_chart(
    petal_averages,
    x="Species",
    y="Mean petal length (cm)",
    height=330,
)
leading_species = petal_averages.iloc[0]
if len(petal_averages) > 1:
    petal_insight = (
        f'{leading_species["Species"]} has the longest average petal in this '
        f'selection at {leading_species["Mean petal length (cm)"]:.2f} cm.'
    )
else:
    petal_insight = (
        f'{leading_species["Species"]} has a mean petal length of '
        f'{leading_species["Mean petal length (cm)"]:.2f} cm in this dataset.'
    )
st.markdown(
    f'<div class="insight"><strong>Insight</strong> · {petal_insight}</div>',
    unsafe_allow_html=True,
)

st.divider()
st.subheader("Measurement profile")
average_measurements = filtered_data.groupby("species", observed=True)[
    feature_names
].mean().T
st.line_chart(average_measurements, height=360)
if average_measurements.shape[1] > 1:
    most_variable_feature = (
        average_measurements.max(axis=1) - average_measurements.min(axis=1)
    ).idxmax()
    measurement_spread = (
        average_measurements.loc[most_variable_feature].max()
        - average_measurements.loc[most_variable_feature].min()
    )
    profile_insight = (
        f'{most_variable_feature.replace(" (cm)", "")} separates the selected '
        f'species by the widest average range ({measurement_spread:.2f} cm).'
    )
else:
    profile_insight = (
        f'The line shows {selected_species[0]} average measurements across all four '
        f'features; add another species to compare their profiles.'
    )
st.markdown(
    f'<div class="insight"><strong>Insight</strong> · {profile_insight}</div>',
    unsafe_allow_html=True,
)

st.divider()
st.subheader("Explore the relationship")
axis_columns = st.columns(2)
with axis_columns[0]:
    x_feature = st.selectbox(
        "Horizontal axis",
        feature_names,
        index=2,
    )
with axis_columns[1]:
    y_feature = st.selectbox(
        "Vertical axis",
        feature_names,
        index=3,
    )

st.scatter_chart(
    filtered_data,
    x=x_feature,
    y=y_feature,
    color="species",
    height=430,
)
if x_feature == y_feature:
    st.markdown(
        '<div class="insight"><strong>Insight</strong> · '
        'Choose two different measurements to compare their relationship.</div>',
        unsafe_allow_html=True,
    )
else:
    correlation = filtered_data[x_feature].corr(filtered_data[y_feature])
    st.markdown(
        f'<div class="insight"><strong>Insight</strong> · '
        f'{x_feature.replace(" (cm)", "")} and {y_feature.replace(" (cm)", "")} '
        f'have a correlation of {correlation:.2f} in this selection. '
        f'Points closer together indicate more similar measurements.</div>',
        unsafe_allow_html=True,
    )

st.caption("Source: scikit-learn Iris dataset. Each point represents one flower.")
