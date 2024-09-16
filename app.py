import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
# from bokeh.plotting import figure
#from bokeh.transform import linear_cmap, factor_cmap
#from bokeh.palettes import Bokeh

# data analysis
penguins = sns.load_dataset("penguins").dropna() 

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

### Exploratory data visualisation

This is data visualisation with the intention of discovering something, as opposed
to displaying or proving something. The plots generated during the exploratory
or investigation stage will likely never make it into a publication or other
output: an awful lot of plots generated won't show anything interesting.
That's ok! That's the point! Because of this, generating these plots needs to
be rapid.

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
        st.write("Interactivity is often not necessary outside of specific applications,",
                 "and can be overused to hide other issues with a visualisation (such as not knowing the message or story it is supposed to tell),",
                 "but in the case of exploratory data visualisation it's ok",
                 "not to know that the message or story is yet!")
        st.write("Quickly-built interactive visualisations using libraries such as `plotly` or `bokeh` can be a useful step in figuring out whether your",
                 "plot should highlight the overall, large-scale patterns in the data,",
                 "or if it should zoom in on the details.")
        st.scatter_chart(penguins, x="bill_length_mm", y="bill_depth_mm",
                         color="species", size="island")
        st.write("*Caption: Adelie penguins resident on all three islands; others restricted to single island. Check if any correlation between Adelie stats and location...*")
        
        st.write("Using size as a method of encoding unordered categorical data (as in the figure above) isn't best practise,",
                 "but it's ok to be a little sloppy when developing plots only for yourself.", 
                 "This figure lets you explore the clustering of bill size with species,",
                 "but also shows the distribution of different species on different islands if you zoom in and hover over the data.",
                 "This plot wouldn't be the best way of showing either of those features, but it's useful to help us spot these trends.")
        st.scatter_chart(penguins.loc[penguins['species'] == "Adelie"], x="flipper_length_mm", y="body_mass_g",
                         color="island",)
        st.write("*Caption: no obvious correlation between physical characteristics and location; can do some exploratory stats.*")
        st.subheader("Captions")
        st.write("Captions do not have to be as formal when building an exploratory plot for yourself; however it's still useful to tag any figures with your notes. This could be by adding some markdown text in a Jupyter notebook after the figure (shown above in italics), or by adding info to the title. It's easy to forget what info you have gleaned from a particular plot, and noting it down like this can help save you time repeating yourself.")

    with st.expander("b. Your research group or collaborators"):
        st.subheader("Informality depends on context")
        st.write("For quick meetings, exploratory plots without much formatting might be sufficient;",
                 "however, bear in mind whether you are meeting in-person to talk through the plot",
                 "or whether the work needs to be able to stand on its own alongside an explanatory note.")
        st.write("While the plots might still be somewhat exploratory, and you may want to maintain some interaction for discussion, it's likely you'll want to have a better idea of the message or key result behind the plot. We'll discuss this more in **Section 2: Story**")
        st.write("While in a publication, you would pick one plot that best highlights a particular pattern or feature, when putting together figures for discussion it can be useful to provide a few different but similar views to help discover the most useful way of presenting the data.")
        fig = px.histogram(penguins, x="bill_length_mm", y="bill_depth_mm",
                           color="species",marginal="box")
        st.plotly_chart(fig, use_container_width=True)
        fig2 = px.scatter(penguins, x="bill_length_mm", y="bill_depth_mm",
                          color="species", marginal_y="violin", marginal_x="box",
                          trendline="ols", )
        st.plotly_chart(fig2, use_container_width=True,)
        st.subheader("Captions")
        st.write("Again, captions are really useful for giving your collaorators a peek inside your thought process.",
                 "They can be conversational and open ended, but should convey what message you think might be lurking in the data.")
        
    with st.expander("c. Specialists in your domain"):
        st.subheader("Managing dependencies")
    with st.expander("d. Researchers outside your domain"):
        st.subheader("Managing dependencies")
    with st.expander("f. General public"):
        st.write("More illustrative or infographic-style plots are often popular",
                 "when designing data visualisation for the general public;",
                 "however, more quant-style plots are also often needed.",
                 "In general, it is useful to label your data clearly and avoid",
                 "unexplained scientific jargon&mdash;this is true of **all** data vis,",
                 "but becomes especially necessary when presenting to non-technical audiences.")
        st.write("In general, all the follow-on rules and guidelines we discuss in later sections are more important for figures created for the general public: other, more specialist audiences will be more forgiving of bad design choices as they have been trained to read scientific visualisations.")
        fig3 = px.scatter(penguins, x="bill_length_mm", y="bill_depth_mm",
                          color="species",hover_data=['sex', "island"],
                          title="Different penguin species have differently shaped bills",
                          labels={
                              "bill_length_mm": "Bill length (mm)",
                              "bill_depth_mm": "Bill depth (mm)",
                              "species": "Penguin Species",
                              "island": "Location (island name)",
                              "sex": "Sex"
                          })
        st.plotly_chart(fig3, use_container_width=True,)
        st.write("Descriptive titles carrying the main message of the plot can be very useful in highlighting the story being told by the data.")
        fig4 = px.scatter(penguins, x="flipper_length_mm", y="body_mass_g",
                          hover_data=["species", "island", "sex"],
                          title="Different penguin species have differently shaped bills",
                          labels={
                              "flipper_length_mm": "Flipper length (mm)",
                              "body_mass_g": "Body mass (g)",
                              "species": "Penguin Species",
                              "island": "Location (island name)",
                              "sex": "Sex"
                          },
                          trendline="ols",)
        st.plotly_chart(fig4, use_container_width=True,)

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
