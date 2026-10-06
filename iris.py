import pandas as pd
import streamlit as st
from sklearn.datasets import load_iris

from iris_theme import apply_theme

st.set_page_config(
	page_title="Iris Field Guide",
	page_icon="🌼",
	layout="wide",
	initial_sidebar_state="expanded",
)
apply_theme()

dataset = load_iris(as_frame=True)
iris_data = dataset.frame.copy()
iris_data["species"] = iris_data["target"].map(
	dict(enumerate(dataset.target_names))
).str.title()

species_details = {
	"Setosa": {
		"latin": "Iris setosa",
		"common": "Beachhead iris",
		"description": "A compact iris with noticeably shorter petals than the other two species in this dataset.",
		"image": "https://thumb.wikimedia.org/wikipedia/commons/thumb/d/d9/Wild_iris_flower_iris_setosa.jpg/500px-Wild_iris_flower_iris_setosa.jpg",
		"credit": "U.S. Fish and Wildlife Service 路 public domain",
		"source": "https://commons.wikimedia.org/wiki/File:Wild_iris_flower_iris_setosa.jpg",
	},
	"Versicolor": {
		"latin": "Iris versicolor",
		"common": "Northern blue flag",
		"description": "An intermediate-sized species; its average petal measurements sit between setosa and virginica.",
		"image": "https://thumb.wikimedia.org/wikipedia/commons/thumb/3/3b/Iris_versicolor_5.jpg/500px-Iris_versicolor_5.jpg",
		"credit": "Danielle Langlois 路 CC BY-SA",
		"source": "https://commons.wikimedia.org/wiki/File:Iris_versicolor_5.jpg",
	},
	"Virginica": {
		"latin": "Iris virginica",
		"common": "Virginia iris",
		"description": "The largest of the three in the classic Iris measurements, especially in petal length and width.",
		"image": "https://thumb.wikimedia.org/wikipedia/commons/thumb/9/9d/Iris_virginica_1.jpg/500px-Iris_virginica_1.jpg",
		"credit": "sonnia hill 路 CC BY 2.0",
		"source": "https://commons.wikimedia.org/wiki/File:Iris_virginica_1.jpg",
	},
}

st.markdown(
	'<div class="eyebrow">FIELD NOTES &nbsp; / &nbsp; IRIDACEAE</div>',
	unsafe_allow_html=True,
)
st.title("The Iris field guide")
st.write("Three related species, four measurements, and the patterns that set them apart.")

selected_species = st.selectbox(
	"Explore a species",
	list(species_details),
	format_func=lambda species: f"{species} 路 {species_details[species]['latin']}",
)
details = species_details[selected_species]
species_measurements = iris_data[iris_data["species"] == selected_species]

info_column, image_column = st.columns([0.95, 1.05], gap="large")
with info_column:
	st.markdown(
		f'<div class="eyebrow">SPECIES PROFILE / 0{list(species_details).index(selected_species) + 1}</div>',
		unsafe_allow_html=True,
	)
	st.header(details["common"])
	st.caption(details["latin"])
	st.write(details["description"])

	mean_petal_length = species_measurements["petal length (cm)"].mean()
	mean_petal_width = species_measurements["petal width (cm)"].mean()
	metric_columns = st.columns(2)
	metric_columns[0].metric("Mean petal length", f"{mean_petal_length:.1f} cm")
	metric_columns[1].metric("Mean petal width", f"{mean_petal_width:.1f} cm")
	st.caption("Averages from the 150-flower Iris dataset.")

with image_column:
	st.image(details["image"], width="stretch")
	st.caption(details["credit"])
	st.markdown(f"[View image source and license 鈫梋({details['source']})")

st.divider()
st.subheader("Four measurements")
measurement_columns = st.columns(4)
measurement_descriptions = [
	("Sepal length", "Length of the outer flower part."),
	("Sepal width", "Width of the outer flower part."),
	("Petal length", "Length of the inner flower part."),
	("Petal width", "Width of the inner flower part."),
]
for column, (name, description) in zip(measurement_columns, measurement_descriptions):
	with column:
		st.markdown(f"**{name}**")
		st.caption(description)
		st.caption("Measured in cm")

with st.expander("About the Iris dataset"):
	st.write(
		"The classic dataset contains 150 flowers, with 50 observations for each "
		"species. The measurements are useful for comparing species, but real "
		"flowers vary beyond these sample averages."
	)
