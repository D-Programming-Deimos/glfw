import re

def const_sub(f):
    def replace(matchobj):
        return 'const({type})'.format(**matchobj.groupdict())

    return re.sub(r'const\s(?P<type>\w+)', replace, f)

def unsigned_sub(f):
    return re.sub(r'unsigned\s+', 'u', f)

def uchar_sub(f):
    return re.sub(r'uchar', 'ubyte', f)

def define_sub(f):
    def replace(matchobj):
        return 'enum {name} = {space}{value};'.format(**matchobj.groupdict())

    return re.sub(r'#define (?P<name>\w+)(?P<space>\s+)(?P<value>-?\w+)', replace, f)

def funcptr_sub(f):
    def replace(matchobj):
        groups = matchobj.groupdict()
        groups['arguments'] = groups['arguments'] if not groups['arguments'] == 'void' else ''
        return 'alias {name} = {return} function({arguments});'.format(**groups)

    return re.sub(r'typedef\s(?P<return>\w+)\s\(\*\s?(?P<name>\w+)\)\((?P<arguments>[\w,\,\*,\s]*)\);', replace, f)

def opaque_struct_sub(f):
    def replace(matchobj):
        return 'struct {name};'.format(**matchobj.groupdict())

    return re.sub(r'typedef struct \w+ (?P<name>\w+);', replace, f)

def struct_typedef_sub(f):
    def replace(matchobj):
        return 'struct {name} {{\n{body}\n}}'.format(**matchobj.groupdict())

    return re.sub(r'typedef\sstruct\s+{\s(?P<body>[^}]+)\s}\s(?P<name>\w+);', replace, f, flags=re.MULTILINE)

def functions_sub(f):
    def replace(matchobj):
        groups = matchobj.groupdict()
        groups['arguments'] = groups['arguments'] if not groups['arguments'] == 'void' else ''
        return '{return} {name}({arguments});'.format(**groups)

    return re.sub('GLFWAPI\s(?P<return>(const)?\s?\w+\s?\*{0,2})\s(?P<name>\w+)\((?P<arguments>[\w,\,\*,\s]*)\);', replace, f)

def extern_c_sub(f):
    return re.sub(r'extern "C" {', 'extern(C) {', f)

COMPILER_SPECIFIC_BEGIN = '/* ------------------- BEGIN SYSTEM/COMPILER SPECIFIC -------------------- */'
COMPILER_SPECIFIC_END = '/* -------------------- END SYSTEM/COMPILER SPECIFIC --------------------- */'

def cutout_sections(f):
    sections = f.count(COMPILER_SPECIFIC_BEGIN)
    for _ in range(0, sections):
        p1, p2 =  f.split(COMPILER_SPECIFIC_BEGIN, 1)
        p3, p4 = p2.split(COMPILER_SPECIFIC_END, 1)
        f = p1 + p4

    return f

def preprocessor_removal(f):
    return re.sub(r'(#(ifdef|endif|if|elif|include|define|else)[^\n]*\n)', '', f)

def main():
    import sys

    header = ''
    with open(sys.argv[1], 'r') as in_file:
        header = in_file.read()

    dheader = header
    for func in [cutout_sections, define_sub, unsigned_sub, uchar_sub, funcptr_sub, opaque_struct_sub,
                 struct_typedef_sub, functions_sub, extern_c_sub, const_sub, preprocessor_removal]:
        dheader = func(dheader)

    with open(sys.argv[2], 'w') as out_file:
        out_file.write('module deimos.glfw.glfw3;\n')
        out_file.write(dheader)


if __name__ == '__main__':
    main()