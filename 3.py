# 读取 setitems.txt 文件
with open('C:\\Users\\TPY\\Desktop\\set\\set\\setitems.txt', 'r') as f:
    lines = f.readlines()

# 初始化变量
current_prefix = ""
current_group = []

# 打开 setitem2.txt 文件准备写入
with open('setitem2.txt', 'w') as f:
    for line in lines:
        # 获取行的前两个字母
        prefix = line[:2]
        
        # 如果当前组为空或前两个字母与当前组的前两个字母相同，则加入当前组
        if not current_group or prefix == current_prefix:
            current_group.append(line)
            current_prefix = prefix
        else:
            # 如果当前组的长度大于等于3，则写入文件并加入空行
            if len(current_group) >= 3:
                f.writelines(current_group)
                f.write('\n')
            
            # 重置当前组和前缀
            current_group = [line]
            current_prefix = prefix
    
    # 检查最后一组是否满足条件
    if len(current_group) >= 3:
        f.writelines(current_group)
        f.write('\n')