from sklearn import tree

#[height,weight,shoe size]

x=[[181,80,44],[150,50,37],[190,78,45],[166,56,39],[157,58,40],[180,75,41],[164,60,37],[139,65,39],[156,80,35],[176,69,43]]

y=['male','female','male','female','male','female','female','male','male','female']

clf=tree.DecisionTreeClassifier()

clf=clf.fit(x,y)

prediction=clf.predict([150,70,35])

print "prediction"