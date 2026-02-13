# 🚀 GUIDE COMPLET DE DÉPLOIEMENT SUR RENDER

## **ÉTAPE 1: Créer un compte Render**

1. Allez à: https://render.com
2. Cliquez sur **"Sign up"** (haut droit)
3. Choisissez **"Sign up with GitHub"** (plus facile)
4. Autorisez Render à accéder à vos repos GitHub
5. Complétez votre profil

---

## **ÉTAPE 2: Connecter votre repo GitHub à Render**

1. Go to: https://dashboard.render.com
2. Cliquez sur **"New +"** → **"Web Service"**
3. Sélectionnez **"Connect a repository"**
4. Cherchez: **`Ayman-cell/chatbot`**
5. Cliquez **"Connect"**

---

## **ÉTAPE 3: Configurer le service**

### **Remplir les champs:**

| Champ | Valeur |
|-------|--------|
| **Name** | `chatbot-aymaan` |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `streamlit run llama.py --server.port=10000 --server.address=0.0.0.0` |
| **Plan** | **Free** (gratuit) |

### **Ajouter les variables d'environnement:**

1. Scroll down → **"Environment Variables"**
2. Cliquez **"Add Environment Variable"**
3. **Key:** `CEREBRAS_API_KEY`
4. **Value:** `csk-wcmnmtnhn9d5hdx25mkmy2h3k4cyj6kdx9fd9v4emd8545xd`
5. Cliquez **"Add"**

---

## **ÉTAPE 4: Déployer**

1. En bas: Cliquez **"Create Web Service"**
2. **Attendre 3-5 minutes** (premier déploiement)
3. Vous verrez le **statut "Live"** en vert
4. **URL de votre app:** `https://chatbot-aymaan.onrender.com`

---

## **ÉTAPE 5: Vérifier que ça marche**

1. Allez à: https://chatbot-aymaan.onrender.com
2. Attendez le chargement (peut prendre 30 sec pour le cold start)
3. **Testez**: Écrivez un message
4. ✅ Si ça répond → **C'est live!**

---

## **FICHIERS NÉCESSAIRES DANS VOTRE REPO**

Assurez-vous d'avoir:

✅ **llama.py** ← Votre code Streamlit (déjà présent)
✅ **requirements.txt** ← Vos dépendances (déjà présent)
✅ **render.yaml** ← Configuration Render (je créé)

---

## **COMMANDES À EXÉCUTER MAINTENANT**

```powershell
cd "c:\Users\Aymen\tensorflow-env\Downloads\cereberas project1"
git add .
git commit -m "add: Render deployment configuration"
git push origin main
```

Puis attendez que Render détecte et redéploie automatiquement.

---

## **POINTS IMPORTANTS**

⚠️ **Ne pas oublier:**
- Render va détecter `render.yaml` automatiquement OU utiliser le dashboard
- Le first deploy peut être lent (3-5 min)
- **Free tier:** 750 heures/mois gratuit (= environ 1 mois non-stop)
- Après 15 min d'inactivité → l'app s'endort (cold start = 30 sec)

---

## **SI ÇA NE MARCHE PAS**

### **Voir les logs:**
1. Dashboard Render → Votre service
2. **"Logs"** en haut
3. Cherchez `ERROR` ou messages rouges
4. Les erreurs montrent le problème exacte

### **Problèmes courants:**

| Erreur | Solution |
|--------|----------|
| `ModuleNotFoundError` | Vérifiez `requirements.txt` |
| `CEREBRAS_API_KEY not found` | Vérifiez env var dans dashboard |
| Port error | Changez port dans startCommand |
| Build timeout | Augmentez timeout ou optimisez requirements |

---

## **AVANTAGES RENDER vs STREAMLIT CLOUD**

| Feature | Render | Streamlit Cloud |
|---------|--------|-----------------|
| **Gratuit** | ✅ 750h/mois | ❌ Limité |
| **Facilité** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Vitesse** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Support deps** | ✅ Excellent | ⚠️ Problématique |
| **Cold start** | 30 sec | 10 sec |

---

## **PROCHAINES ÉTAPES APRÈS DÉPLOIEMENT**

1. ✅ App fonctionne
2. 📊 Ajouter analytics (Render dashboard)
3. 💰 Si besoin: Passer à plan payant ($7/mois)
4. 🔧 Mettre à jour code: `git push` → Render redéploie auto

---

**Avez-vous besoin d'aide pour une étape spécifique?**
