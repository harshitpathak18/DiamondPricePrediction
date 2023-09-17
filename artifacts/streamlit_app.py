import streamlit as st
from src.pipelines.prediction_pipeline import CustomData,PredictPipeline


st.title("Diamond Price Prediction")

col1,col2,col3=st.columns(3)

with col1:
    carat=st.number_input(label="Carat")
    depth=st.number_input(label="Depth")
    table=st.number_input(label="table")
with col2:
    x=st.number_input(label="x")
    y=st.number_input(label="y")
    z=st.number_input(label="z")

with col3:
    cut=st.selectbox(label="Select Cut type",options=['Fair','Good','Very Good','Premium','Ideal'])
    color=st.selectbox(label="Select Color",options=['D','E','F','G','H','I','J'])
    clarity=st.selectbox(label="Select Clarity",options=['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF'])


data=CustomData(
    carat=carat,
    depth=depth,
    table=table,
    x=x,
    y=y,
    z=z,
    cut=cut,
    color=color,
    clarity=clarity
)

if st.button("Predict"):
    final_new_data=data.get_data_as_dataframe()
    predict_pipeline=PredictPipeline()
    pred=predict_pipeline.predict(final_new_data)

    results=round(pred[0])

    st.subheader(f"Predicted Price for diamond is - ${results}")