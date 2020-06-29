prompt="这是一个应用程序，用来记录我们待办事项列表。"
prompt+="\n添加待办事项时，输入'add'，回车，待添加内容。"
prompt+="\n删除待办事项时，输入'delete'，回车,待删除内容。"
prompt+="\n修改待办事项为完成时，输入'change'，回车，待修改内容。"
prompt+="\n如果要终止程序并输出待办，完成事项，输入'quit',回车。"
todo_list=[]
done_list=[]
active=True
print(prompt)
while active:
    message=input()
    if message=='add':
        content=input()
        todo_list.append(content)
    elif message=='delete':
        content=input()
        todo_list.remove(content)
    elif message=='change':
        content=input()
        todo_list.remove(content)
        done_list.append(content)
    elif message=='quit':
        active=False
    else:
        print('输入错误！请检查输入内容或输入格式。')

if todo_list:
    print('待办事项:')
    for todo_thing in todo_list:
        print(todo_thing)
else:
    print('待办事项为空。')
if done_list:
    print('完成事项:')
    for done_thing in done_list:
        print(done_thing)
else:
    print('完成事项为空。')
