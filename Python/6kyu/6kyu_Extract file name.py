class FileNameExtractor:
    def extract_file_name(dirty_file_name):
        import re
        match = re.match(r'^([0-9]+[_])?([A-Za-z_-]+\.[a-zA-Z0-9_-]+)', dirty_file_name)
        if match:
            return match.groups()[1]