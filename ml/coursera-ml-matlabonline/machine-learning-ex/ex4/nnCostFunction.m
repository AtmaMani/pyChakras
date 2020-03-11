function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));

% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m

% the first part here is calculating the predicted result -> h_theta_x
% we calculate that by creating the first, hidden1, output layers of the network

term_a_vec = zeros(m,1);  % 5000x1
for i=1:m  % iterate over each training sample/image
  % make layer 1
  train_vec = X(i,:); % dims: 1x400
  train_vec = [1 train_vec]; % dims: 1x401
  
  % calc layer 2
  z2 = Theta1*train_vec';  % 25x401 x 401x1 = 25x1
  a2 = sigmoid(z2);
  a2 = [1;a2];  %26x1 with bias
  
  % calc layer 3
  z3 = Theta2*a2;  % 10x26 x 26x1 = 10x1
  a3 = sigmoid(z3);
  h_theta_x = a3;  % 10x1
  
  % make y_vec using the labeled data
  y_vec = zeros(num_labels,1);  % 10x1 in this case.
  y_class = y(i);  % get the labeled data for this image
  y_vec(y_class)=1;  % turn the scalar into a class vector
  
  % calculate cost for this training sample (classwise)
  term1 = y_vec.*log(h_theta_x);  % 10x1
  term2 = (1-y_vec).*log(1-h_theta_x);  % 10x1
  term_a = sum(term1+term2); % 1x1
  
  % insert into array
  term_a_vec(i) = term_a;
endfor

% sum cost over all training samples

term_a_sum = sum(term_a_vec);  % sum of 5000x1 = 1x1
cost_no_penalty = (-1/m)*term_a_sum;  % scalar value
J = cost_no_penalty;

% account for penalty when computing the cost.
% The idea is to square the weights for each layer, sum them up layerwise.
% before squaring, we need to remove weights for bias as we don't regularize bias
Theta1_nobias = Theta1(:,2:end);  % 25x400
Theta2_nobias = Theta2(:,2:end);  % 10x25

sum_of_sq_theta1 = sum(sum(Theta1_nobias.^2));  % scalar
sum_of_sq_theta2 = sum(sum(Theta2_nobias.^2));  % scalar
penalty = (lambda/(2*m)) * (sum_of_sq_theta1 + sum_of_sq_theta2);  % penalty

J = cost_no_penalty + penalty;

% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%

for t=1:m
  
endfor



% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%



% -------------------------------------------------------------

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
