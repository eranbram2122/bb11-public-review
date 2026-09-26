"""Public SCORE finite-control sampling; Python standard library only."""
from pathlib import Path
import csv,json,random,statistics,itertools
P=Path(__file__).resolve().parent
r=list(csv.DictReader(open(P/'data/score_historical_control_passes.csv')));pool={}
for x in r:
 a,b=int(x['a']),int(x['b']);v=float(x['median'])
 pool.setdefault((a,b),{}).setdefault(x['date'],[]).append(v)
 pool.setdefault((b,a),{}).setdefault(x['date'],[]).append(-v)
threshold=3.485107871532107;floor=3.1627276253162426;distributions=[];allrows=[]
for (a,b),dates in sorted(pool.items()):
 if len(dates)<3:continue
 vals={k:statistics.median(v) for k,v in dates.items()};cases=[]
 for days in itertools.combinations(sorted(vals),3):
  y=[vals[k] for k in days];median=statistics.median(y);minimum=min(y);row={'target':a,'comparator':b,'dates':'|'.join(days),'median':median,'minimum':minimum,'matches':median>=threshold and minimum>=floor};cases.append(row);allrows.append(row)
 distributions.append(cases)
rng=random.Random(20260926);hits=0;N=100000
for _ in range(N):hits+=rng.choice(rng.choice(distributions))['matches']
result={'source':'historical SCORE control pass summaries','mc_draws':N,'eligible_ordered_pairs':len(distributions),'exact_cases':len(allrows),'mc_hits':hits,'exact_hits':sum(x['matches'] for x in allrows),'maximum_three_date_median':max(x['median'] for x in allrows),'interpretation':'finite observed-control resampling only; zero hits is not a population p-value or deployment probability','input_note':'pass-level public SCORE derived summaries inherited from prior analysis; selected original raw SCORE responses also included'}
assert len(allrows)==80 and result['exact_hits']==0
(P/'results/public_score_monte_carlo.json').write_text(json.dumps(result,indent=2)+'\n')
with (P/'results/public_score_exact_subsets.csv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=list(allrows[0]));w.writeheader();w.writerows(allrows)
print(json.dumps(result,indent=2))
