import streamlit as st


st.title('Basic Python Project Structure')

st.write("This webapp creates customised code snippets to help you set up a Python package project.",
"First, look through the **Picking a project name** tab and decide on a name for your Python package.",
"Then, go to the **Project details** tab and fill in information for your project.",
"Then, you can generate a sensible project folder structure using the `bash` scripts in the tab **Folder Structure**.",
"You can build your Python package using the generated `pyproject.toml` template in the **pyproject.toml** tab." )

with st.expander("Click here to learn more about balancing `env.yml` files for development and `pyproject.toml` files for distributing code"):
    st.subheader("Managing dependencies")


tablist = ["Audience", "Project details", "Folder structure", "pyproject.toml", " Build docs", "Citation"]

intro, tab0, tab1, tab2, tab3, tab4 = st.tabs(tablist)

with intro:
    st.header("Basic information on picking a project name.")
    st.markdown(
        """
        Picking a sensible project and package name can be challenging. There are a few rules to follow:
        - For your Python package name, stick to just lowercase letters and underscores. No spaces! No hyphens!
        - Make your repository name for the project the same as the package name, again all lowercase, but use hyphens instead of underscores. This is not a rule, but is a nice [convention](https://github.com/GoldenbergLab/naming-and-documentation-conventions)]
        - If you plan on publishing your package on PyPI (so you can install with pip), check that there are no packages with the same name!
        """
        )

with tab0:

    st.write("By default, we have used the MIT license in the `pyproject.toml` file; you can change this by swapping to one of the other common licenses [here](https://pypi.org/classifiers/) or by instead including a license file in your repository.")

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
    "[*SWD3: Software development in Python*](https://arc.leeds.ac.uk/training/courses/swd3/) course run by the [Research Computing Team](https://arc.leeds.ac.uk/about/team/) at the University of Leeds.")
    st.write("Find out more about [Research Computing](https://arc.leeds.ac.uk/) at Leeds.")
    st.write("You can also get in contact with me directly by leaving a message [here](https://murphyqm.github.io/murphyqm/).")
