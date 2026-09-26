"""Offline public-data reproduction. Python 3 standard library only."""
from pathlib import Path
import json,csv,math,itertools,statistics,datetime
P=Path(__file__).resolve().parent;OUT=P/'results';OUT.mkdir(exist_ok=True)
def write(name,rows):
 with (OUT/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
def gp(name):return {int(r['NORAD_CAT_ID']):r for r in json.load(open(P/'data'/name))}
old=gp('gp-2026-09-23.json');new=gp('gp-2026-09-24-25.json');target=new[100242]['BSTAR'];mu=398600.8
rows=[]
for n in [67232,69589,69590,69591,100241,100240,100242]:
 r=new[n];rows.append(dict(norad=n,epoch=r['EPOCH'],bstar=r['BSTAR'],bb11_bstar_ratio=target/r['BSTAR']))
write('bstar_snapshot.csv',rows)
rows=[]
for n in [100242,100241,100240]:
 a,b=old[n],new[n];dt=(datetime.datetime.fromisoformat(b['EPOCH'])-datetime.datetime.fromisoformat(a['EPOCH'])).total_seconds()/86400
 axis=lambda r:(mu/(r['MEAN_MOTION']*2*math.pi/86400)**2)**(1/3)
 rows.append(dict(norad=n,span_days=dt,old_bstar=a['BSTAR'],new_bstar=b['BSTAR'],semimajor_proxy_change_m_per_day=1000*(axis(b)-axis(a))/dt))
write('gp_two_snapshot_changes.csv',rows)
allobs=[]
for file in sorted((P/'data').glob('score-*.json')):
 data=json.load(open(file));assert data['count']==len(data['items'])
 for x in data['items']:
  x=x.copy();x['bb']=int(x['satellite_name'].split('-')[-1]);distance=x.get('range_to_sat_km') or x.get('range_to_sat_km_satchecker')
  if x['apparent_mag'] is None or not distance or distance<=0 or x.get('potentially_discrepant'):continue
  x['m1000']=x['apparent_mag']-5*math.log10(distance/1000);allobs.append(x)
pairs=[]
for a,b in itertools.combinations([11,12,13],2):
 candidates=[]
 for x in allobs:
  if x['bb']!=a or x['obs_time_utc']<'2026-09-01':continue
  for y in allobs:
   if y['bb']!=b or x['obs_time_utc'][:10]!=y['obs_time_utc'][:10]:continue
   if any(x.get(k)!=y.get(k) for k in ['obs_orc_id','instrument','obs_filter','obs_lat_deg','obs_long_deg','obs_alt_m']):continue
   if x.get('phase_angle') is None or y.get('phase_angle') is None:continue
   dp=abs(x['phase_angle']-y['phase_angle'])
   if dp<=3:candidates.append((dp,x,y))
 ua=set();ub=set()
 for dp,x,y in sorted(candidates,key=lambda z:z[0]):
  if x['id'] in ua or y['id'] in ub:continue
  ua.add(x['id']);ub.add(y['id']);delta=x['m1000']-y['m1000']
  pairs.append(dict(a=a,b=b,date=x['obs_time_utc'][:10],id_a=x['id'],id_b=y['id'],phase_difference=dp,delta_mag_a_minus_b=delta,flux_a_over_b=10**(-.4*delta),observer_orcids=';'.join(x['obs_orc_id'])))
write('score_matched_launchmates.csv',pairs)
assert len(pairs)==5
assert len({x['id_a'] for x in pairs if x['a']==11})==2
assert math.isclose(next(x['delta_mag_a_minus_b'] for x in pairs if x['a']==11 and x['b']==12),4.026003337414612,abs_tol=1e-8)
summary=[]
for label,ids in [('BB12/13',[100241,100240]),('BB8/9/10',[69589,69590,69591]),('five_controls',[69589,69590,69591,100241,100240])]:
 vals=[new[n]['BSTAR'] for n in ids];summary.append(dict(group=label,n=len(vals),max_over_min=max(vals)/min(vals),bb11_over_mean=target/statistics.mean(vals)))
write('control_agreement.csv',summary)
print('PASS: public GP comparisons and five SCORE pairs reproduced; two unique BB11 optical observations.')
