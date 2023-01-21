#git

##git的一些命令

+ __cd__ ：更改目录。  
+ __cd..__：退回到上一个目录路径，直接cd则是进入默认目录。  
+ __pwd__：显示当前所在的目录路径。  
+ __ls(ll)__：列出当前目录中的所有文件，只不过ll列出的更加的详细。  
+ __touch__：新建一个文件，eg：touch index,js就会在当前目录下建立一个index,js文件。  
+ __rm__：删除一个文件。  
+ mkdir：新建一个目录，文件夹。
+ rm -r：删除一个文件夹，rm -r src删除src目录。
+ mv 移动文件，mv index.html src index.html 是我们要移动的文件, src 是目标文件夹,当然, 这样写,必须保证文件和目标文件夹在同一目录下。  
+ reset 重新初始化终端/清屏   
+ clear 清屏。  
+ history 查看命令历史。  
+ help 帮助。  
+ exit 退出。  
+ `#表示注释  

#git 的工作区域
* Workspace ：工作区，用于存放项目代码的地方。
* Index/Stage：暂存区，用于临时存放你的改动，事实上他是一个文件，保存即将提交到文件列表信息。
* Repository：仓区（本地仓库），就是在安全存放数据的位置，这里有提交所有数据的版本，HEAD指向最新放入仓库的版本。
* Remote：远程仓库，托管代码的服务器。

#git 的文件状态
+ Untrackde：未跟踪，此文件在文件夹中，都是没有加到git库中，不参与版本控制。
+ Unmodufy：文件以入库，未修改。
+ Modified：文件已修改，但是还没有进行其他操作，可通过`git add`放入暂存区。
+ Staged 暂存状态，执行`git commit`则将修改同步到库中，这时库中的文件和本地文件又变为一致，文件为Unmodify状态，执行`git reset HEAD filename`取消暂存，文件状态为Modified。
