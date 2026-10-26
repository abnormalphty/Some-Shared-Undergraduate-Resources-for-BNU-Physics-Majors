data = spdfcdfread("mvn_sep_l2_s1-cal-svy-full_20230601_v04_r06.cdf");
time = data{1,3};
elecflx = data{1,15};

eflx = NaN(43203,1);
for i=1:43203
    clear sum
    sum = 0
    for j=1:15
        if (elecflx(i,j)~=NaN)
            sum = sum+elecflx(i,j);
        end
    end
    eflx(i,43203) = sum
end