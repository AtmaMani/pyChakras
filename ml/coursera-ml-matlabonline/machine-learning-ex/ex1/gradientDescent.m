function [theta, J_history, theta_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);
theta_history = zeros(num_iters,2);
%fprintf('Initial theta0 %f theta1 %f', theta(1), theta(2));
for iter = 1:num_iters
  
    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %
  
  % IN GD, we  simultaneously update both theta0 and theta1.
  % theta0 = theta0 - (alpha/m)*sum(error * x0)
  
  % Calculate error, which is (thetaTranspose * X vector) - y
  error = (X*theta - y);
  
  % multiply with X vector and learning rate over m
  %term0 = (alpha/m) * sum(error * X(:,1)');
  %term1 = (alpha/m) * sum(error * X(:,2)');
  
  term0 = (alpha/m) * sum(error .* X(:,1));
  term1 = (alpha/m) * sum(error .* X(:,2));
  
  term_vector = [term0;term1];
  
  % find update values
  theta = theta - term_vector;
  theta_history(iter,1) = theta(1);
  theta_history(iter,2) = theta(2);
  %fprintf('Current theta0 %f theta1 %f', theta(1), theta(2));
  
    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta);

end

end
