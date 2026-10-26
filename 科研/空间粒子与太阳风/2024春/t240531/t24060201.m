data = spdfcdfread("mvn_sep_l2_s2-cal-svy-full_20240214_v04_r05.cdf");
data0 = spdfcdfinfo("mvn_sep_l2_s2-cal-svy-full_20240214_v04_r05.cdf")
time = data{1,3};
elecflx = transpose(data{1,28});

pcolor(elecflx);shading interp