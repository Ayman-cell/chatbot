# 🤖 Assistant IA Multilingue - Cerebras Llama 3.1-8B

**Un chatbot intelligent et multilingue basé sur l'IA générative avec récupération de documents (RAG) avancée**

🚀 **[Essayer l'application en ligne](https://chatbot-aymaan.streamlit.app/)**

---

## 📋 Vue d'ensemble

Ce projet est un **assistant IA conversationnel complet** construit avec Streamlit et le modèle **Cerebras Llama 3.1-8B**. C'est une application web interactive qui combine les capacités de traitement du langage naturel (NLP) avec un système avancé de récupération et de génération augmentée par récupération (RAG) pour fournir des réponses précises et contextuelles.

---

## ✨ Fonctionnalités principales

### 1. **Chatbot Conversationnel Multilingue**
- 🌍 Support complet de **plusieurs langues** (Français, Anglais, Espagnol, Allemand, etc.)
- 💬 Conversations naturelles et fluides avec l'IA
- 🧠 Compréhension contextuelle avancée
- 📝 Historique des conversations sauvegardé automatiquement en **JSON**
- 🔄 Gestion des tours de parole (user ↔ assistant)

### 2. **Système RAG (Retrieval-Augmented Generation) Avancé**
- 📄 **Support multi-formats** : PDF, Excel, DOCX, TXT
- 🧩 **Chunking intelligent** : Adaptation automatique de la taille des chunks selon le type de contenu :
  - **Contenu mathématique** : 960 caractères (optimisé pour les formules)
  - **Contenu orienté code** : 720 caractères (optimisé pour la syntaxe)
  - **Contenu généraliste** : 1200 caractères (optimisé pour les textes normaux)
- 🔍 **Recherche sémantique améliorée** via embeddings FAISS
- 📊 **Re-ranking intelligent** des résultats avec cross-encoder
- 🎯 Récupération des **documents les plus pertinents** pour chaque question

### 3. **Gestion Avancée des Tokens Cerebras**
- ⏱️ **Limitation des requêtes** en temps réel :
  - 30 requêtes par minute
  - 64,000 tokens par minute
  - 900 requêtes par heure
  - 1,000,000 tokens par jour
- 📊 **Affichage des statistiques d'usage** en direct
- ⏳ **Gestion automatique des files d'attente** quand les limites sont atteintes
- 🔄 **Retry automatique** avec délai (max 3 tentatives)

### 4. **Interface Web Intuitive (Streamlit)**
- 🎨 **Design moderne et responsive**
- 📱 **Layout adaptatif** (widest mode pour une meilleure utilisation de l'espace)
- 🎯 **Panneau latéral** avec options et configurations
- 📈 **Affichage des statistiques** en temps réel
- 🎛️ **Contrôles interactifs** pour ajuster les paramètres

### 5. **Gestion des Fichiers Utilisateur**
- 📤 **Upload multi-fichiers** avec validation
- 🗂️ **Traitement automatique** de documents volumineux
- 💾 **Extraction intelligente** du contenu textuel
- 📊 **Gestion efficace** de la mémoire pour les gros fichiers

### 6. **Sauvegarde et Historique des Conversations**
- 💾 **Sauvegarde JSON automatique** de chaque conversation
- 🔍 **Identifiants uniques** (UUID) pour chaque conversation
- ⏰ **Métadonnées temporelles** (date/heure)
- 📋 **Chargement et visualisation** des conversations précédentes
- 🔄 **Reprise de conversations** anciennes

### 7. **Analyse et Traitements Avancés**
- 📈 **Statistiques linguistiques** sur les messages
- 🧮 **Compteur de tokens** pour optimiser l'utilisation
- 📊 **Analyse de la similarité** entre requêtes avec TF-IDF et cosine similarity
- 🔬 **Extraction d'informations** via expressions régulières avancées

### 8. **Optimisation des Performances**
- ⚡ **Cache Streamlit** pour accélérer le re-rendering
- 🔐 **Gestion sécurisée** des API keys
- 📦 **Chunking optimisé** selon le type de document
- 🎯 **Retrieval de documents** efficace avec FAISS
- 🔄 **Délai entre requêtes** configurable

---

## 🛠️ Technologies utilisées

| Technologie | Utilisation |
|---|---|
| **Streamlit** | Framework web pour l'interface utilisateur |
| **Cerebras Llama 3.1-8B** | Modèle LLM pour la génération de texte |
| **LangChain** | Orchestration des chaînes d'IA et RAG |
| **FAISS** | Vector store pour la recherche sémantique |
| **HuggingFace Embeddings** | Création d'embeddings textuels |
| **Sentence Transformers** | Cross-encoder pour le re-ranking |
| **PyPDF** | Lecture de fichiers PDF |
| **OpenPyXL** | Traitement de fichiers Excel |
| **Pandas** | Manipulation de données |
| **Scikit-learn** | TF-IDF et analyse de similarité |
| **NumPy** | Calculs numériques et vectoriels |

---

## 📋 Prérequis

Avant de démarrer, assurez-vous d'avoir :
- Python 3.9 ou supérieur
- pip (gestionnaire de paquets Python)
- Une API key Cerebras (gratuite et facile à obtenir)
- Au moins 4GB de RAM
- Une connexion Internet stable

---

## 🚀 Installation et démarrage

### 1. **Cloner le dépôt**
```bash
git clone https://github.com/yourusername/Ayman-cell-chatbot.git
cd Ayman-cell-chatbot
```

### 2. **Créer un environnement virtuel**
```bash
python -m venv venv
```

**Activation de l'environnement :**
- **Windows** :
  ```bash
  .\venv\Scripts\activate
  ```
- **macOS/Linux** :
  ```bash
  source venv/bin/activate
  ```

### 3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

### 4. **Configurer l'API Cerebras**
Ouvrez le fichier `llama.py` et remplacez la clé API :
```python
CEREBRAS_API_KEY = "votre-clé-api-ici"
```

ou définissez la variable d'environnement :
```bash
set CEREBRAS_API_KEY=votre-clé-api-ici  # Windows
export CEREBRAS_API_KEY=votre-clé-api-ici  # macOS/Linux
```

### 5. **Lancer l'application**
```bash
streamlit run llama.py
```

L'application s'ouvrira automatiquement sur `http://localhost:8501`

---

## 📖 Guide d'utilisation

### Interface de Chat
1. **Entrez votre question** dans le champ de texte en bas
2. **Appuyez sur Entrée** ou cliquez sur le bouton d'envoi
3. **L'IA traite** et répond en temps réel
4. **Votre conversation est sauvegardée** automatiquement

### Utiliser le RAG (upload de documents)

1. **Cliquez sur "Upload des fichiers"** dans la barre latérale
2. **Sélectionnez des fichiers** (PDF, Excel, DOCX, TXT)
3. **L'application traite** les documents automatiquement
4. **Vos questions** bénéficieront du contexte des documents
5. **Les réponses** seront plus précises et documentées

### Types de documents supportés

| Format | Extension | Support |
|---|---|---|
| PDF | .pdf | ✅ Complet |
| Excel | .xlsx, .xls | ✅ Complet |
| Word | .docx | ✅ Complet |
| Texte | .txt | ✅ Complet |

### Visualiser l'historique

1. **Consultez le panneau latéral** pour voir vos conversations passées
2. **Cliquez sur une conversation** pour la recharger
3. **Continuez ou révisez** votre historique

---

## ⚙️ Configuration avancée

### Paramètres RAG

Vous pouvez ajuster les paramètres de RAG dans la section `RAG_CONFIG` :

```python
RAG_CONFIG = {
    "general": {
        "chunk_size": 1200,        # Taille des chunks en caractères
        "chunk_overlap": 300,      # Chevauchement entre chunks
        "separators": ["\n\n", "\n", " ", ""]
    },
    "math_heavy": {
        "chunk_size": 960,
        "chunk_overlap": 225,
        "separators": ["\n\n", "\n$$", "\n$", " ", ""]
    },
    "code_heavy": {
        "chunk_size": 720,
        "chunk_overlap": 150,
        "separators": ["\n\n", "\n\`\`\`", "\nclass", "\ndef", " "]
    }
}
```

### Limites des tokens Cerebras

Modifiez `TOKEN_LIMITS` pour ajuster les restrictions :

```python
TOKEN_LIMITS = {
    "max_requests_per_minute": 30,
    "max_tokens_per_minute": 64000,
    "max_requests_per_hour": 900,
    "max_tokens_per_hour": 1000000,
    "max_requests_per_day": 14400,
    "max_tokens_per_day": 1000000,
    "max_tokens_per_request": 8000,
    "chunk_size": 4000,
    "delay_between_requests": 2,
    "max_retries": 3
}
```

---

## 📁 Structure du projet

```
Ayman-cell-chatbot/
├── llama.py                    # Fichier principal de l'application
├── conversations/              # Dossier de stockage des conversations JSON
│   ├── conv_*.json            # Fichiers de conversation sauvegardés
├── requirements.txt            # Dépendances Python
├── README.md                   # Ce fichier
└── .gitignore                 # Fichiers à ignorer dans Git
```

### Fichier de conversation (JSON)

```json
{
  "id": "unique-uuid",
  "timestamp": "2024-02-13T10:30:45.123456",
  "messages": [
    {
      "role": "user",
      "content": "Votre question",
      "timestamp": "2024-02-13T10:30:45.123456"
    },
    {
      "role": "assistant",
      "content": "Réponse de l'IA",
      "timestamp": "2024-02-13T10:30:50.456789"
    }
  ]
}
```

---

## 🔒 Sécurité et bonnes pratiques

### ⚠️ Points importants

1. **API Keys** : Ne commitez JAMAIS votre clé API
   - Utilisez un fichier `.env` pour les clés secrètes
   - Utilisez `python-dotenv` pour charger les variables d'environnement

2. **Données sensibles** : 
   - Les conversations sont stockées localement
   - Aucune donnée sensible n'est envoyée à des tiers non autorisés

3. **Limites de l'API** :
   - Respectez les quotas Cerebras
   - L'application gère automatiquement les dépassements

---

## 🐛 Dépannage

### Problème : "Clé API invalide"
```
Solution : Vérifiez que votre CEREBRAS_API_KEY est correctement définie
```

### Problème : "FAISS not found"
```bash
pip install faiss-cpu
# ou pour GPU :
pip install faiss-gpu
```

### Problème : Conversations non sauvegardées
```
Solution : Vérifiez que le dossier 'conversations' existe et que vous avez les permissions d'écriture
```

### Problème : Lenteur de l'application
```
Solution : 
- Réduisez la taille des chunks (chunk_size)
- Diminuez le nombre de documents traités
- Videz le cache de Streamlit : streamlit cache clear
```

---

## 📊 Cas d'usage

### 1. **Support client intelligent**
Fournissez vos documents de support et le chatbot répond aux questions des clients de manière automatique.

### 2. **Assistant de recherche**
Uploadez des papers de recherche ou des livres et posez des questions spécifiques.

### 3. **Tuteur personnel**
Inutile d'expliquer des concepts - l'IA peut vous aider avec des documents fournis.

### 4. **Analyse de documents**
Traitez plusieurs documents et obtenez des résumés ou analyses comparatives.

### 5. **Assistance multilingue**
Demandez à l'IA de répondre dans différentes langues, même si vos documents sont dans une autre langue.

---

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. **Fork** le dépôt
2. **Créez une branche** (`git checkout -b feature/AmazingFeature`)
3. **Commit** vos changements (`git commit -m 'Add some AmazingFeature'`)
4. **Push** vers la branche (`git push origin feature/AmazingFeature`)
5. **Ouvrez une Pull Request**

---

## 📝 Licence

Ce projet est sous licence **MIT** - voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## 👨‍💻 Auteur

**Ayman**
- � GitHub : [@aymen-cell](https://github.com/aymen-cell)
- 🚀 Application déployée : [https://chatbot-aymaan.streamlit.app/](https://chatbot-aymaan.streamlit.app/)

---

## 🙏 Remerciements

- **Cerebras** pour leur API LLM puissante et abordable
- **LangChain** pour l'orchestration RAG
- **Streamlit** pour un framework web simplifié
- **HuggingFace** pour les modèles d'embeddings

---

## 📚 Ressources utiles

- [Documentation Cerebras](https://docs.cerebras.ai/)
- [Documentation LangChain](https://python.langchain.com/)
- [Documentation Streamlit](https://docs.streamlit.io/)
- [FAISS Documentation](https://github.com/facebookresearch/faiss)

---

## 📞 Support

Pour toute question ou problème :
1. Vérifiez la section **Dépannage**
2. Ouvrez une **Issue** sur GitHub
3. Contactez l'auteur directement

---

**Dernière mise à jour** : 13 février 2026
**Version** : 1.0.0

