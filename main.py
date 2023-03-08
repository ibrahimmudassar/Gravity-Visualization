import math
import os
import re

import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import requests

location = "N11E077"
gravity_type = "full"  # res or full

reg = re.search(r"(.)(\d+)(.)(\d+)", location)

capturing = reg.groups()

lon = int(capturing[1])
lat = int(capturing[3])

lon_folder = divmod(lon, 30)
lat_folder = divmod(lat, 30)

folder = str(capturing[0]) + str(lon_folder[0]*30).zfill(2) + \
    str(capturing[2]) + str(lat_folder[0]*30).zfill(3)

prefix = "https://ddfe.curtin.edu.au/models/SRTM2gravity2018/data/"
verbose_gravity_type = "FullScaleGravity/" if gravity_type == "full" else "ResidualGravity/"

link = prefix + verbose_gravity_type + folder + \
    "/" + location + "_" + gravity_type + ".bin"

print(link)

filename = link.split("/")[-1]
r = requests.get(link, allow_redirects=True)
open(filename, 'wb').write(r.content)

binarydata = np.fromfile(filename, dtype='>i4')

binarydata = [i / 10_000_000 for i in binarydata]  # 0.01 mGal to m/s^2

square = int(math.sqrt(len(binarydata)))

longitude_label = [i/square + lon for i in range(square)]
latitude_label = [i/square + lat for i in range(square)]


# Taking the 1d array and turning it into 2d square
d2 = np.reshape(binarydata, (square, square))
d2 = np.rot90(d2)
d2 = np.flipud(d2)  # changing the matrix to graph how it should look


fig = px.imshow(d2,
                color_continuous_scale='Rainbow',
                origin="lower",
                labels=dict(x="Longitude [deg]", y="Latitude [deg]",
                            color=verbose_gravity_type + " [in m/s^2]"),
                x=longitude_label,
                y=latitude_label)
# title alignment
fig.update_layout(title_text=location + " " +
                  verbose_gravity_type + " [in m/s^2]")

fig.show()

fig = go.Figure(data=[go.Surface(x=latitude_label,
                y=longitude_label, z=d2, colorscale='Rainbow')])
fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))
fig.update_layout(title=location + " " + verbose_gravity_type + " [in m/s^2]",
                  scene=dict(
                      xaxis_title='Longitude [in deg]',
                      yaxis_title='Latitude [in deg]'),)

# Attribution
fig.add_annotation(text="By: Ibrahim Mudassar",
                   xref="paper", yref="paper",
                   x=1, y=-0.04,
                   showarrow=False,
                   align="center",
                   font=dict(size=15))

fig.show()
fig.write_html("filename.html")

os.remove(filename)
