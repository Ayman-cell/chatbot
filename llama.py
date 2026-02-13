"""
🤖 Assistant IA Multilingue - Cerebras Llama 3.1-8B
Chatbot conversationnel basé sur l'IA générative
"""

import streamlit as st
import os
import json
from datetime import datetime
import uuid
from langchain_cerebras import ChatCerebras

# ========== CONFIGURATION DE LA PAGE ==========
st.set_page_config(
    page_title="Assistant IA - Cerebras",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========== CONFIGURATION DES DOSSIERS ==========
CONVERSATIONS_DIR = "conversations"
if not os.path.exists(CONVERSATIONS_DIR):
    os.makedirs(CONVERSATIONS_DIR)

# ========== CONFIGURATION DE L'API CEREBRAS ==========
try:
    CEREBRAS_API_KEY = st.secrets["CEREBRAS_API_KEY"]
except KeyError:
    st.error("❌ CEREBRAS_API_KEY n'est pas configurée!")
    st.info("Allez dans: Settings → Secrets → Ajoutez: CEREBRAS_API_KEY = 'votre-clé'")
    st.stop()

os.environ["CEREBRAS_API_KEY"] = CEREBRAS_API_KEY

# ========== INTERFACE PRINCIPALE ==========
st.title("🤖 Assistant IA Multilingue")
st.markdown("**Basé sur Cerebras Llama 3.1-8B**")

# ========== INITIALISER LE LLM ==========
@st.cache_resource
def get_llm():
    """Initialiser le modèle LLM Cerebras"""
    return ChatCerebras(
        api_key=CEREBRAS_API_KEY,
        model="llama-3.1-8b",
        temperature=0.7
    )

try:
    llm = get_llm()
except Exception as e:
    st.error(f"❌ Erreur LLM: {e}")
    st.stop()

# ========== ÉTAT DE SESSION ==========
if "messages" not in st.session_state:
    st.session_state.messages = []
if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = str(uuid.uuid4())

# ========== AFFICHER L'HISTORIQUE ==========
st.subheader("💬 Conversation")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# ========== ENTRÉE UTILISATEUR ==========
user_input = st.chat_input("Écrivez votre question ou message...")

if user_input:
    # Ajouter le message utilisateur
    st.session_state.messages.append({
        "role": "user",
        "content": user_input,
        "timestamp": datetime.now().isoformat()
    })
    
    # Afficher le message utilisateur
    with st.chat_message("user"):
        st.write(user_input)
    
    # Générer une réponse
    with st.chat_message("assistant"):
        with st.spinner("⏳ L'IA réfléchit..."):
            try:
                # Construire l'historique
                history = ""
                for msg in st.session_state.messages[:-1]:
                    role_label = "User" if msg["role"] == "user" else "Assistant"
                    history += f"{role_label}: {msg['content']}\n"
                
                # Construire le prompt
                prompt = f"""{history}User: {user_input}
Assistant: """
                
                # Appeler le LLM
                response = llm.invoke(prompt)
                
                # Extraire la réponse
                if hasattr(response, 'content'):
                    answer = response.content
                else:
                    answer = str(response)
                
                # Afficher la réponse
                st.write(answer)
                
                # Sauvegarder la réponse
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": answer,
                    "timestamp": datetime.now().isoformat()
                })
                
            except Exception as e:
                st.error(f"❌ Erreur: {str(e)}")
                st.stop()

# ========== BOUTONS D'ACTION ==========
if st.session_state.messages:
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("💾 Sauvegarder"):
            conv_data = {
                "id": st.session_state.conversation_id,
                "timestamp": datetime.now().isoformat(),
                "messages": st.session_state.messages
            }
            filepath = os.path.join(
                CONVERSATIONS_DIR,
                f"conv_{st.session_state.conversation_id}.json"
            )
            with open(filepath, "w", encoding="utf-8") as f:
                json.dump(conv_data, f, ensure_ascii=False, indent=2)
            st.success("✅ Sauvegardé!")
    
    with col2:
        if st.button("🗑️ Effacer"):
            st.session_state.messages = []
            st.rerun()
    
    with col3:
        if st.button("🔄 Nouveau"):
            st.session_state.conversation_id = str(uuid.uuid4())
            st.session_state.messages = []
            st.rerun()

# ========== PANNEAU LATÉRAL ==========
with st.sidebar:
    st.title("ℹ️ Information")
    
    st.metric("Messages", len(st.session_state.messages))
    st.metric("Conversation ID", st.session_state.conversation_id[:8])
    
    st.divider()
    
    st.subheader("📂 Conversations")
    if os.path.exists(CONVERSATIONS_DIR):
        conv_files = [f for f in os.listdir(CONVERSATIONS_DIR) if f.endswith(".json")]
        
        if conv_files:
            selected = st.selectbox(
                "Charger",
                conv_files,
                format_func=lambda x: x.replace("conv_", "").replace(".json", "")[:8]
            )
            
            if selected:
                with open(os.path.join(CONVERSATIONS_DIR, selected), "r") as f:
                    data = json.load(f)
                    st.session_state.messages = data.get("messages", [])
                    st.session_state.conversation_id = data.get("id")
                    st.success("✅ Chargé!")
                    st.rerun()
        else:
            st.info("Aucune conversation")
    
    st.divider()
    st.caption("© 2026 Cerebras AI | Streamlit Cloud")
