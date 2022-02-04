…

# Librerías necesarias para la utilización de SelectKBest
from sklearn.feature_selection import SelectKBest, chi2

…

X.shape
	# Resultado: (1797,64)
	
X_new = SelectKBest(chi2, k=20).fit_transform(X,y)

X_new.shape
	# Resultado: (1797,20)
	
…