"""M&V Agent Eval Dashboard — Streamlit application.

Launch with: streamlit run dashboard/app.py

This dashboard reads from the SQLite trace store at ~/.mv_agent/traces.db
and provides views for prompt comparison, trace analysis, cost tracking,
and task success rates.
"""

import sys
from pathlib import Path

# Ensure src is on the path
sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta, timezone

from src.mv_agent.observability.store import TraceStore
from src.mv_agent.prompts import prompt_registry
from src.mv_agent.config import config

# Page config
st.set_page_config(
    page_title="M&V Agent Eval Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)


@st.cache_resource
def get_store():
    """Get or create the trace store."""
    return TraceStore()


def load_traces(store: TraceStore, limit: int = 1000) -> pd.DataFrame:
    """Load traces into a DataFrame."""
    traces = store.get_traces(limit=limit)
    if not traces:
        return pd.DataFrame()
    df = pd.DataFrame(traces)
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


def load_evals(store: TraceStore, limit: int = 500) -> pd.DataFrame:
    """Load eval results into a DataFrame."""
    evals = store.get_evals(limit=limit)
    if not evals:
        return pd.DataFrame()
    df = pd.DataFrame(evals)
    if "timestamp" in df.columns:
        df["timestamp"] = pd.to_datetime(df["timestamp"])
    return df


# Sidebar navigation
st.sidebar.title("M&V Eval Dashboard")
page = st.sidebar.radio(
    "Navigate",
    ["Overview", "Prompt Comparison", "Trace Viewer", "Cost Analysis", "Success Rates"],
)

store = get_store()
traces_df = load_traces(store)
evals_df = load_evals(store)

# ── Overview ──
if page == "Overview":
    st.title("M&V Agent — Eval Overview")

    stats = store.get_stats()

    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Traces", stats["total_traces"])
    col2.metric("Total Evals", stats["total_evals"])
    col3.metric("Success Rate", f"{stats['success_rate']:.1%}")
    col4.metric("Total Cost", f"${stats['total_cost_usd']:.2f}")

    if not traces_df.empty:
        st.subheader("Traces Over Time")
        traces_by_day = traces_df.set_index("timestamp").resample("D").size().reset_index(name="count")
        fig = px.area(traces_by_day, x="timestamp", y="count", title="Daily Trace Volume")
        fig.update_layout(template="plotly_white")
        st.plotly_chart(fig, use_container_width=True)

        st.subheader("Tool Usage Distribution")
        tool_counts = traces_df["tool_name"].value_counts()
        fig2 = px.pie(values=tool_counts.values, names=tool_counts.index, title="Calls by Tool")
        st.plotly_chart(fig2, use_container_width=True)

    # Registered prompts
    st.subheader("Registered Prompts")
    prompts_data = []
    for name in prompt_registry.list_prompts():
        versions = prompt_registry.list_versions(name)
        for v in versions:
            prompts_data.append({
                "Name": name,
                "Version": v.version,
                "Default": "✓" if v.is_default else "",
                "Description": v.description,
            })
    if prompts_data:
        st.dataframe(pd.DataFrame(prompts_data), use_container_width=True)

# ── Prompt Comparison ──
elif page == "Prompt Comparison":
    st.title("Prompt Version Comparison")

    if traces_df.empty:
        st.info("No trace data yet. Run some agent tasks to generate traces.")
    else:
        prompt_names = traces_df[traces_df["prompt_name"] != ""]["prompt_name"].unique()
        if len(prompt_names) > 0:
            selected = st.selectbox("Select Prompt", prompt_names)
            prompt_traces = traces_df[traces_df["prompt_name"] == selected]

            if "prompt_version" in prompt_traces.columns:
                versions = prompt_traces["prompt_version"].unique()

                comparison = []
                for v in versions:
                    v_traces = prompt_traces[prompt_traces["prompt_version"] == v]
                    comparison.append({
                        "Version": v,
                        "Calls": len(v_traces),
                        "Success Rate": f"{v_traces['success'].mean():.1%}",
                        "Avg Latency (ms)": f"{v_traces['latency_ms'].mean():.0f}",
                        "Avg Cost ($)": f"{v_traces['cost_usd'].mean():.4f}",
                        "Total Cost ($)": f"{v_traces['cost_usd'].sum():.4f}",
                    })

                st.dataframe(pd.DataFrame(comparison), use_container_width=True)

                # Side-by-side latency
                fig = px.box(
                    prompt_traces, x="prompt_version", y="latency_ms",
                    title="Latency Distribution by Version",
                    color="prompt_version",
                )
                fig.update_layout(template="plotly_white")
                st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No prompt-level trace data found. Traces exist but no prompt_name recorded.")

# ── Trace Viewer ──
elif page == "Trace Viewer":
    st.title("Tool-Call Trace Viewer")

    if traces_df.empty:
        st.info("No traces recorded yet.")
    else:
        col1, col2 = st.columns(2)
        with col1:
            tool_filter = st.selectbox(
                "Filter by Tool",
                ["All"] + list(traces_df["tool_name"].unique()),
            )
        with col2:
            status_filter = st.selectbox("Status", ["All", "Success", "Failed"])

        filtered = traces_df.copy()
        if tool_filter != "All":
            filtered = filtered[filtered["tool_name"] == tool_filter]
        if status_filter == "Success":
            filtered = filtered[filtered["success"] == 1]
        elif status_filter == "Failed":
            filtered = filtered[filtered["success"] == 0]

        st.dataframe(
            filtered[["timestamp", "tool_name", "prompt_name", "prompt_version",
                       "model", "latency_ms", "cost_usd", "success", "error"]].sort_values(
                "timestamp", ascending=False
            ),
            use_container_width=True,
        )

        # Error analysis
        failed = filtered[filtered["success"] == 0]
        if not failed.empty:
            st.subheader("Error Analysis")
            error_counts = failed["error"].value_counts().head(10)
            fig = px.bar(
                x=error_counts.values, y=error_counts.index,
                orientation="h", title="Top Errors",
                labels={"x": "Count", "y": "Error"},
            )
            fig.update_layout(template="plotly_white")
            st.plotly_chart(fig, use_container_width=True)

# ── Cost Analysis ──
elif page == "Cost Analysis":
    st.title("Cost & Token Analysis")

    if traces_df.empty:
        st.info("No cost data yet.")
    else:
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Cost", f"${traces_df['cost_usd'].sum():.4f}")
        col2.metric("Avg Cost/Call", f"${traces_df['cost_usd'].mean():.4f}")
        col3.metric("Total Tokens", f"{(traces_df['input_tokens'] + traces_df['output_tokens']).sum():,}")

        # Cost by model
        st.subheader("Cost by Model")
        if "model" in traces_df.columns:
            cost_by_model = traces_df.groupby("model")["cost_usd"].sum().reset_index()
            fig = px.bar(cost_by_model, x="model", y="cost_usd", title="Cost by Model")
            fig.update_layout(template="plotly_white")
            st.plotly_chart(fig, use_container_width=True)

        # Cost over time
        st.subheader("Cumulative Cost")
        cost_over_time = traces_df.sort_values("timestamp").copy()
        cost_over_time["cumulative_cost"] = cost_over_time["cost_usd"].cumsum()
        fig2 = px.line(
            cost_over_time, x="timestamp", y="cumulative_cost",
            title="Cumulative Cost Over Time",
        )
        fig2.update_layout(template="plotly_white")
        st.plotly_chart(fig2, use_container_width=True)

        # Token usage
        st.subheader("Token Usage by Tool")
        token_data = traces_df.groupby("tool_name").agg({
            "input_tokens": "sum",
            "output_tokens": "sum",
        }).reset_index()
        fig3 = px.bar(
            token_data, x="tool_name", y=["input_tokens", "output_tokens"],
            title="Token Usage by Tool", barmode="stack",
        )
        fig3.update_layout(template="plotly_white")
        st.plotly_chart(fig3, use_container_width=True)

# ── Success Rates ──
elif page == "Success Rates":
    st.title("Task Success Rates")

    if traces_df.empty:
        st.info("No data yet.")
    else:
        # By tool
        st.subheader("Success Rate by Tool")
        tool_success = traces_df.groupby("tool_name").agg(
            total=("success", "count"),
            successes=("success", "sum"),
        ).reset_index()
        tool_success["rate"] = tool_success["successes"] / tool_success["total"]

        fig = px.bar(
            tool_success, x="tool_name", y="rate",
            title="Success Rate by Tool",
            text=tool_success["rate"].apply(lambda x: f"{x:.0%}"),
            color="rate",
            color_continuous_scale=["#a13544", "#d19900", "#437a22"],
            range_color=[0, 1],
        )
        fig.update_layout(template="plotly_white", yaxis_tickformat=".0%")
        st.plotly_chart(fig, use_container_width=True)

        # Latency by tool
        st.subheader("Latency by Tool (ms)")
        fig2 = px.box(
            traces_df, x="tool_name", y="latency_ms",
            title="Latency Distribution by Tool",
            color="tool_name",
        )
        fig2.update_layout(template="plotly_white")
        st.plotly_chart(fig2, use_container_width=True)

        # Eval results
        if not evals_df.empty:
            st.subheader("Eval Pass Rates")
            eval_summary = evals_df.groupby("eval_name").agg(
                total=("passed", "count"),
                passed=("passed", "sum"),
            ).reset_index()
            eval_summary["rate"] = eval_summary["passed"] / eval_summary["total"]

            fig3 = px.bar(
                eval_summary, x="eval_name", y="rate",
                title="Eval Pass Rate by Test",
                color="rate",
                color_continuous_scale=["#a13544", "#437a22"],
                range_color=[0, 1],
            )
            fig3.update_layout(template="plotly_white", yaxis_tickformat=".0%")
            st.plotly_chart(fig3, use_container_width=True)
