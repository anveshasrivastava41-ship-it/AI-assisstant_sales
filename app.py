import streamlit as st
import json
import time
def mock_lead_capture(name, email, platform):
    print(f"Lead captured successfully: {name}, {email}, {platform}")

st.set_page_config(page_title="AI Sales Assistant", page_icon="🤖")

# Header
st.title("🤖 AI Sales Assistant")
st.caption("Ask about pricing, features, or request a demo")

# Initialize session
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "lead_stage" not in st.session_state:
    st.session_state.lead_stage = 0

if "lead_data" not in st.session_state:
    st.session_state.lead_data = {}

with open("data/knowledge.json") as f:
    knowledge = json.load(f)


# Show chat messages (bubble style)
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.write(msg)

# Chat input (modern UI)
user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))

    user_lower = user_input.lower()

    # Intent logic
    if "hi" in user_lower or "hello" in user_lower:
        response = "Hello! 👋 I can help you with pricing, features, or getting started."

    elif any(word in user_lower for word in ["price", "pricing", "cost"]):
        pricing = knowledge["pricing"]

        response = f"""💰 
        Pricing Plans:

        Basic Plan:
        {pricing['basic']}

        Pro Plan:
        {pricing['pro']}

        👉 Would you like a demo of the Pro plan?
        """
    elif "refund" in user_lower:
        response = knowledge["policies"]["refund"]


    elif "feature" in user_lower:
        response = "We offer AI-powered video editing, captions, 4K export, and automation tools."

    elif any(word in user_lower for word in ["buy", "demo", "yes"]):
        response = "Awesome 🚀 Let's get you started!"
        st.session_state.lead_stage = 1

    else:
        response = "Ask me about pricing, features, or getting started."

    st.session_state.chat_history.append(("assistant", response))

    st.rerun()

# Lead capture UI (clean card style)
if st.session_state.lead_stage > 0:
    st.divider()
    st.subheader("🚀 Get Started")

if st.session_state.lead_stage == 1:
    name = st.text_input("Your Name", key="name_input")

    if st.button("Next"):
        if name:
            st.session_state.lead_data["name"] = name
            st.session_state.lead_stage = 2
            st.rerun()

elif st.session_state.lead_stage == 2:
    email = st.text_input("Your Email", key="email_input")

    if st.button("Next"):
        if email:
            st.session_state.lead_data["email"] = email
            st.session_state.lead_stage = 3
            st.rerun()

elif st.session_state.lead_stage == 3:
    platform = st.text_input("Platform (YouTube / Instagram)", key="platform_input")

    if st.button("Submit"):
        if platform:
            st.session_state.lead_data["platform"] = platform

            mock_lead_capture(
               st.session_state.lead_data["name"],
               st.session_state.lead_data["email"],
               st.session_state.lead_data["platform"]
        )

        st.success("🎉 Lead captured successfully!")
        st.write(st.session_state.lead_data)
        st.toast("Lead sent to backend ✅")
        time.sleep(1)

        st.session_state.lead_stage = 0
        st.rerun()
        st.toast("Lead sent to backend ✅")