function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta
h_theta_x  = sigmoid(X*theta);
term1 = y.*log(h_theta_x);
term2 = (1-y).*log(1-h_theta_x);
term_a = (-1/m)*sum(term1+term2);

term_b1 = sum(theta(2:end).^2); % dont penalize theta0
term_b2 = lambda/(2*m);

J = term_a + term_b1*term_b2;

% calculate gradient - dont penalize theta0
term_g1 = ((h_theta_x - y)'*X)./m;
penalty = (lambda/m).*theta;
penalty(1) = 0; %reset penalty for theta0 to 0

grad = term_g1' + penalty;
% =============================================================

end
