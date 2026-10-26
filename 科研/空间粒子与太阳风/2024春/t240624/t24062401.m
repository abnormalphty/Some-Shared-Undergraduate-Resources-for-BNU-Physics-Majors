data = spdfcdfread("mvn_sep_l2_s1-cal-svy-full_20150303_v04_r03.cdf");
data0 = spdfcdfinfo("mvn_sep_l2_s1-cal-svy-full_20150303_v04_r03.cdf")
time = data{1,3};
elecflx = transpose(data{1,15});
eleceng = transpose(data{1,19});

tmin = time(1);
tmax = time(end);
time = time - tmin;
[ts,tr]=size(time);
[es,er]=size(eleceng);
eng = nan(ts,tr)

for i = 1:1:ts
    engm = 0;
    for j = 1:1:es
        engm = engm + eleceng(j,i);
    end
    eng(i,1) = engm
end

%pcolor(elecflx);shading interp