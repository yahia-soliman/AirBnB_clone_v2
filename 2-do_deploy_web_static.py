#!/usr/bin/python3
"""deploy a packaged web_static archive"""
from fabric.api import env, put, run, local, runs_once
from datetime import datetime
from os.path import exists

env.hosts = ['54.210.126.177', '18.208.120.189']
env.user = 'ubuntu'


@runs_once
def do_pack():
    """pack the files in web_static folder"""
    path = 'versions'
    local('mkdir -p {}'.format(path))
    date = datetime.now().strftime('%Y%m%d%H%M%S')
    path += '/web_static_{}.tgz'.format(date)
    cmd = local('tar -cvzf {} web_static/'.format(path))
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
    run('mkdir -p {}'.format(outdir))
    run('tar -xzf {} --directory {}'.format(path[0], outdir))
    run('rm -rf {}'.format(path[0]))
    run('rm -rf {}'.format(link))
    run('ln -sf {} {}'.format(outdir, link))
    run('mv -n ' + outdir + '/web_static/* ' + outdir)
    print('New version deployed!\n')
    return True
