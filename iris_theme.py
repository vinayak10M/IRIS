import streamlit as st


def apply_theme():
	st.markdown(
		"""
		<style>
		@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=DM+Serif+Display&display=swap');
		:root {
			--ink: #1d302b;
			--green: #2f5d4e;
			--muted: #64736d;
			--paper: #f5f6f2;
			--line: #dce3dc;
			--accent: #bd6e4d;
		}
		.stApp { background: var(--paper); color: var(--ink); }
		[data-testid="stHeader"] { background: transparent; }
		.block-container { max-width: 1220px; padding-top: 2.4rem; padding-bottom: 4rem; }
		html, body { font-family: "DM Sans", "Segoe UI", sans-serif; }
		h1, h2, h3 { font-family: "DM Serif Display", Georgia, serif !important; color: var(--ink); }
		h1 { font-size: 2.75rem !important; line-height: 1.08 !important; }
		h2 { font-size: 1.7rem !important; }
		.eyebrow { color: var(--green); font-size: 0.72rem; font-weight: 700; letter-spacing: 0.09em; }
		.insight {
			background: #e9efea;
			border-left: 3px solid var(--accent);
			border-radius: 0 5px 5px 0;
			color: var(--ink);
			line-height: 1.55;
			margin: 0.4rem 0 1rem;
			padding: 0.8rem 1rem;
		}
		div[data-testid="stMetric"] {
			background: #edf1ec;
			border: 1px solid var(--line);
			border-radius: 5px;
			padding: 0.85rem 1rem;
		}
		div[data-testid="stMetricLabel"] { color: var(--muted); }
		[data-testid="stWidgetLabel"], [data-testid="stWidgetLabel"] p, label {
			color: var(--ink) !important;
			opacity: 1 !important;
		}
		[data-baseweb="select"] > div {
			background: #fff !important;
			border-color: var(--line) !important;
			color: var(--ink) !important;
		}
		.stButton > button[kind="primary"], .stFormSubmitButton > button[kind="primary"] {
			background: var(--green);
			border-color: var(--green);
			border-radius: 4px;
		}
		[data-testid="stSidebar"] { background: #eaf0eb; }
		[data-testid="stSidebar"] * { color: var(--ink) !important; }
		[data-testid="stSidebar"] a[aria-current="page"] { background: #dce7df !important; }
		</style>
		""",
		unsafe_allow_html=True,
	)