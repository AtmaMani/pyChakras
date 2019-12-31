% Script to use logistic regression to classify if a student will be admitted% or not, based on their performance on two tests.% Load datadata = load('ex2data1.txt');X = data(:, [1,2]); y=data(:,3);% plot training dataplotData(X, y);xlabel('Exam 1 score');ylabel('Exam 2 score');legend('Addmitted', 'Not admitted');% region - calculate cost and gradient of cost[m,n] = size(X);X = [ones(m,1),X]; % adding intercepts to Xinitial_theta = zeros(n+1,1); % initial learning parameters% compute the cost and gradient[cost, grad] = costFunction(initial_theta, X, y);fprintf('Cost at initial theta (zeros): %f\n', cost);disp('Grad at initial theta (zeros): '); disp(grad);% converge using fminunc functionpkg load optimoptions = optimoptions(@fminunc, 'Algorithm','Quasi-Newton','GradObj','on','MaxIter',400);% run fminunc to obtain optimal theta and the cost[theta, cost] = fminunc(@(t)(costFunction(t, X, y)), initial_theta, options);fprintf('Cost at theta found by fminunc: %f\n', cost);disp('theta:'); disp(theta);% plot boundaryplotDecisionBoundary(theta, X, y);hold on;xlabel('Exam 1 score');ylabel('Exam 2 score');legend('Admitted', 'Not admitted');hold off;% predictp = predict(theta, X);fprintf('Train accuracy: %f\n', mean(double(p==y))*100);