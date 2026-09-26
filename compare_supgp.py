import sys

from pathlib import Path
import json,numpy as np,pandas as pd
from astropy.time import Time
from sgp4.api import Satrec
from sgp4 import omm
P=Path(__file__).resolve().parent
old={r['NORAD_CAT_ID']:r for r in json.load(open(P/'data/supgp-2026-09-25-earlier.json'))}
new={r['NORAD_CAT_ID']:r for r in json.load(open(P/'data/supgp-2026-09-25-new.json'))}
def sat(r):
 s=Satrec();omm.initialize(s,r);return s
def state(s,t):
 e,r,v=s.sgp4(t.jd1,t.jd2);assert e==0;return np.array(r),np.array(v)
rows=[];fields=[]
for n in new:
 a,b=old[n],new[n];sa,sb=sat(a),sat(b);t0,t1=Time(a['EPOCH']),Time(b['EPOCH'])
 fields.append(dict(norad=n,old_epoch=a['EPOCH'],new_epoch=b['EPOCH'],hours=float((t1-t0).to_value('hour')),old_bstar=a['BSTAR'],new_bstar=b['BSTAR'],delta_mean_motion=b['MEAN_MOTION']-a['MEAN_MOTION'],delta_kepler_semimajor_m=1000*((398600.8/(b['MEAN_MOTION']*2*np.pi/86400)**2)**(1/3)-(398600.8/(a['MEAN_MOTION']*2*np.pi/86400)**2)**(1/3))))
 for label,t in [('old_epoch',t0),('new_epoch',t1),('common_24utc',Time('2026-09-26T00:00:00')),('common_next24utc',Time('2026-09-27T00:00:00'))]:
  r,v=state(sa,t);rn,vn=state(sb,t);rad=r/np.linalg.norm(r);cross=np.cross(r,v);cross/=np.linalg.norm(cross);along=np.cross(cross,rad);dr=rn-r;dv=vn-v
  rows.append(dict(norad=n,time=str(t),comparison=label,separation_km=float(np.linalg.norm(dr)),radial_km=float(dr@rad),along_km=float(dr@along),cross_km=float(dr@cross),velocity_difference_m_s=float(np.linalg.norm(dv)*1000)))
pd.DataFrame(fields).to_csv(P/'results/supgp_element_changes.csv',index=False);pd.DataFrame(rows).to_csv(P/'results/supgp_common_epoch_comparison.csv',index=False)
print(pd.DataFrame(fields).to_string(index=False));print(pd.DataFrame(rows).to_string(index=False))
