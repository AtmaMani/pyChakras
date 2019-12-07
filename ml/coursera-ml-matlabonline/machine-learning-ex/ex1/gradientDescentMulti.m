function [theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
%   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
n = size(X, 2); % get number of thetas
J_history = zeros(num_iters, 1);
theta_history = zeros(num_iters,n);

%fprintf('Initial theta0 %f theta1 %f', theta(1), theta(2));
for iter = 1:num_iters
  
  % Calculate error, which is (thetaTranspose * X vector) - y
  error = (X*theta - y);
  
  % multiply with X vector and learning rate over m
  term_vector = zeros(n,1);
  
  for theta_iter = 1:n
    current_term = (alpha/m) * sum(error .* X(:,theta_iter));
    term_vector(theta_iter) = current_term;
  endfor
  
  % find update values
  theta = theta - term_vector;
  theta_history(iter,1) = theta(1);
  theta_history(iter,2) = theta(2);
  %fprintf('Current theta0 %f theta1 %f', theta(1), theta(2));
  
    % ============================================================

    % Save the cost J in every iteration    
    J_history(iter) = computeCostMulti(X, y, theta);

end

end
