#!/usr/bin/python3
"""deploy a packaged web_static archive"""
from fabric.api import put, run, env

env.hosts = ['54.210.126.177', '18.208.120.189']


def do_deploy(archive_path):
    """distribute an archive to web servers"""
    path = put(archive_path, '/tmp/')
    if path.failed:
        return False
    outdir = '/data/web_static/releases/'
    run(f'tar -xzf {path[0]} --directory {outdir}')
    new_name = path[0].split('/')[-1].split('.')[0]
    link = "/data/web_static/current"
    run(f'rm -rf {outdir + new_name} {path[0]} {link}')
    run(f'rm -rf {outdir + new_name} {path[0]} {link}')
    run('mv ' + outdir + '{web_static,' + new_name + '}')
    return run(f'ln -sf {outdir + new_name} {link}').succeeded
