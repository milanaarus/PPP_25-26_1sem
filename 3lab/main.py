import os

def travell_directory(path):
    way = {}
    try:
        items = os.listdir(path)
    except PermissionError:
        print(f'Нет доступа к директории: {path}')
        return way

    for item in items:
        full_way = os.path.join(path, item)
        
        if os.path.isdir(full_way):
            way[item] = travell_directory(full_way)
        else:
            way[item] = None  
    
    return way


if __name__ == "__main__":
    directory_path = 'путь/к/директории'
    result = travell_directory(directory_path)
    print(result)
