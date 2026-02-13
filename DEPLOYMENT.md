# 🚀 Guide de Déploiement sur Streamlit Cloud

## **Déploiement Simple en 5 minutes**

### **Étape 1 : S'enregistrer sur Streamlit Cloud**

1. Allez sur : https://streamlit.io/cloud
2. Cliquez sur **"Sign up"**
3. Connectez-vous avec **GitHub** (l'option la plus simple)
4. Autorisez Streamlit
5. Cliquez sur **"Create app"**

### **Étape 2 : Configuration du déploiement**

Dans Streamlit Cloud, remplissez :

| Champ | Valeur |
|---|---|
| **Repository** | `Ayman-cell/chatbot` |
| **Branch** | `main` |
| **Main file path** | `llama.py` |

### **Étape 3 : Ajouter le Secret (API Key)**

1. Dans Streamlit Cloud, allez à **"Advanced settings"**
2. Cliquez sur **"Secrets"**
3. Collez votre clé API Cerebras au format :

```toml
CEREBRAS_API_KEY = "csk-votre-cle-api-ici"
```

4. Cliquez **"Save"**

### **Étape 4 : Activer le déploiement**

Cliquez sur **"Deploy"** et attendez ~2-3 minutes

Votre app sera ensuite disponible à :
```
https://ayman-cell-chatbot.streamlit.app
```

---

## **❌ Dépannage des Erreurs Courantes**

### **Erreur : "ModuleNotFoundError: No module named 'streamlit'"**
✅ Solution : Les dépendances sont automatiquement installées à partir de `requirements.txt`

### **Erreur : "CEREBRAS_API_KEY not found"**
✅ Solution : Assurez-vous d'avoir mis la clé dans les Secrets Streamlit Cloud (pas dans secrets.toml)

### **Erreur : "FAISS Error"**
✅ Solution : Streamlit Cloud a déjà FAISS installé. Si problème, utilisez `faiss-cpu`

### **App très lente au démarrage**
✅ Solution : Streamlit Cloud peut prendre 30-60 secondes pour démarrer la première fois

---

## **📊 Performance sur Streamlit Cloud**

| Métrique | Valeur | Notes |
|---|---|---|
| **CPU** | Partagé | Toujours disponible |
| **RAM** | 1GB | Suffisant pour l'application |
| **Stockage** | Limité | Utilisez `/tmp` pour les fichiers temporaires |
| **Uploads** | Max 200MB | Configurable dans config.toml |
| **Temps démarrage** | 30-60s | Normal pour une première visite |

---

## **🔒 Gestion sécurisée des secrets**

### **✅ À FAIRE :**
```toml
# Dans Streamlit Cloud Secrets UI:
CEREBRAS_API_KEY = "votre-clé-ici"
```

### **❌ À NE PAS FAIRE :**
- Ne mettez JAMAIS la clé directement dans le code
- Ne commitez JAMAIS les secrets dans Git
- Ne partagez JAMAIS vos clés API

---

## **🔄 Mise à jour automatique du déploiement**

À chaque **push** sur la branche `main` de GitHub, Streamlit Cloud se met à jour automatiquement !

```bash
# Après avoir fait des changements localement :
git add .
git commit -m "Mise à jour: description"
git push origin main

# L'app sur Streamlit Cloud se redéploiera automatiquement
```

---

## **📱 Accéder à votre application**

Une fois déployée, votre app est accessible à :

```
https://ayman-cell-chatbot.streamlit.app
```

Ou consultez l'URL dans le dashboard Streamlit Cloud

---

## **⚡ Optimisations recommandées**

### **1. Ajouter du cache pour les embeddings**
```python
@st.cache_resource
def load_embeddings():
    return HuggingFaceEmbeddings()
```

### **2. Limiter la taille des fichiers uploadés**
```python
st.file_uploader("Upload", accept_multiple_files=True, 
                 max_upload_size=50_000_000)  # 50MB
```

### **3. Utiliser le cache Streamlit**
```python
@st.cache_data
def process_large_file(file):
    return process(file)
```

---

## **🛠️ Variables d'environnement personnalisées**

Dans Streamlit Cloud Secrets, vous pouvez ajouter :

```toml
CEREBRAS_API_KEY = "votre-clé"
# Autres variables :
MAX_TOKENS = "8000"
TIMEOUT = "30"
```

Accédez-les dans le code :
```python
import streamlit as st
api_key = st.secrets["CEREBRAS_API_KEY"]
```

---

## **📞 Support et Ressources**

- **Docs Streamlit Cloud** : https://docs.streamlit.io/streamlit-cloud
- **Forum** : https://discuss.streamlit.io/
- **Chat d'aide** : Dans le dashboard Streamlit Cloud

---

**Voilà ! Votre chatbot IA est prêt à être déployé sur Streamlit Cloud ! 🚀**
