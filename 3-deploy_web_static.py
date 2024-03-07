#!/usr/bin/python3
"""deploy a packaged web_static archive"""
from fabric.api import put, run, env, local, runs_once
from datetime import datetime
from os.path import exists

env.hosts = ['54.210.126.177', '18.208.120.189']
env.user = 'ubuntu'


@runs_once
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


def deploy():
    """pack and deploy silently"""
    archive = do_pack()
    if not archive:
        return False
    return do_deploy(archive)
