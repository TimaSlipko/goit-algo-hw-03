import argparse
import shutil
from pathlib import Path

def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Copy and sort dir with contents'
    )
    parser.add_argument(
        'source_dir',
        type=str,
        help='Source dir'
    )
    parser.add_argument(
        'dest_dir',
        type=str,
        nargs='?',
        default='dist',
        help='Destination dir'
    )
    
    return parser.parse_args()

def copy_files_recursively(source_path, dest_path):
    try:
        if not source_path.exists():
            print(f"dir '{source_path}' does not exist")
            return
        
        if not source_path.is_dir():
            print(f"'{source_path}' is not dir")
            return
        
        dest_path.mkdir(parents=True, exist_ok=True)
        
        for item in source_path.iterdir():
            try:
                if item.is_dir():
                    copy_files_recursively(item, dest_path)
                    
                elif item.is_file():
                    copy_file(item, dest_path)
                    
            except PermissionError:
                print(f"permission error for '{item}'")
            except Exception as e:
                print(f"error '{item}': {e}")
                
    except PermissionError:
        print(f"permission error for '{source_path}'")
    except Exception as e:
        print(f"error for '{source_path}': {e}")


def copy_file(file_path, dest_path):
    try:
        file_extension = file_path.suffix.lstrip('.').lower()
        
        if not file_extension:
            file_extension = 'no_extension'
        
        extension_dir = dest_path / file_extension
        extension_dir.mkdir(parents=True, exist_ok=True)
        
        destination_file = extension_dir / file_path.name
        
        if destination_file.exists():
            base_name = file_path.stem
            counter = 1
            while destination_file.exists():
                new_name = f"{base_name}_{counter}{file_path.suffix}"
                destination_file = extension_dir / new_name
                counter += 1
        
        shutil.copy2(file_path, destination_file)
        
    except PermissionError:
        print(f"permission error for '{file_path}'")
    except Exception as e:
        print(f"error for '{file_path}': {e}")

def main():
    args = parse_arguments()
    
    source_path = Path(args.source_dir)
    dest_path = Path(args.dest_dir)
        
    copy_files_recursively(source_path, dest_path)
    
    print("done")

if __name__ == "__main__":
    main()