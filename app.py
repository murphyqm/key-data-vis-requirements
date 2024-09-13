import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from bokeh.plotting import figure
from bokeh.transform import linear_cmap, factor_cmap
from bokeh.palettes import Bokeh

# data analysis
penguins = sns.load_dataset("penguins")

# colour maps
# peng_cmap = factor_cmap(penguins, palette=Bokeh, factors=sorted(penguins.species.unique()))

st.title('5 Concepts for Data Visualisation')

intro_text = """
This website introduces five key concepts to help you build better research data visualisations.
These are not the *only* rules, or the *only* way to approach building a robust and reproducible
graphical research output, but should help you to create visualisaitions in a methodical way.
"""

st.write(intro_text)

col1, col2 = st.columns(2)

with col1:
    with st.popover("Publications and references behind this tool"):
        st.subheader("Managing dependencies")

package_references = """
#### seaborn

![seaborn logo](https://seaborn.pydata.org/_images/logo-wide-lightbg.svg)

Waskom, M. L., (2021). seaborn: statistical data visualization. Journal of Open Source Software, 6(60), 3021, https://doi.org/10.21105/joss.03021.


"""

with col2:
    with st.popover("Python packages and datasets used"):
        st.header("Python packages")
        st.markdown(package_references)
        st.header("Datasets")
        st.write("We use the `penguins` example dataset from the seaborn library. This can be browsed below:")
        st.dataframe(penguins)




# st.markdown("""
# <style>

# 	.stTabs [data-baseweb="tab-list"] {
# 		gap: 2px;
#     }

# 	.stTabs [data-baseweb="tab"] {
# 		height: 50px;
#         white-space: pre-wrap;
# 		border-radius: 4px 4px 4px 4px;
# 		gap: 5px;
# 		padding-top: 10px;
# 		padding-bottom: 10px;
#         font-size:4rem;
#     }

# 	.stTabs [aria-selected="true"] {
#   		background-color: #FFFFFF;
# 	}

# </style>""", unsafe_allow_html=True)

tablist = [r"$\; \textsf{1.} \; \textsf{\Large Audience}\; \;$", r"$\; \textsf{2.} \; \textsf{\Large Story}\; \;$", r"$\; \textsf{3.} \; \textsf{\Large Encoding}\; \;$", r"$\; \textsf{4.} \; \textsf{\Large Composition}\; \;$", r"$\; \textsf{5.} \; \textsf{\Large Simplify}\; \;$"]

tab0, tab1, tab2, tab3, tab4 = st.tabs(tablist)

md_0_a = """
Creating plots and graphs for yourself can be a fantastic way of quickly evaluating datasets, discovering patterns, and validating model output.

Exploratory data visualisation for yourself might be...

- Messy! Labels might be all lowercase, with underscores instead of spaces, and plots might use all default settings for colours.
- Informal
- Embedded in notebooks surrounded by exploratory notes
- Interactive
"""

with tab0:

    st.header("Who is your audience?")
    with st.expander("a. Yourself!"):
        st.markdown(md_0_a )
        st.subheader("Interaction can aid exploration")
        st.scatter_chart(penguins, x="bill_length_mm", y="bill_depth_mm", color="species", size="island")
        st.write("Using size as a method of encoding unordered categorical data isn't best practise,",
                 "but it's ok to be a little sloppy when developing plots only for yourself.")

    with st.expander("b. Your research group or collaborators"):
        st.subheader("Managing dependencies")
    with st.expander("c. Specialists in your domain"):
        st.subheader("Managing dependencies")
    with st.expander("d. Researchers outside your domain"):
        st.subheader("Managing dependencies")
    with st.expander("f. General public"):
        st.subheader("Managing dependencies")

    st.header("What's the context?")

    st.header("What's the medium?")

with tab1:

    st.write(f'To recreate the structure above, `cd` into your project directory (`) and run the following commands (by copying and pasting the block below into the terminal):')


with tab2:
    
    st.write("The previous step created a file and folder layout for your project. Open up the new `pyproject.toml` file and paste the following code template into it:")


with tab3:
    st.write("[Mkdocs](https://www.mkdocs.org/) is a simple and quick documentation building library that works well with GitHub and GitHub pages.")


with tab4:

    st.write("Once your repository contains a citation file, you can use this with the [GitHub-Zenodo integration](https://docs.github.com/en/repositories/archiving-a-github-repository/referencing-and-citing-content) when generating DOIs for your release.")


with st.sidebar:

    st.header("About")
    st.write("This webapp was developed by [murphyqm](https://github.com/murphyqm) as part of the course materials for the",
    "[*SWD7: Software development in Python*](https://arc.leeds.ac.uk/training/courses/swd7/) course run by the [Research Computing Team](https://arc.leeds.ac.uk/about/team/) at the University of Leeds.")
    st.write("Find out more about [Research Computing](https://arc.leeds.ac.uk/) at Leeds.")
    st.write("You can also get in contact with me directly by leaving a message [here](https://murphyqm.github.io/murphyqm/).")
