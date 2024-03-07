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
    if run(f'tar -xzf {path[0]} --directory {outdir}').failed:
        return False
    new_name = path[0].split('/')[-1].split('.')[0]
    link = "/data/web_static/current"
    if run(f'rm -rf {outdir + new_name} {path[0]} {link}').failed:
        return False
    if run('mv ' + outdir + '{web_static,' + new_name + '}').failed:
        return False
    return run(f'ln -sf {outdir + new_name} {link}').succeeded
