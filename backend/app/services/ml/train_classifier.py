# import pandas as pd
# import joblib

# from sklearn.model_selection import train_test_split
# from sklearn.pipeline import Pipeline
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.linear_model import LogisticRegression
# from sklearn.metrics import classification_report


# # ==========================================
# # 1. CHARGEMENT DATASET
# # ==========================================

# df = pd.read_csv("data/documents.csv")

# X = df["texte"]
# y = df["domaine"]


# # ==========================================
# # 2. SEPARATION TRAIN / TEST
# # ==========================================

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     # test_size=0.2,
#     test_size=0.4,
#     random_state=42,
#     stratify=y
# )


# # ==========================================
# # 3. MODELE
# # ==========================================

# # model = Pipeline([
# #     (
# #         "tfidf",
# #         TfidfVectorizer(
# #             lowercase=True,
# #             ngram_range=(1, 2)
# #         )
# #         # TfidfVectorizer(
# #         #     lowercase=True,
# #         #     ngram_range=(1, 2),
# #         #     sublinear_tf=True,
# #         #     min_df=1,
# #         #     max_df=0.95
# #         # )
# #     ),
# #     (
# #         "classifier",
# #         LogisticRegression(
# #             max_iter=1000
# #         )
# #     )
# # ])

# model = Pipeline([
#     (
#         "tfidf",
#         TfidfVectorizer(
#             lowercase=True,
#             ngram_range=(1, 2),
#             sublinear_tf=True,
#             min_df=1
#         )
#     ),
#     (
#         "classifier",
#         LogisticRegression(
#             max_iter=2000,
#             class_weight="balanced"
#         )
#     )
# ])
# # ==========================================
# # 4. ENTRAINEMENT
# # ==========================================

# model.fit(
#     X_train,
#     y_train
# )


# # ==========================================
# # 5. EVALUATION
# # ==========================================

# predictions = model.predict(X_test)

# print("\n========== RESULTATS ==========")

# print(
#     classification_report(
#         y_test,
#         predictions
#     )
# )


# # ==========================================
# # 6. SAUVEGARDE
# # ==========================================

# joblib.dump(
#     model,
#     "app/services/ml/model.pkl"
# )

# print("\nModèle sauvegardé.")

import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.metrics import (
    classification_report,
    accuracy_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

import matplotlib.pyplot as plt

# ==========================================
# 1. CHARGEMENT DU DATASET
# ==========================================

df = pd.read_csv("data/documents.csv")

X = df["texte"]
y = df["domaine"]


# ==========================================
# 2. SEPARATION TRAIN / TEST
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# ==========================================
# 3. MODELE
# ==========================================

model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            ngram_range=(1, 2),
            sublinear_tf=True,
            min_df=1
        )
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=2000,
            class_weight="balanced"
        )
    )
])


# ==========================================
# 4. ENTRAINEMENT
# ==========================================

model.fit(
    X_train,
    y_train
)


# # ==========================================
# # 5. EVALUATION
# # ==========================================

# predictions = model.predict(X_test)

# accuracy = accuracy_score(
#     y_test,
#     predictions
# )

# print("\n========== RESULTATS ==========")

# print(
#     "Accuracy :",
#     round(accuracy, 4)
# )

# print("\n========== RAPPORT ==========")

# print(
#     classification_report(
#         y_test,
#         predictions,
#         zero_division=0
#     )
# )

# ==========================================
# 5. EVALUATION
# ==========================================

predictions = model.predict(X_test)


# ------------------------------------------
# Accuracy
# ------------------------------------------

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\n========== RESULTATS ==========")

print(
    "Accuracy :",
    round(accuracy, 4)
)


# ------------------------------------------
# Rapport de classification
# ------------------------------------------

print("\n========== RAPPORT DE CLASSIFICATION ==========")

print(
    classification_report(
        y_test,
        predictions,
        zero_division=0
    )
)


# ------------------------------------------
# Matrice de confusion
# ------------------------------------------

matrice = confusion_matrix(
    y_test,
    predictions,
    labels=model.classes_
)

print("\n========== MATRICE DE CONFUSION ==========")

print(matrice)


# ------------------------------------------
# Affichage graphique
# ------------------------------------------

plt.figure(figsize=(14, 14))

disp = ConfusionMatrixDisplay(
    confusion_matrix=matrice,
    display_labels=model.classes_
)

disp.plot(
    xticks_rotation=90
)

plt.title("Matrice de confusion - Classification des domaines")

plt.tight_layout()

plt.show()
# ==========================================
# 6. SAUVEGARDE
# ==========================================

joblib.dump(
    model,
    "app/services/ml/model.pkl"
)

print("\nModèle sauvegardé.")