#!/usr/bin/env shell
#----------------------------------------------------------
#   Name: automake.sh
#   Author: xyy15926
#   Created at: 2019-08-02 23:10:24
#   Updated at: 2019-08-02 23:13:15
#   Description:
#----------------------------------------------------------

npm uninstall hexo-renderer-marked --save
npm install hexo-generator-feed hexo-generator-searchdb \
	hexo-renderer-pandoc hexo-deployer-git

