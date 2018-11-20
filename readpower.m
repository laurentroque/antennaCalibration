function [ff, dd] = readpower(fname,npts)
% read DUTPNPI trace files from PNA-X (convert dBm/Hz to W/Hz)
fid = fopen(fname);

TYPE = fgetl(fid);
PARAM = fgetl(fid);

for ii = 1:npts
    tmp = str2num(fgetl(fid));
    ff(ii) = tmp(1);
    dd(ii) = tmp(2);
end

dd = 10.^((dd-30)./10);

fclose(fid);
