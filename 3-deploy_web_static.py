#!/usr/bin/python3
"""deploy a packaged web_static archive"""
from fabric.api import put, run, env, local
from datetime import datetime

env.hosts = ['54.210.126.177', '18.208.120.189']
env.user = 'ubuntu'


def do_pack():
    """pack the files in web_static folder"""
    path = 'versions'
    local(f'mkdir -p {path}')
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    path += f'/web_static_{date}.tgz'
    cmd = local(f'tar -cvzf {path} web_static/')
    return path if cmd.succeeded else None


def do_deploy(archive_path):
    """distribute an archive to web servers"""
    path = put(archive_path, '/tmp/')
    if path.failed:
        return False
    outdir = '/data/web_static/releases/'
    new_name = path[0].split('/')[-1].split('.')[0]
    link = "/data/web_static/current"
    if run(f'tar -xzf {path[0]} --directory {outdir}').failed:
        return False
    if run(f'rm -rf {outdir + new_name} {path[0]} {link}').failed:
        return False
    if run('mv ' + outdir + '{web_static,' + new_name + '}').failed:
        return False
    return run(f'ln -sf {outdir + new_name} {link}').succeeded


def deploy():
    """pack and deploy silently"""
    archive = do_pack()
    if not archive:
        return False
    return do_deploy(archive)
