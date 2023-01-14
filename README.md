# Automatically-build-pyd-and-use-it-to-build-executable-files
该脚本能自动使用Cython生成pyd文件并使用Pyinstaller将pyd文件打包成可执行文件；这在某种程度上可以提高程序的运行效率，并且能够防止程序被反编译
# 使用方法
1、直接将需要编译的py源码文件拖到 脚本/程序 上

2、将脚本加入环境变量，在命令行输入 脚本/程序 的名字，后面跟py源码文件
# Ps：
如果源码使用了下列语句

    if __name__ == "__main__":

或者使用了以

    import 或 from

开头的语句但该语句却不是起导入包的作用的时候，脚本生成的程序将无法正常工作
