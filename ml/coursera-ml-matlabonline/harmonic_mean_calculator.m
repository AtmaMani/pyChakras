%harmonic means%disp('Harmonic mean function');function result = hmean(vec1)  %calculates harmonic mean of the given vector%  vec1 = vec1(:)'; %convert to vectors  reciprocals = 1./vec1;  %convert to reciprocals  sum_reciprocals = sum(reciprocals); % sum of reciprocals - the denominator    result = size(vec1)(2) / sum_reciprocals;
endfunction
disp(hmean([2,3,4,5]));