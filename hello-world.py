from sklearn import tree

# features
# 0 = smooth
# 1 = bumpy
features = [[140, 0], [130, 0], [150, 1], [170, 1]]

# labels
# 0 = apple
# 1 = orange
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()

# fit ==> training algorithm to find patterns and data
clf = clf.fit(features, labels)

print clf.predict([160, 1])
