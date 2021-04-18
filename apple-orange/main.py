from sklearn import tree

features = [[140,1],[130,1],[160,0],[170,0]]
labels = [1,1,0,0]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)

is_apple = clf.predict([[150,0]])
if is_apple == 0:
    print(f"With the given features the classifer predicts an apple")
else:
    print(f"these features lean torwards being an orange")