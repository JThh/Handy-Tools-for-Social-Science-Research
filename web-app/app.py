import streamlit as st

st.set_page_config(layout="wide")

st.title("Handy Tools for Social Science Research")
st.markdown("_Initated by Jiatong Han affiliated with NUS LKYSPP_")

st.sidebar.header("Dashboard")

with st.sidebar.expander("Notes"):
    st.markdown(
        """
                      This web interface is under active development and is meant for automated data processing and analysis. The source code is openly shared under Apache license.
                      """
    )
st.sidebar.markdown(
    """_Version 0.1.0 | Jan 7th, 2023_""".format(unsafe_allow_html=True)
)

with st.expander("File Conversion Utility"):
    st.write('Please enable pop-up to allow downloads')
    x
    pass

with st.expander("Online Scraper"):

    pass

with st.expander("Sentiment Analysis Tool"):
    st.markdown(
        "Under development. Look out for more updates on [repo](https://github.com/JThh/Handy-Tools-for-Social-Science-Research)"
    ) 
    pass