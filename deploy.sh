#!/usr/bin/env bash
#----------------------------------------------------------
#   Name: deploy.sh
#   Author: xyy15926
#   Created at: 2019-08-31 14:49:27
#   Updated at: 2019-08-31 14:57:44
#   Description:
#----------------------------------------------------------

set -ex

curdir=$(cd $(dirname $0); pwd)
_posts="$curdir/source/_posts"
cd $_posts
git pull
if [ -f README.md ]; then
	rm README.md
fi
cd $curdir
python add_info.py --mv_imgs
hexo generate && hexo deploy
cd $_posts
git checkout .

