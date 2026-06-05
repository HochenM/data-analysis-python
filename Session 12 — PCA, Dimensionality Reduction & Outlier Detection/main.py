#Session 10
#####################
#Part 1
import numpy as np
from PIL.TiffImagePlugin import idx
from sklearn.datasets import  fetch_openml
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
#images, labels = fetch_openml('mnist_784', return_X_y=True)
#print(images.shape, labels.shape)
#plt.imshow(images[3454].values.reshape(28, 28))
#plt.title(labels[3454])
#plt.show()
#sample, feature = images.shape
#classes = np.unique(labels)
#print(classes)
#print(sample)
#print(feature)

 #PCA
#samplng
#images = images[:500]
#labels = labels[:500]

#pca = PCA(n_components=3)
#labels = np.array([int(l) for l in labels]) #Important
#pca_data = pca.fit_transform(images)
#class_num = 0#/1/2/3
#pca_data = pca.fit_transform(images[labels==class_num])
#print(pca_data.shape)
#print(type(pca_data))
#fig = plt.figure()
#ax = fig.add_subplot(111,projection='3d')
#ax.scatter(pca_data[:,0], pca_data[:,1], pca_data[:,2], c=labels)
#ax.scatter(pca_data[:,0], pca_data[:,1], pca_data[:,2], c=labels[labels==class_num])
#mean = np.mean(pca_data,axis=0)
#ax.scatter(mean[:,0], mean[:,1], mean[:,2], c='red')
#std = np.std(pca_data,axis=0)
#outlier = euclidean_distances(pca_data,mean.reshape[1,-1]) > 2 *std
#print(outlier)
#plt.show()

#حالت 3
#std = np.std(pca_data)
#for points in pca_data:
 #   if np.abs(points-(mean +std)) >2 *std:
  #      print('Outlier')
   #    print("OK")

#std = np.std(pca_data)
#   distance = np.abs(pca_data - (mean +std))
#for points in pca_data:
  #  outlier=(distance[distance> (2 *std)])
   # normal=(distance[distance <= (2 *std)])


#for idx,points in enumerate(pca_data):
 #   if distance[idx] <= 2*std:
  #      ax.scatter(points[0],points[1],points[2],c='r')
   # else:
    #    ax.scatter(points[0],points[1],points[2],c='b')
#plt.show()


#distance = []
#outlier_index = []
# why with hands : because the shape is wrong in rst of the code
#for points in pca_data:
 #   distance = np.sqrt((points[0]-mean[1])**2 + (points[1]-mean[1])**2 + (points[2]-mean[2])**2)
  #  distance.append(distance)
#for idx,points in enumerate(pca_data):
 #   if distance[idx] <= 2*std:
  #      ax.scatter(points[0],points[1],points[2],c='r')
   # else:
    #    ax.scatter(points[0],points[1],points[2],c='b')
         #outlier_index.append(idx)
#plt.show()
#print(outlier_index)


#Or IQR

########
 #Outlier finding
from sklearn.metrics.pairwise import euclidean_distances,manhattan_distances, cosine_similarity
#points =np.array([[1,2],[2,2],[3,4]])

#mean = np.mean(points,axis=0)
#std = np.std(points,axis=0)
#outlier = euclidean_distances(points,mean) > 2 *std
#print(mean)
#print(std)




#for class_num in labels:

# pca = PCA(n_components=3)
# labels = np.array([int(l) for l in labels]) #Important
# pca_data = pca.fit_transform(images)
# class_num = 0#/1/2/3
# pca_data = pca.fit_transform(images[labels==class_num])
# print(pca_data.shape)
# print(type(pca_data))
# fig = plt.figure()
# ax = fig.add_subplot(111,projection='3d')
# ax.scatter(pca_data[:,0], pca_data[:,1], pca_data[:,2], c=labels)
# ax.scatter(pca_data[:,0], pca_data[:,1], pca_data[:,2], c=labels[labels==class_num])
# mean = np.mean(pca_data,axis=0)
# ax.scatter(mean[:,0], mean[:,1], mean[:,2], c='red')
# std = np.std(pca_data,axis=0)
# outlier = euclidean_distances(pca_data,mean.reshape[1,-1]) > 2 *std
# print(outlier)
# plt.show()

# حالت 3
# std = np.std(pca_data)
# for points in pca_data:
#   if np.abs(points-(mean +std)) >2 *std:
#      print('Outlier')
#    print("OK")

# std = np.std(pca_data)
#   distance = np.abs(pca_data - (mean +std))
# for points in pca_data:
#  outlier=(distance[distance> (2 *std)])
# normal=(distance[distance <= (2 *std)])


# for idx,points in enumerate(pca_data):
#   if distance[idx] <= 2*std:
#      ax.scatter(points[0],points[1],points[2],c='r')
# else:
#    ax.scatter(points[0],points[1],points[2],c='b')
# plt.show()


# distance = []
# outlier_index = []
# why with hands : because the shape is wrong in rst of the code
# for points in pca_data:
#   distance = np.sqrt((points[0]-mean[1])**2 + (points[1]-mean[1])**2 + (points[2]-mean[2])**2)
#  distance.append(distance)
# for idx,points in enumerate(pca_data):
#   if distance[idx] <= 2*std:
#      ax.scatter(points[0],points[1],points[2],c='r')
# else:
#    ax.scatter(points[0],points[1],points[2],c='b')
# outlier_index.append(idx)
# plt.show()
# print(outlier_index)
#for show راهنمایی
#   ax = fig.add_subplot(250+class_num-1  , projection='3d')
    #ax.title(str(class_num))