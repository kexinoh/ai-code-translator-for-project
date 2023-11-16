# scanconfig.py

languages_import_statements = {
    'python': ['import', 'from'],
    'lua': ['require'],
    'c': ['#include'],
    'cpp': ['#include'],
    'javascript': ['import', 'require'],
    'java': ['import'],
    'rust': ['use', 'extern crate'],
    'php': ['include', 'require', 'require_once', 'include_once'],
    'go': ['import']
}

support_languages={
    "c","cpp","py",""
}