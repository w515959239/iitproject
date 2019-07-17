function asset_prices
tic
load_data
clean_data
join_data
transform_data
visualize_data
summarize_data
train_baseline_model
evaluate_baseline_model
train_model
evaluate_model
toc
end


function load_data
Asset = { 
'SPY',''; 
}; 
Asset = table(Asset(:,1), Asset(:,2), 'VariableNames', {'Symbol', 'SE'}); 
Date1 = '1-Jan-2010'; 
Date2 = '14-Jul-2019'; 
interval = '1d';

downloadStocksData(Asset,Date1,Date2,interval)
movefile Data/SPY.xls input
end  

function clean_data

end  

function join_data

end  


function transform_data

end  

function visualize_data

end  

function summarize_data

end  

function train_baseline_model
end

function evaluate_baseline_model
end

function train_model
end

function evaluate_model
end
