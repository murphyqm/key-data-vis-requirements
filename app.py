import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
import pandas as pd
# from bokeh.plotting import figure
#from bokeh.transform import linear_cmap, factor_cmap
#from bokeh.palettes import Bokeh

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

Kelleher, Christa, and Thorsten Wagener. 2011. “Ten Guidelines for Effective Data Visualization in Scientific Publications.” Environmental Modelling & Software: With Environment Data News 26 (6): 822–27.

Midway, Stephen R. 2020. “Principles of Effective Data Visualization.” Patterns (New York, N.Y.) 1 (9): 100141.

Rougier, Nicolas P., Michael Droettboom, and Philip E. Bourne. 2014. “Ten Simple Rules for Better Figures.” PLoS Computational Biology 10 (9): e1003833.
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
        st.write("We also generated some random geological data to build a QFL ternary plot.")
        st.dataframe(geo_df)




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
audience_gen = """
- Is the figure for yourself or direct collaborators? This may be the case if you are quickly checking if results are expected, are pulling together some notes for a supervisory or team meeting, or have some questions for a collaborator about some recent results.

- Is the figure for a scientific publication and so for a broader audience who has technical knowledge but does not know the details of your work specifically?

- Are you presenting a talk or a poster at a conference where the audience are mainly experts in your niche field?

- Is your audience going to be undergraduate students where the aim is to convey a concept or method with your data as an example, instead of conveying your results specifically?

- Is you data visualisation being used in an outreach setting for the general public without any assumed research or field-specific knowledge?
"""

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

domain_specific_plots = """
Certain research areas will have niche, domain-specific plots, that will be easily understandable by people within that field but would look unusual or confusing to someone outside. These sort of plots which require specialist knowledge can be very useful in quickly imparting detailed information. For example, the ternary plot below used for determining the provenance of sedimentary samples will be immediately recognised by those working in geology or a related field.

"""

general_research_audience = """
Some useful questions to ask include:
- What are common scientific/research terms, and what might be terms only understood by researchers in your specific field?
- What are some common assumptions in your field that might not be true of other domain areas, and will require explanation?
"""

gen_pop_info = """
Some useful questions to ask yourself include:
- Do we need to convey detailed number or can we focus instead on trends?
- How busy are our plots? Can we strip them down and split data up into different plots?
- How much information are we trying to deliver in each plot? Try to stick to one key message or piece of information.
"""

context_medium = """
- Is it going to be quickly viewed on a large projector screen as part of a presentation, with you talking over it?
    - Possibly reveal features slowly, adding data as you explain
    - Large font size and thick lines/large markers
    - Should be rapidly digestible
    - Your spoken word can act as a caption to explain the plot to the audience
- Will it be part of a published research article?
    - Can expect people to spend a little longer reading it and absorbing the content
    - Can include a lot of detail in the caption
    - Will need to meet very specific dimension, font size and resolution specifications
- Will it be presented on a poster?
    - Make it large enough to be comfortably read from a distance
    - Be careful defining size and resolution to ensure it can be printed in large format

Depending on the context, you may need to play around with features such as transparency and colour palette to ensure your graphic is legible.

"""

context_part2 = """
#### Create the same plot for different contexts

The `seaborn` library allows you to change the setting of an argument called `"context"`. This automatically scales the line thickness, marker size and font size of your figure to better suit the presentation medium. You might still need to tweak these individually, but this is a quick way to update your plot.
"""

with tab0:
    st.header("Why are you making a figure?")
    st.markdown(audience_gen)
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
        st.write("Again, captions are really useful for giving your collaborators a peek inside your thought process.",
                 "They can be conversational and open ended, but should convey what message you think might be lurking in the data.")
        
    with st.expander("c. Specialists in your domain"):
        st.subheader("Domain-specific plots")
        st.markdown(domain_specific_plots)
        fig5 = px.scatter_ternary(geo_df, a="Qm", b="F", c="Lt", color="Locality Number")
        st.plotly_chart(fig5, use_container_width=True,)
        st.write("*Caption: Quartz, feldspar and lithic fragments (QFL) ternary plot for sedimentary samples returned from three localities (locality number listed in legend, denoted by colour). Quartz, feldspar and lithic fragments have been point counted in thin section and normalised to 100 %. Please see the main text for a discussion of location in QFL space and likely provenance of samples in each location.*")
        st.subheader("Captions")
        st.write("Captions should be detailed and define every piece of visual information in the figure. A non-specialist should still be able to determine the main message of your plot after reading the caption, even if the layout of the plot is new to them.")
        
    with st.expander("d. Researchers outside your domain"):
        st.write("A more general research audience may require more hand-holding to digest niche or complex plots. This can be done by reducing the amount of information being conveyed in the plot, by incorporating helpful labels, or by creating multiple panels and splitting up the data.")
        st.markdown(general_research_audience)
    with st.expander("f. General public"):
        st.write("More illustrative or infographic-style plots are often popular",
                 "when designing data visualisation for the general public;",
                 "however, more quant-style plots are also often needed.",
                 "In general, it is useful to label your data clearly and avoid",
                 "unexplained scientific jargon&mdash;this is true of **all** data vis,",
                 "but becomes especially necessary when presenting to non-technical audiences.")
        st.write("In general, all the follow-on rules and guidelines we discuss in later sections are more important for figures created for the general public: other, more specialist audiences will be more forgiving of bad design choices as they have been trained to read scientific visualisations.")
        st.markdown(gen_pop_info)
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
        fig3.add_annotation(text="Stubby, short, deep bills", x=35, y=21.55, showarrow=False)
        fig3.add_annotation(text="Slender, long, shallow bills", x=54, y=13.5, showarrow=False)
        fig3.add_annotation(text="Large, long, deep bills", x=54, y=21.55, showarrow=False)
        st.plotly_chart(fig3, use_container_width=True,)
        st.write("*Caption: the shape (or aspect ratio) of a penguins bill (the bill depth times and bill length) is related to the species of penguin. You can see the three distinct clusters of aspect ratio, and how this correlates with species. Click on the species name in the legend to toggle if its included in the plot.*")
        st.write("Descriptive titles carrying the main message of the plot can be very useful in highlighting the story being told by the data.",
                 "Captions can expand on this further.",
                 "Text annotations can provide additional context. In the example above, a cartoon diagram of each bill morphology could be added in place of the text annotations.")
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
        st.write("*Caption: there is a relationship between penguin body mass and flipper length: heavier penguins are likely to have longer flippers; however, the relationship is not perfect with a lot of variation.*")

    st.header("What's the context and the medium?")
    with st.expander("Where will your visualisation be shown?"):
        st.markdown(context_medium)
    
    if "context" not in st.session_state:
        st.session_state.context = "paper"
        st.session_state.palette = "Set2"
        st.session_state.alpha = 0.7
    with st.expander("Different versions of the same plot"):
        st.markdown(context_part2)
        col1, col2, col3 = st.columns(3)
        with col1:
            st.radio(
                'Pick a plot `"context"`: ',
                key="context",
                options=["paper", "talk", "poster"]
            )
        with col2:
            st.radio(
                "Pick a colour palette: ",
                key="palette",
                options=["Set2", "pastel", "colorblind"]
            )
        
        with col3:
            st.radio(
                "Pick a marker transparency:",
                key="alpha",
                options=[1, 0.7, 0.5]
            )

        fig6 = plt.figure()
        with sns.axes_style("ticks"):
                sns.set_context(st.session_state.context)
                sns.set_palette(st.session_state.palette)
                ax = sns.scatterplot(data=Penguins, x="Body mass (g)", y="Flipper length (mm)", hue="Island", style="Sex", alpha=st.session_state.alpha)
                sns.despine()
                sns.move_legend(ax, "upper left", bbox_to_anchor=(1, 1))
        st.pyplot(fig6, use_container_width=True,)
    

story_01 = """
A figure can express an idea quickly, succinctly, and straightforwardly. However, it is important to know exactly what the message of the figure is, to avoid creating either pointless plots that don’t really tell much, or overly complex plots that try to tell far too much.

#### Diagram first

Try sketching out some ideas with pen and paper to explore how you might want to present the data. Exploratory data vis (discussed in the previous slide) is also useful for this.
- What's the result you want to showcase? Can you explain it in a single sentence?
- Do you need to show the **broad trends** or the **fine-grained details** to tell the story?
    - These should usually be separated; if both are relevant, split them into two separate plots
- What is the **simplest graph possible** that will communicate the meaning?

#### Collaborate and share

Share your plots from an early stage (perhaps even at the sketching-with-pen-and-paper stage) to see if your peers can quickly grasp the message you are hoping to convey. 

>You know your data and your research very well; the patterns you are trying to highlight might be very obvious to you when you look at your figure, but completely hidden to someone looking at it for the first time.


#### What sort of plots are even out there?

When trying to figure out what kind of plot wll best help to visualise your message, it's useful to remind yourself of what kind of plots even exist!
"""

plot_inspiration = """

#### Plotting library galleries and showcases

A great place to find out whats available and what you can achieve is to scroll through some of the well-curated example galleries and tutorials published alongside many of the popular Python plotting libraries.

Some notable examples include:

- [Example gallery: seaborn](https://seaborn.pydata.org/examples/index.html)
- [Plotly documentation](https://plotly.com/python/)
- [Bokeh gallery: Topic guide](https://docs.bokeh.org/en/latest/docs/gallery.html)

There are also some larger-scale collected galleries that include multiple libraries:
- [The Python Graph Gallery](https://python-graph-gallery.com/)
    - This gallery breaks up plots from a range of different libraries into topics such as distribution, correlation, ranking, evolution, and mapping

#### Articles on data visualisation

While not specifically sharing Python libraries, general articles discussing great data visualisation can be a useful place to discover new kinds of plots and to inspire yourself; these sorts of posts can often be found on [company blogs](https://visme.co/blog/best-data-visualizations/)
"""

with tab1:

    st.markdown(story_01)
    with st.expander("Finding plot inspiration"):
        st.markdown(plot_inspiration)


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
