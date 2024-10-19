# Linear regression
MSE is convex to the weight matrix $w$.
$X = [1~x_i~x^2_i~...~x^D_i]$\
$L(w) = 1/N||Xw-y||^2$\
$\nabla_w||Xw-y||^2=0$ is where the convex loss function is equal to $0\in \mathbb R^D$\
In the normal equation the matrix $X^TX$ has to be inversable <==> all the data isn't related one to another. An approximated inverse solves the problem, and no need to clean the data.\
Model capacity $E_{RMS}=\sqrt{L(w^*)}$ : ability of a model to learn the training set "by heart".\
Regularization : add penality term to MSE $\tilde{L}(w)=MSE(w)+\lambda||w||^2$\
$||w||^2$ is weight decay penality, regularization is done to keep $w$ values small which prevents overfitting cause by high values.\
To help with the malidiction of dimentionality : dimensionality reduction and feature engineering/learning.


# Probabilistic modeling
The bayes theorem x NO TP



# Linear classiers
LDA
QDA
GDA

# Support vector machines
# Decision trees
# Combination of models