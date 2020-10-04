from io import StringIO
from math import pi
from datetime import datetime

import requests
import pandas as pd

from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource, LabelSet, Label
from bokeh.models.tools import HoverTool
import bokeh.colors.named
from bokeh.models import NumeralTickFormatter
from bokeh.io import export_png, export_svgs

df = pd.read_csv("./mitchydsalary - Sheet1-2.csv", sep=",")
df["Year_String"] = [str(year) for year in df["Year"]]

PURDUE_TOOLTIPS = [
    ("Year", "@Year"),
    ("Compensation", "@Compensation{$0,0.000}"),
]

source = ColumnDataSource(df)

p = figure(title="Mitch Daniels' salary from 2013 to 2020", plot_width=1600, plot_height=900, x_range=df["Year_String"], tooltips=PURDUE_TOOLTIPS, toolbar_location="above")
p.sizing_mode = "scale_width"

purdue_line = p.line("Year_String", "Compensation", line_width=5, line_color="goldenrod", muted_color="goldenrod", muted_alpha=0.2, source=source, legend_label="Mitch Daniels' Compensation")

labels = LabelSet(x='Year_String', y='Compensation', text='Compensation', level='glyph',
              x_offset=5, y_offset=5, source=source, render_mode='canvas')


p.toolbar.active_drag = None
p.legend.location = "top_left"
p.legend.click_policy="mute"
p.add_layout(Label(x=2016, y=900000))
p.yaxis.formatter=NumeralTickFormatter(format="$0,0.00")

p.output_backend = "svg"

export_svgs(p, filename="plot.svg")

