import streamlit as st

class Opportunity:
    def __init__(self, title, description, author, author_occupation, author_location, contact_email, contact_phone, organization, opportunity_type, fieldOfStudy):
        self.title = title
        self.description = description
        self.author = author
        self.author_occupation = author_occupation
        self.author_location = author_location
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.organization = organization
        self.opportunity_type = opportunity_type
        self.fieldOfStudy = fieldOfStudy

class OpportunityBoard:
    def __init__(self):
        self.opportunities = []

    def add_opportunity(self, opportunity: Opportunity):
        self.opportunities.append(opportunity)

    def get_all_opportunities(self):
        return self.opportunities

    def filter_opportunities(self, selected_type):
        if selected_type == "All":
            return self.opportunities
        return [opp for opp in self.opportunities if opp.opportunity_type == selected_type]

# Persist board across reruns
if "board" not in st.session_state:
    st.session_state.board = OpportunityBoard()

board = st.session_state.board

# Initialize app title
st.title("🎓 Network Board – Student Opportunities Platform")
st.write("Browse and post professional opportunities for students across different fields.")

with st.form("add_opportunity"):
    st.header("Post a New Opportunity")
    title = st.text_input("Title")
    description = st.text_area("Description")
    author = st.text_input("Author")
    author_occupation = st.text_input("Occupation")
    author_location = st.text_input("Location")
    contact_email = st.text_input("Contact Email")
    contact_phone = st.text_input("Contact Phone")
    organization = st.text_input("Organization")
    fieldOfStudy = st.text_input("Field of Study")
    opportunity_type = st.selectbox("Who you're looking for", ["Ambassador", "Intern", "Mentee", "Part-Time Employee", "Project Collaborator", "Research Assistant", "Shadow", "Volunteer", "Other"])
    submitted = st.form_submit_button("Post Opportunity")

    if submitted:
        new_opp = Opportunity(title, description, author, author_occupation, author_location, contact_email, contact_phone, organization, opportunity_type, fieldOfStudy)
        board.add_opportunity(new_opp)

st.subheader("Browse Opportunities")
field_filter = st.selectbox("Filter by Opportunity Type", ["All", "Ambassador", "Intern", "Mentee", "Part-Time Employee", "Project Collaborator", "Research Assistant", "Shadow", "Volunteer", "Other"])
filtered_opps = board.filter_opportunities(field_filter)

for opp in filtered_opps:
    st.markdown(
        f"""
        <div style="
            border: 1px solid #ccc;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
        ">
            <h3>{opp.title}</h3>
            <p><strong>From:</strong> {opp.author}, {opp.author_occupation} at {opp.organization}</p>
            <p><strong>Contact:</strong> {opp.contact_email} – {opp.contact_phone}</p>
            <p>{opp.description}</p>
            <p><strong>Field(s) of Study:</strong> {opp.fieldOfStudy}</p>
            <p><strong>Location:</strong> {opp.author_location}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
