def ft_ancient_text(file_name: str):
    try:
        file = open(file_name)
        return file.read()
    except Exception as e:
        print(e)
    
    
if __name__ == "__main__":
   print(ft_ancient_text("ancient_fragment.txt"))
    