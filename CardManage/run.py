import os
import json
import time

def add_info():
    os.system("cls")
    already = [s["t_name"] for s in info_table]
    print("添加联系人\n")
    name = input("请输入\n姓名：")
    if name in already:
        print('姓名已存在')
        time.sleep(0.5)
        add_info()
    if (name ==''):
        add_info()
    com_name = input("公司名称：")
    tel_list = input("联系电话(用空格隔开)：")
    remark = input("备注：")
    global dic_templ
    dic_templ = {
        't_name': name,
        't_com_name': com_name,
        't_tel_list': tel_list,
        't_remark': remark
        }
    info_table.append(dic_templ)
    with open('info_table', 'w+', encoding='utf-8') as f:
        json.dump(info_table, f)
    print("添加成功\n"+"="*60+"\n0. 返回主菜单 \n"+"1. 继续添加\n"+"="*60)
    comm = int(input("请输入你要的操作："))
    if(comm == 0):
        run()
    if(comm == 1):
        add_info()
    else:
        run()


def dele_info():
    os.system("cls")
    print("删除联系人\n")
    name = input("请输入姓名：")
    already = [s["t_name"] for s in info_table]
    if name not in already:
        print("姓名不存在\n"+"="*60+"\n0. 返回主菜单 \n"+"1. 继续删除\n"+"="*60)
        comm = input("请输入你要的操作：")
        if(comm == '0'):
            run()
        if(comm == '1'):
            dele_info()
        if(comm==''):
            run()
    else:
        for s in info_table:
            if s["t_name"] == name:
                info_table.remove(s)
                with open('info_table', 'w+', encoding='utf-8') as f:
                    json.dump(info_table, f)
                print("删除成功\n"+"="*60+"\n0. 返回主菜单 \n"+"1. 继续删除\n"+"="*60)
                comm = input("请输入你要的操作：")
                if(comm == '0'):
                    run()
                if(comm == '1'):
                    dele_info()
                if(comm==''):
                    run()
                


def modify_info():
    os.system("cls")
    name = input("请输入要修改的信息姓名：")
    already = [s["t_name"] for s in info_table]
    if name not in already:
        print('需要修改的信息不存在')
        time.sleep(0.5)
        modify_info()
    else:
        for s in info_table:
            if s["t_name"] == name:
                for key, value in s.items():
                    if key == 't_name':
                        print('姓名'+"："+value)
                    if key == 't_com_name':
                        print('公司名称'+"："+value)
                    if key == 't_tel_list':
                        print('联系电话'+"："+value)
                    if key == 't_remark':
                        print('备注'+"："+value)
                comm = input("请选择需要修改的项目(1:姓名，2:公司名称，3:联系电话，4:备注信息，0:退出)")
                chan_info = input("请输入修改内容：")
                if(comm == '1'):
                    s["t_name"] = chan_info
                if(comm == '2'):
                    s["t_com_name"] = chan_info
                if(comm == '3'):
                    s["t_tel_list"] = chan_info
                if(comm == '4'):
                    s["t_remark"] = chan_info
                with open('info_table', 'w+', encoding='utf-8') as f:
                    json.dump(info_table, f)
                print("修改成功\n"+"="*60+"\n0. 返回主菜单 \n"+"1. 继续修改\n"+"="*60)
                flag = input("请输入你要的操作：")
                if(flag == '0'):
                    run()
                if(flag == '1'):
                    modify_info()
                if(comm == '0'):
                    run()
                if(comm == ''):
                    run()
               

def list_info():

    P = 1
    l_count = 0
    lab = " "
    while(True):
        os.system("cls")
        print("     姓名"+" "*9+"公司名称"+" "*9+"联系电话"+" "*9+"备注")
        print("\n")
        for i in info_table[l_count:l_count+10]:            
            print(i["t_name"].center(15,' ')+i["t_com_name"].center(15,' ')+str(i["t_tel_list"]).center(15,' ')+i["t_remark"].center(15,' '))
        print("\n")
        print("=====  ⬅(输入F到上一页)  ==================第"+ str(P) +"页"+str(lab)+"=========================  (输入N到下一页)➡ ====")
        flag=input("输入F或N翻页，按0退出到主菜单：")
        if (flag=='N' or flag=='n'):
            l_count=l_count+10
            P=P+1
            lab=" "
            if (l_count>=len(info_table)):
                l_count=l_count-10
                P=P-1
                lab="（已经到最后一页了）"
        if (flag=='F' or flag=='f'):
            l_count=l_count-10
            P=P-1
            lab=" "
            if (l_count<=-10):
                l_count=l_count+10
                P=P+1
                lab="（已经到第一页了）"
        if (flag=='0'):
            run()
        
            

def serch_info():
    mess=input("请输入想要查找的内容：")
    mess=mess.lower()
    print("\n")
    for s in info_table:
        ls=s
        if mess in str(ls).lower():
            print("姓名："+s["t_name"])
            print("公司名称："+s["t_com_name"])
            print("联系电话："+str(s["t_tel_list"]))
            print("备注："+s["t_remark"])
            print("\n")
    print("查询成功\n"+"="*60+"\n0. 返回主菜单 \n"+"1. 继续查询\n"+"="*60)
    flag =input("请输入你要的操作：")
    if(flag == '0'):
        run()
    if(flag == '1'):
        serch_info()
    if(flag==None):
        serch_info()
    
def run():

    os.system("cls")
    # global info_table
    # with open('info_table', 'w+', encoding='utf-8') as f:
    #     info_table = []
    #     dic_templ = {
    #         't_name': name,
    #         't_com_name': com_name,
    #         't_tel_list': tel_list,
    #         't_remark': remark
    #     }
    #     info_table.append(dic_templ)
    #     json.dump(info_table,f)

    with open('info_table', 'r+', encoding='utf-8') as f:
        data = json.load(f)
        global info_table
        info_table = data
        # print(info_table)
    print("                       名片管理系统")
    print("="*60)
    print("1. 添加名片")
    print("2. 删除名片")
    print("3. 修改名片")
    print("4. 查询名片")
    print("5. 搜索信息")
    print("6. 退出系统")
    print("="*60)

    comm = input("请输入你的操作：")
    if comm == '1':
        add_info()
    if comm == '2':
        dele_info()
    if comm == '3':
        modify_info()
    if comm == '4':
        list_info()
    if comm == '5':
        serch_info()
    if comm == '6':
        print("\n欢迎再次使用！")
        exit()
    else:
        run()





run()
