"""Chart Components"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

NBE_GREEN = "#006341"
NBE_GOLD  = "#D4AF37"


def render_gauge(
    value: float,
    title: str = "Risk Score",
    max_value: float = 100
) -> go.Figure:
    """
    Render risk score gauge chart

    Args:
        value:     Score value (0-100)
        title:     Chart title
        max_value: Maximum value

    Returns:
        Plotly figure
    """
    if value >= 70:
        bar_color = "#28a745"
    elif value >= 50:
        bar_color = "#ffc107"
    else:
        bar_color = "#dc3545"

    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=value,
        domain={"x": [0, 1], "y": [0, 1]},
        title={"text": title, "font": {"size": 20}},
        number={"suffix": "%", "font": {"size": 36}},
        gauge={
            "axis": {
                "range": [0, max_value],
                "tickwidth": 1,
                "tickcolor": "darkblue"
            },
            "bar": {"color": bar_color},
            "bgcolor": "white",
            "borderwidth": 2,
            "bordercolor": "gray",
            "steps": [
                {"range": [0, 50],  "color": "#fde8e8"},
                {"range": [50, 70], "color": "#fefde8"},
                {"range": [70, 100],"color": "#e8fef0"}
            ],
            "threshold": {
                "line": {"color": NBE_GREEN, "width": 4},
                "thickness": 0.75,
                "value": 70
            }
        }
    ))

    fig.update_layout(
        height=300,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor="white",
        font={"color": "#333", "family": "Arial"}
    )

    return fig


def render_confusion_matrix(
    tn: int, fp: int,
    fn: int, tp: int
) -> go.Figure:
    """Render confusion matrix heatmap"""
    z      = [[tn, fp], [fn, tp]]
    text_z = [
        [f"TN<br>{tn}", f"FP<br>{fp}"],
        [f"FN<br>{fn}", f"TP<br>{tp}"]
    ]

    fig = go.Figure(go.Heatmap(
        z=z,
        text=text_z,
        texttemplate="%{text}",
        textfont={"size": 20, "color": "white"},
        colorscale="Greens",
        showscale=False,
        x=["Predicted Bad", "Predicted Good"],
        y=["Actual Bad",    "Actual Good"]
    ))

    fig.update_layout(
        title="Confusion Matrix",
        height=350,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    return fig


def render_risk_distribution(df: pd.DataFrame) -> go.Figure:
    """Render risk distribution pie chart"""
    risk_counts = df["Risk"].value_counts()
    labels = ["Bad Risk (0)", "Good Risk (1)"]
    values = [
        risk_counts.get(0, 0),
        risk_counts.get(1, 0)
    ]

    fig = go.Figure(go.Pie(
        labels=labels,
        values=values,
        hole=0.4,
        marker_colors=["#dc3545", NBE_GREEN],
        textinfo="label+percent"
    ))

    fig.update_layout(
        title="Risk Distribution",
        height=350,
        showlegend=True,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    return fig


def render_feature_importance(
    features: list,
    importances: list,
    top_n: int = 10
) -> go.Figure:
    """Render feature importance bar chart"""
    df = pd.DataFrame({
        "feature":    features,
        "importance": importances
    }).sort_values("importance").tail(top_n)

    colors = [
        NBE_GREEN if i >= len(df) - 5
        else NBE_GOLD
        for i in range(len(df))
    ]

    fig = go.Figure(go.Bar(
        x=df["importance"],
        y=df["feature"],
        orientation="h",
        marker_color=colors,
        text=[f"{v:.3f}" for v in df["importance"]],
        textposition="outside"
    ))

    fig.update_layout(
        title=f"Top {top_n} Feature Importances",
        xaxis_title="Importance Score",
        height=400,
        margin=dict(l=20, r=20, t=50, b=20),
        paper_bgcolor="white"
    )

    return fig


def render_credit_distribution(df: pd.DataFrame) -> go.Figure:
    """Render credit amount distribution"""
    fig = go.Figure()

    for risk_val, color, name in [
        (0, "#dc3545", "Bad Risk"),
        (1, NBE_GREEN, "Good Risk")
    ]:
        subset = df[df["Risk"] == risk_val]["Credit_Amount"]
        fig.add_trace(go.Histogram(
            x=subset,
            name=name,
            marker_color=color,
            opacity=0.75,
            nbinsx=20
        ))

    fig.update_layout(
        title="Credit Amount Distribution by Risk",
        xaxis_title="Credit Amount",
        yaxis_title="Count",
        barmode="overlay",
        height=350,
        margin=dict(l=20, r=20, t=50, b=20)
    )

    return fig
