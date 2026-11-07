import sys
import platform

print("Hello,LLM journey")
print("Python 版本:",sys.version.split()[0])
print("操作系统:",platform.system(),platform.release())

numbers = [1,2,3,4,5]
total = sum(numbers)
print(f"1到5的和是{total},平均值是{total/len(numbers)}") 

"""
          git语句的记录
#------1.身份配置------
git config --global user.name "你的GitHub用户名"
git config --global user.email "你的邮箱"
git config --global core.autocrlf true
验证输入是否有误
git config --global --list

#------2.初始化------
git init
#------3.状态查看------
git status
#------4.创建.gitignore文件------
.venv/
__pycache__/
*.pyc
.ipynb_checkpoints/

#------5.创建REAMDE.md------
#------6.加入暂存区------
git add .
git status
→ 文件名变绿,Changes to be committed

add 的意思：把这些改动放进待提交清单，还没真正保存。
#------7.提交------
git commit -m "项目描述"
commit 的意思:拍一张快照存档。a1b2c3d 是快照编号。

#------8.查看历史------
git log --oneline
"""