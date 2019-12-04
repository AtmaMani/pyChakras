function J = computeCost(X, y, theta)
%COMPUTECOST Compute cost for linear regression
%   J = COMPUTECOST(X, y, theta) computes the cost of using theta as the
%   parameter for linear regression to fit the data points in X and y

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta
%               You should set J to the cost.

% Compute hypothesis function. Which is given by theta'*x
hypothesis_fn = X*theta;

% Compute error function which is given by Sum(square(error))
error_fn = sum((hypothesis_fn - y).^2);

% Compute loss function which is error function divided by 2*training samples
loss_fn = error_fn ./(2*m);

% return
J = loss_fn
% =========================================================================

end
