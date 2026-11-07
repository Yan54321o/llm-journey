import sys
import platform

print("Hello,LLM journey")
print("Python 版本:",sys.version.split()[0])
print("操作系统:",platform.system(),platform.release())

numbers = [1,2,3,4,5]
total = sum(numbers)
print(f"1到5的和是{total},平均值是{total/len(numbers)}") 