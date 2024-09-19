import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
import pandas as pd
from matplotlib import colormaps
import matplotlib as mpl
import requests
import scipy as sp

import urllib.request
from PIL import Image
# from bokeh.plotting import figure
#from bokeh.transform import linear_cmap, factor_cmap
#from bokeh.palettes import Bokeh

# page urls
url_home = "https://data-vis-101.streamlit.app/"
url_audience = "https://key-data-vis-requirements-audience.streamlit.app/"
url_story = "https://key-data-vis-requirements-story.streamlit.app/"
url_encoding = "https://key-data-vis-requirements-encoding.streamlit.app/"
url_composition = "https://key-data-vis-requirements-composition.streamlit.app/"
url_simplify = "https://key-data-vis-requirements-simplify.streamlit.app/"

urls = [url_home, url_audience, url_story, url_encoding, url_composition, url_simplify]

home_title = "0. Home"
audience_title = "1. Audience"
story_title = "2. Story"
encoding_title = "3. Encoding"
composition_title = "4. Composition"
simplify_title = "5. Simplify"

titles = [home_title, audience_title , story_title, encoding_title, composition_title, simplify_title]

# def click_button(url, text):
#      st.markdown(f'<a style="word-wrap:break-word;color:#ea388f;font-size:20px;font-style:bold; width: fit-content; border-style: none;padding:6px;text-decoration: none;border-width:2px;" href={url} target="_self">{text}</a>', unsafe_allow_html=True)

def click_button(url, text):
     st.markdown(f'<a href={url} target="_self">{text}</a>', unsafe_allow_html=True)

def pink_button(url, text):
     st.markdown(f'<a style="word-wrap:break-word;color:#ea388f;font-size:20px;font-style:bold; width: fit-content; border-style: solid;border-radius:10px;padding:6px;text-decoration: none;border-width:2px;text-align: center;" href={url} target="_self">{text}</a>', unsafe_allow_html=True)


def nav_bar(urls, titles):
    with st.popover("Table of contents", use_container_width=True):
        click_button(urls[0], titles[0])
        click_button(urls[1], titles[1])
        click_button(urls[2], titles[2])
        click_button(urls[3], titles[3])
        click_button(urls[4], titles[4])
        click_button(urls[5], titles[5])




@st.cache_data
def load_image_from_github(url):

    img = np.array(Image.open(requests.get(url, stream=True).raw))
    return img




my_pall ={'orange': '#e66101',
'pink': '#CA054D',
'blue': '#1B98E0',
'green':'#A4D4B4',
'purple': '#5e3c99', }

# data analysis
penguins = sns.load_dataset("penguins").dropna() 
Penguins = penguins.rename(columns={"species": "Species",
                                    "island": "Island",
                                    "bill_length_mm": "Bill length (mm)",
                                    "bill_depth_mm": "Bill depth (mm)",
                                    "flipper_length_mm": "Flipper length (mm)",
                                    "body_mass_g": "Body mass (g)",
                                    "sex":"Sex"
                                    })
# colour maps
# peng_cmap = factor_cmap(penguins, palette=Bokeh, factors=sorted(penguins.species.unique()))

# building data for ternary plot


locat = ["Locality #01B-32", "Locality #01B-34", "Locality #02C-01"]
local_no = np.random.choice(locat, 200)
local_var = np.zeros(200)
local_var [local_no == "Locality #01B-32"] = 1.3
local_var [local_no == "Locality #01B-34"] = -1.2

Qm_raw = 3.5 * np.random.randn(200) + 5
Qm_raw = Qm_raw + local_var
Qm_raw [Qm_raw <0] = 1.3
F_raw = 1.5 * np.random.randn(200) + 3
F_raw [F_raw <0] = 0.5
Lt_raw = 0.7 * np.random.randn(200) + 2
Lt_raw = Lt_raw - local_var
Lt_raw[Lt_raw <0] = 0.1



total_val = Qm_raw + F_raw + Lt_raw
norm_factor = 100/total_val

Qm = Qm_raw * norm_factor
F = F_raw * norm_factor
Lt = Lt_raw * norm_factor



geo_data = {"Qm":Qm,
            "F":F,
            "Lt":Lt,
            "Locality Number": local_no}

geo_df = pd.DataFrame.from_dict(geo_data)


st.title('5 Concepts for Data Visualisation')

intro_text = """
This website introduces five key concepts to help you build better research data visualisations.
These are not the *only* rules, or the *only* way to approach building a robust and reproducible
graphical research output, but should help you to create visualisations in a methodical way.
"""

st.write(intro_text)

col1, col2 = st.columns(2)

pub_refs = """
# Sources and inspiration

A number of fantastic articles went into this resource. Please read these works: the content shared here is a much-abridged, simplified, shortened version of the content shared in the articles below.


#### Bibliography

Berinato, Scott. 2016. “Visualizations That Really Work.” Harvard Business Review, June 1, 2016. https://hbr.org/2016/06/visualizations-that-really-work.

Franconeri, Steven L., Lace M. Padilla, Priti Shah, Jeffrey M. Zacks, and Jessica Hullman. 2021. “The Science of Visual Data Communication: What Works.” Psychological Science in the Public Interest: A Journal of the American Psychological Society 22 (3): 110–61.

Kelleher, Christa, and Thorsten Wagener. 2011. “Ten Guidelines for Effective Data Visualization in Scientific Publications.” Environmental Modelling & Software: With Environment Data News 26 (6): 822–27.

Midway, Stephen R. 2020. “Principles of Effective Data Visualization.” Patterns (New York, N.Y.) 1 (9): 100141.

Rougier, Nicolas P., Michael Droettboom, and Philip E. Bourne. 2014. “Ten Simple Rules for Better Figures.” PLoS Computational Biology 10 (9): e1003833.


#### Other resources

- [Berkeley Library Data Visualisation library guide](https://guides.lib.berkeley.edu/data-visualization/about)
- [Tableau documentation: Visual Best Practices](https://help.tableau.com/current/blueprint/en-us/bp_visual_best_practices.htm)
- [from Data to Viz project](https://www.data-to-viz.com/)
- [Principles of Data Visualization workshop notes](https://ucdavisdatalab.github.io/workshop_data_viz_principles/)
- [What’s visual ‘encoding’ in data viz, and why is it important?](https://medium.com/@sophiewarnes/whats-visual-encoding-in-data-viz-and-why-is-it-important-7406bc88b4b4#:~:text=Encoding%20in%20data%20viz%20basically,trying%20to%20say%20or%20show.)
- [University of Utah visualization design lab](https://vdl.sci.utah.edu/)
"""

with col1:
    with st.popover("Publications and references behind this tool"):
        st.markdown(pub_refs)

package_references = """
#### matplotlib
![matplotlib logo](https://matplotlib.org/stable/_static/logo_dark.svg)

J. D. Hunter, "Matplotlib: A 2D Graphics Environment", Computing in Science & Engineering, vol. 9, no. 3, pp. 90-95, 2007.

#### seaborn

![seaborn logo](https://seaborn.pydata.org/_images/logo-wide-lightbg.svg)

Waskom, M. L., (2021). seaborn: statistical data visualization. Journal of Open Source Software, 6(60), 3021, https://doi.org/10.21105/joss.03021.

#### Plotly

![Plotly logo](https://plotly.com/all_static/images/graphing_library_dark.svg)

Plotly Technologies Inc. Collaborative data science. Montréal, QC, 2015. https://plot.ly.

#### Streamlit

![streamlit logo](https://docs.streamlit.io/logo.svg)

Streamlit documentation, https://docs.streamlit.io/ 

#### NumPy

![numpy logo](https://numpy.org/images/logo.svg)

Harris, C.R., Millman, K.J., van der Walt, S.J. et al. Array programming with NumPy. Nature 585, 357–362 (2020). DOI: 10.1038/s41586-020-2649-2.

### pandas

![pandas logo](https://pandas.pydata.org/static/img/pandas.svg)

Data structures for statistical computing in python, McKinney, Proceedings of the 9th Python in Science Conference, Volume 445, 2010.
"""

with col2:
    with st.popover("Python packages and datasets used"):
        st.header("Python packages")
        st.markdown(package_references)
        st.header("Datasets")
        st.write("We use the `penguins` example dataset from the seaborn library. This can be browsed below:")
        st.dataframe(penguins)
        st.write("We also generated some random geological data to build a QFL ternary plot. This will regenerate when you reload the page, but will look something similar to this:")
        st.dataframe(geo_df)

st.subheader("The five themes to keep in mind include:")
st.subheader("Audience | Story | Encoding | Composition | Simplify")
nav_bar(urls, titles)

st.text("")
st.text("")

st.write("Use the contents menu above to start exploring.")

st.write("This webapp was developed by as part of the course materials for the",
"[*SWD7: Software development in Python*](https://arc.leeds.ac.uk/training/courses/swd7/) course run by the [Research Computing Team](https://arc.leeds.ac.uk/about/team/) at the University of Leeds.")
st.write("Find out more about [Research Computing](https://arc.leeds.ac.uk/) at Leeds.")

st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.text("")
st.divider()

st.write(r"$\textsf{\scriptsize Authored by Dr Maeve Murphy Quinlan, University of Leeds Research Computing Team © Copyright 2024}$")
st.write("[App home page](https://data-vis-101.streamlit.app/) | [Research Computing Team](https://arc.leeds.ac.uk/about/team/) | [Research Computing Website](https://arc.leeds.ac.uk/)")
