import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(layout="centered", page_icon="🎓", page_title="Diploma Generator")
st.title("🎓 Resume Generator")

left, right = st.columns(2)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")


left.write("Fill in the data:")
form = left.form("template_form")
name = form.text_input("Name")
mail= form.text_input("Email")
git= form.text_input("Github URL")
li = form.text_input("Linkedin URl")
submit = form.form_submit_button("Generate PDF")

if submit:
    html = template.render(
        name=name,
        mail=mail,
        git=git,
        li=li,
        date=date.today().strftime("%B %d, %Y"),
    )

    pdf = pdfkit.from_string(html, False)
    st.balloons()

    right.success("🎉 Your resume was generated!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    right.download_button(
        "⬇️ Download PDF",
        data=pdf,
        file_name="resume.pdf",
        mime="application/octet-stream",
    )
