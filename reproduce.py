"""Clone pinned upstream, record regression before patch, apply, and verify after."""
import json,subprocess,sys,os
from pathlib import Path
ROOT=Path(__file__).resolve().parent
meta=json.loads((ROOT/'upstream.json').read_text());clone=ROOT/'var/upstream';clone.parent.mkdir(exist_ok=True)
if not clone.exists():
 subprocess.run(['git','clone',meta['repository'],str(clone)],check=True)
 subprocess.run(['git','-C',str(clone),'checkout','--detach',meta['commit']],check=True)
if subprocess.check_output(['git','-C',str(clone),'rev-parse','HEAD'],text=True).strip()!=meta['commit']:raise SystemExit('Unexpected upstream revision')
env={**os.environ,'UPSTREAM_ROOT':str(clone)}
if subprocess.check_output(['git','-C',str(clone),'status','--porcelain'],text=True).strip():raise SystemExit('Existing clone is modified; use a fresh var/upstream directory')
def run():return subprocess.run([sys.executable,'-m','pytest','-q',str(ROOT/'tests')],env=env,cwd=ROOT,capture_output=True,text=True)
before=run()
if before.returncode==0:raise SystemExit('Baseline did not reproduce the regression')
subprocess.run(['git','-C',str(clone),'apply',str(ROOT/'patches/validate-cli-regex.patch')],check=True)
after=run();report={'upstream_commit':meta['commit'],'before_exit':before.returncode,'before':before.stdout,'after_exit':after.returncode,'after':after.stdout,'submitted':False}
(ROOT/'reports').mkdir(exist_ok=True);(ROOT/'reports/regression.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ('before','after')},indent=2))
raise SystemExit(after.returncode)
