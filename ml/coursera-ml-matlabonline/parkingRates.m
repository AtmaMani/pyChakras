%functions%function charge = parkingRates(hours)  %Calculates parking charge based on number of hours%  if hours <=1    charge = 2;  elseif hours<=8 && hours>1    charge = hours*0.75;  else    charge = 9;  end
end