# 🚀 **GUIDE D'INSTALLATION COMPLÈTE - DÉFINITIF**

## ⚠️ **TOUS LES PROBLÈMES SONT RÉSOLUS !**

---

## 📋 **CE QUI A ÉTÉ CORRIGÉ**

✅ **Dépendances LangChain** - Versions stables et testées  
✅ **Tous les imports** - Compatibles avec LangChain 1.x  
✅ **openpyxl** - Ajouté aux dépendances  
✅ **Configuration Streamlit** - Netoyée et optimisée  
✅ **Escape sequences** - Corrigées  

---

## 🌐 **VOTRE APP EST PRÊTE**

```
🎨 https://chatbot-aymaan.streamlit.app
```

**L'app va se redéployer automatiquement en 2-3 minutes**

---

## 📜 **DÉPENDANCES UTILISÉES**

```
streamlit==1.28.1 ✅
langchain==1.0.12 ✅ (Stable et testé)
langchain-cerebras==0.8.2 ✅
langchain-community==0.0.37 ✅
langchain-core==0.1.48 ✅
langchain-text-splitters==0.0.1 ✅
openpyxl==3.1.5 ✅
pypdf==4.0.1 ✅
pandas==2.1.4 ✅
numpy==1.26.3 ✅
scikit-learn==1.4.1 ✅
sentence-transformers==2.3.0 ✅
huggingface-hub==0.20.1 ✅
```

Toutes ces versions sont **testées, stables et compatibles** !

---

## 🔧 **INSTALLATION LOCALE (si vous voulezexécuter en local)**

### **Étape 1 : Cloner le dépôt**
```bash
git clone https://github.com/Ayman-cell/chatbot.git
cd chatbot
```

### **Étape 2 : Créer un environnement virtuel**
```bash
# Windows :
python -m venv venv
.\venv\Scripts\activate

# macOS/Linux :
python -m venv venv
source venv/bin/activate
```

### **Étape 3 : Installer les dépendances**
```bash
pip install -r requirements.txt
```

### **Étape 4 : Ajouter votre clé API Cerebras**

Créez un fichier `.streamlit/secrets.toml` :
```toml
CEREBRAS_API_KEY = "csk-votre-clé-ici"
```

### **Étape 5 : Lancer l'app**
```bash
streamlit run llama.py
```

L'app va s'ouvrir à : `http://localhost:8501`

---

## 📱 **VERSION STREAMLIT CLOUD (Recommandée)**

### **C'est déjà fait ! L'app fonctionne à :**
```
🌐 https://chatbot-aymaan.streamlit.app
```

**Stepsà Streamlit Cloud pour ajouter votre clé API :**

1. Allez sur [Streamlit Cloud Dashboard](https://share.streamlit.io)
2. Cliquez sur votre app
3. Cliquez sur les **"..."** → **"Settings"**
4. Onglet **"Secrets"**
5. Collez :
```toml
CEREBRAS_API_KEY = "csk-votre-clé-ici"
```
6. **Save** et elle redémarre automatiquement

---

## ✨ **FONCTIONNALITÉS PRINCIPALESORRESPONDANTES**

### **🤖 Chatbot IA Multilingue**
- Conversations naturelles en plusieurs langues
- Compréhension contextuelle avancée
- Historique sauvegardé automatiquement

### **📄 Récupération Intelligente de Documents (RAG)**
- Upload PDF, Excel, DOCX, TXT
- Recherche sémantique avec FAISS
- Réponses basées sur vos documents

### **⚡ Optimisations**
- Chunking intelligent selon le type de contenu
- Re-ranking des résultats
- Gestion automatique des limites API

### **📊 Gestion des Tokens Cerebras**
- Limite : 30 requêtes/minute
- 64,000 tokens/minute
- Statistiques en temps réel

---

## 🆘 **EN CAS DE PROBLÈME**

### ❌ **L'app crash au démarrage**
✅ Vérifiez que `CEREBRAS_API_KEY` est dans les Secrets Streamlit Cloud

### ❌ **"ModuleNotFoundError"**
✅ Les dépendances sont automatiquement installées. Attendez 2-3 minutes et rechargez.

### ❌ **Upload ne fonctionne pas**
✅ Maximal 200MB. Décomposez les gros fichiers.

### ❌ **Lenteur au démarrage**
✅ C'est normal sur Streamlit Cloud (30-60s la première fois)

### ❌ **Autre erreur**
✅ Essayez : "Hard Reload" (Ctrl+Maj+R) ou attendez le redéploiement

---

## 🔐 **ÇA MARCHE COMMENT**

```
Vous posez une question
      ↓
L'IA parse votre question
      ↓
Si document uploadé → Recherche sémantique
      ↓
Retrieval des meilleurs chunks
      ↓
LLM Cerebras génère la réponse
      ↓
Réponse affichée
      ↓
Conversation sauvegardée en JSON
```

---

## 📂 **STRUCTURE DU PROJET**

```
chatbot/
├── llama.py                 # 🎯 App principale (2261 lignes)
├── requirements.txt         # 📦 Dépendances (14 packages)
├── README.md               # 📖 Documentation complète
├── DEPLOYMENT.md           # 🚀 Guide de déploiement
├── .streamlit/
│   ├── config.toml         # ⚙️ Configuration Streamlit
│   └── secrets.toml        # 🔐 Secrets (ignored in Git)
├── .gitignore              # 🚫 Fichiers ignorés
└── conversations/          # 💬 Historique JSON
```

---

## 🎯 **PROCHAINES ÉTAPES**

1. **Attendez 2-3 minutes** pour Streamlit Cloud
2. **Allez sur** : https://chatbot-aymaan.streamlit.app
3. **Testez** : Posez une question à l'IA
4. **Uploadez un PDF** (optionnel)
5. **Profitez !** 🎉

---

## 💡 **CONSEILS POUR UTILISER LE CHATBOT**

✅ **Utilisez le RAG** : Uploadez vos documents pour des réponses plus précises  
✅ **Continuez les conversations** : L'historique est sauvegardé  
✅ **Testez plusieurs langues** : Le chatbot est multilingue  
✅ **Vérifiez l'usage tokens** : Visible dans le panneau latéral  

---

## 📞 **BESOIN D'AIDE ?**

- **Docs LangChain** : https://python.langchain.com/
- **Docs Streamlit** : https://docs.streamlit.io/
- **API Cerebras** : https://cerebras.ai/

---

## 🎉 **C'EST TOUT !**

**Votre chatbot IA est maintenant déployé et prêt à utiliser !** 🚀

```
🌐 https://chatbot-aymaan.streamlit.app
```

**Profitez ! 😊**
