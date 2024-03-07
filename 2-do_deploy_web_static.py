#!/usr/bin/python3
"""deploy a packaged web_static archive"""
from fabric.api import put, run, env
from os.path import exists

env.hosts = ['54.210.126.177', '18.208.120.189']


def do_deploy(archive_path):
    """distribute an archive to web servers"""
    if not (archive_path and exists(archive_path)):
        return False
    path = put(archive_path, '/tmp/')
    if path.failed:
        return False
    outdir = '/data/web_static/releases/'
    link = "/data/web_static/current"
    outdir += path[0].split('/')[-1].split('.')[0]
    run(f'mkdir -p {outdir}')
    run(f'tar -xzf {path[0]} --directory {outdir}')
    run(f'rm -rf {path[0]}')
    run(f'rm -rf {link}')
    run(f'ln -sf {outdir} {link}')
    run('mv ' + outdir + '/web_static/* ' + outdir)
    return True
