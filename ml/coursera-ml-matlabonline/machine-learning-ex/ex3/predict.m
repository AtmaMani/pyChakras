function p = predict(Theta1, Theta2, X)
%PREDICT Predict the label of an input given a trained neural network
%   p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given the
%   trained weights of a neural network (Theta1, Theta2)

% Useful values
m = size(X, 1);
num_labels = size(Theta2, 1);

% You need to return the following variables correctly 
p = zeros(size(X, 1), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Complete the following code to make predictions using
%               your learned neural network. You should set p to a 
%               vector containing labels between 1 to num_labels.
%
% Hint: The max function might come in useful. In particular, the max
%       function can also return the index of the max element, for more
%       information see 'help max'. If your examples are in rows, then, you
%       can use max(A, [], 2) to obtain the max for each row.
%

% get first training set
for row = 1:m,
  x_1 = X(row,:)'; % row i, all cols
  x_1 = [1;x_1]; % 401x1 col vector with a bias node

  z2 = Theta1*x_1; % 25x401 X 401x1 = 25x1 
  a2 = sigmoid(z2); % 25x1

  a2_1 = [1; a2]; % 26x1
  z3 = Theta2*a2_1; % 10x26 X 26x1 = 10x1

  a3 = sigmoid(z3); % 10x1

  % find index of class with max prob
  [p_max, p_index] = max(a3', [], 2);
  
  p(row) = p_index;
endfor

% =========================================================================
end
