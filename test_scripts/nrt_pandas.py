import sys
from memory_profiler import memory_usage
from pathlib import Path
sys.path.append("/home/callum/Documents/data-flow/raw-to-nc/pyglider_pandas")
import shutil
import datetime
import pyglider.seaexplorer as seaexplorer

if __name__ == '__main__':
    rawdir = "/home/callum/Downloads/glider_data/pyglider_improve/sea63_35_nrt/"
    rawncdir = "/home/callum/Downloads/glider_data/pyglider_improve/sea63_35_nrt_pandas/"
    deploymentyaml = "/home/callum/Documents/data-flow/raw-to-nc/deployment-yaml/mission_yaml/SEA63_M35.yml"
    l0tsdir = "/home/callum/Downloads/glider_data/pyglider_improve/sea63_35_nrt_l0_pandas/"
    if Path(rawncdir).exists():
        shutil.rmtree(rawncdir)
    if Path(l0tsdir).exists():
        shutil.rmtree(l0tsdir)
    mem_usage = memory_usage((seaexplorer.raw_to_rawnc, (rawdir, rawncdir, deploymentyaml)))
    print('Maximum memory usage: %s' % max(mem_usage))
    seaexplorer.merge_rawnc(rawncdir, rawncdir, deploymentyaml, kind='sub')
    seaexplorer.raw_to_timeseries(rawncdir, l0tsdir, deploymentyaml, kind='sub')
