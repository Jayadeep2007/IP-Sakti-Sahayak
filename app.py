import streamlit as st

# Page configuration
st.set_page_config(
    page_title="IP-SAKTI Sahayak",
    page_icon="⚖️",
    layout="wide"
)

# Main heading
st.title("⚖️ IP-SAKTI Sahayak")

st.subheader(
    "AI Regulatory & Knowledge Assistant"
)

st.write(
    "Your intelligent assistant for "
    "Intellectual Property information."
)


# Navigation
st.sidebar.title("IP-SAKTI Navigation")

page = st.sidebar.radio(
    "Select a page",
    [
        "Home",
        "AI Assistant",
        "About"
    ]
)

# Home page
if page == "Home":

    st.header("Welcome to IP-SAKTI")

    st.write(
        "Explore intellectual property information "
        "with the help of AI."
    )

    st.info(
        "Ask questions about patents, trademarks "
        "and copyrights."
    )

# AI Assistant page
elif page == "AI Assistant":

    st.header("AI Knowledge Assistant")

    question = st.text_input(
        "Enter your IP-related question:"
    )

    if st.button("Ask IP-SAKTI"):

        if question.strip():

            st.info(
                "RAG and AI functionality "
                "will be integrated in the next phase."
            )

        else:

            st.warning(
                "Please enter a question."
            )

# About page
elif page == "About":

    st.header("About Our Project")

    st.write(
        """
        IP-SAKTI Sahayak is an AI-powered
        Regulatory and Knowledge Assistant.

        It uses:

        - Retrieval-Augmented Generation (RAG)
        - Agentic AI
        - Prompt Engineering
        - Streamlit
        - Web Development
        """
    )

    st.caption(
        "CDS208 - Emerging Tools and Applications"
    )
