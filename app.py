import streamlit as st
import pandas as pd
import plotly.express as px

# ===============================
# PAGE CONFIG
# ===============================
st.set_page_config(
    page_title="MetroPulse | Real Estate Investment Analytics",
    layout="wide"
)

st.title("🏙️ MetroPulse: Real Estate Investment Analytics")
st.markdown(
    """
    **MetroPulse** identifies high-potential real estate micro-markets by
    combining **yield, growth, infrastructure, liquidity, risk, and clustering**.
    """
)

# ===============================
# LOAD DATA
# ===============================
@st.cache_data
def load_data():
    master = pd.read_csv("master_dataset.csv", parse_dates=["date"])
    score = pd.read_csv("market_investment_score_cluster_adjusted.csv")
    cluster = pd.read_csv("market_clusters_hdbscan.csv")
    return master, score, cluster

master_df, score_df, cluster_df = load_data()

# ===============================
# SIDEBAR FILTERS
# ===============================
st.sidebar.header("🔎 Filters")

markets = sorted(master_df["micro_market"].unique())
selected_markets = st.sidebar.multiselect(
    "Select Micro-Markets",
    markets,
    default=markets
)

property_types = master_df["property_type"].unique()
selected_types = st.sidebar.multiselect(
    "Property Type",
    property_types,
    default=property_types
)

# Apply filters
filtered = master_df[
    (master_df["micro_market"].isin(selected_markets)) &
    (master_df["property_type"].isin(selected_types))
]

# ===============================
# KPI SECTION
# ===============================
st.subheader("📊 Key Investment Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Avg Rental Yield (%)",
    round(filtered["rental_yield_pct"].mean(), 2)
)

col2.metric(
    "Avg Price Growth (YoY %)",
    round(filtered["yoy_price_growth"].mean(), 2)
)

col3.metric(
    "Avg Infra Score",
    round(filtered["infra_score"].mean(), 2)
)

col4.metric(
    "Avg Liquidity",
    round(filtered["liquidity_score"].mean(), 2)
)

# ===============================
# YIELD VS GROWTH
# ===============================
st.subheader("📈 Yield vs Capital Appreciation")

yg_df = (
    filtered.groupby("micro_market")
    .agg({
        "rental_yield_pct": "mean",
        "yoy_price_growth": "mean"
    })
    .reset_index()
)

fig_yg = px.scatter(
    yg_df,
    x="yoy_price_growth",
    y="rental_yield_pct",
    text="micro_market",
    labels={
        "yoy_price_growth": "Capital Appreciation (YoY %)",
        "rental_yield_pct": "Rental Yield (%)"
    }
)

st.plotly_chart(fig_yg, use_container_width=True)

# ===============================
# RISK VS RETURN
# ===============================
st.subheader("⚠️ Risk vs Return")

rr_df = (
    filtered.groupby("micro_market")
    .agg({
        "price_volatility": "mean",
        "yoy_price_growth": "mean"
    })
    .reset_index()
)

fig_rr = px.scatter(
    rr_df,
    x="price_volatility",
    y="yoy_price_growth",
    text="micro_market",
    labels={
        "price_volatility": "Risk (Price Volatility)",
        "yoy_price_growth": "Return (YoY %)"
    }
)

st.plotly_chart(fig_rr, use_container_width=True)

# ===============================
# CLUSTER VIEW
# ===============================
st.subheader("🧠 Market Clustering (HDBSCAN)")

cluster_view = score_df.merge(
    cluster_df[["micro_market", "cluster_label"]],
    on="micro_market",
    how="left"
)

fig_cluster = px.scatter(
    cluster_view,
    x="final_investment_score",
    y="rank",
    color="cluster_label",
    hover_name="micro_market",
    labels={
        "final_investment_score": "Final Investment Score",
        "rank": "Market Rank"
    }
)

st.plotly_chart(fig_cluster, use_container_width=True)

# ===============================
# INVESTMENT RANKING TABLE
# ===============================
st.subheader("🏆 Investment Ranking")

st.dataframe(
    cluster_view.sort_values("final_rank")[
        [
            "final_rank",
            "micro_market",
            "final_investment_score",
            "cluster_label"
        ]
    ],
    use_container_width=True
)

# ===============================
# MARKET DRILL-DOWN
# ===============================
st.subheader("🔍 Market Drill-Down")

market_selected = st.selectbox(
    "Select a micro-market",
    sorted(filtered["micro_market"].unique())
)

market_ts = filtered[
    filtered["micro_market"] == market_selected
]

fig_ts = px.line(
    market_ts,
    x="date",
    y="avg_price_sqft",
    color="property_type",
    title=f"Price Trend – {market_selected}"
)

st.plotly_chart(fig_ts, use_container_width=True)

# ===============================
# CONFIDENCE VIEW
# ===============================
st.subheader("🎯 Confidence vs Returns")

conf_df = filtered.dropna(subset=["confidence_score", "future_12m_growth"])

fig_conf = px.scatter(
    conf_df,
    x="final_investment_score",
    y="future_12m_growth",
    size="confidence_score",
    hover_name="micro_market",
    labels={
        "final_investment_score": "Investment Score",
        "future_12m_growth": "Future 12M Growth (%)"
    }
)

st.plotly_chart(fig_conf, use_container_width=True)

# ===============================
# FOOTER
# ===============================
st.markdown("---")
st.markdown(
    "**MetroPulse** – An end-to-end real estate investment analytics platform "
    "combining data engineering, analytics, ML clustering, and explainability."
)
