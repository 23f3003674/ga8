# Marimo Notebook
# Email: 23f3003674@ds.study.iitm.ac.in
# This notebook demonstrates variable dependencies, interactivity, and dynamic markdown.

import marimo
import numpy as np

app = marimo.App()

# ----------------------------
# Cell 1: Slider Input
# ----------------------------
# Provides interactive input controlling the data generation.
# Downstream cells depend on this slider value.

@app.cell
def __(mo):
    slider = mo.ui.slider(1, 100, value=50, label="Number of Data Points")
    slider
    return slider,

# ----------------------------
# Cell 2: Data Generation (depends on slider)
# ----------------------------
# Uses the slider's value to create a synthetic dataset.
# Other cells depend on dataset and statistics.

@app.cell
def __(np, slider):
    n = slider.value
    x = np.linspace(0, 10, n)
    y = 3 * x + np.random.normal(0, 5, n)
    data = {"x": x, "y": y}
    data
    return data,

# ----------------------------
# Cell 3: Compute Summary Statistics
# ----------------------------
# Depends on generated dataset.

@app.cell
def __(np, data):
    mean_y = np.mean(data["y"])
    std_y = np.std(data["y"])
    summary = {"mean_y": mean_y, "std_y": std_y}
    summary
    return summary,

# ----------------------------
# Cell 4: Dynamic Markdown Output
# ----------------------------
# Markdown updates automatically based on slider input and stats.

@app.cell
def __(mo, slider, summary):
    text = f"""
# Interactive Data Summary

- **Number of points:** {slider.value}
- **Mean of y:** {summary['mean_y']:.2f}
- **Std of y:** {summary['std_y']:.2f}

This report updates automatically as you move the slider.
"""
    mo.md(text)
    return text,

if __name__ == "__main__":
    app.run()
