import subprocess

def execute_command(./sing-box run):
    try:
        # 执行命令并获取输出
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # 打印标准输出
        print("输出：", result.stdout)
    except subprocess.CalledProcessError as e:
        # 打印错误信息
        print("错误：", e.stderr)

if __name__ == "__main__":
    # 在这里输入你想要执行的命令
    command = "ls -l"  # 例如，列出当前目录的文件
    execute_command(command)
