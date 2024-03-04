import streamlit as st 
st.set_page_config(page_title='COCOMO MODEL',page_icon="🎵")

with st.container():
    st.title("COCOMO MODEL")
    st.subheader('Effort Estimation')
    st.text('Enter value to get the effort estimation')
    st.text_input(label='KLOC', value="0")
    st.radio(label='Mode',options=["Organic","Semi-detached","Embedded"])
    st.button(label='Estimation effort', use_container_width=True)
    st.subheader("Cost Estimation")
    st.text('Number of Person_months(PM):-')
    st.text('Number of person_Years(PY)')
