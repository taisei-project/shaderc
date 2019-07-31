project('shaderc', 'cpp',
    version : run_command('meson-tools/get-version.py').stdout().strip(),
    meson_version : '>=0.47.0',
    default_options : [
        'cpp_std=c++11',
    ]
)

glslang_dep = dependency('glslang', fallback : ['glslang', 'glslang_dep'])
spirv_tools_dep = dependency('SPIRV-Tools', fallback : ['SPIRV-Tools', 'spirv_tools_opt_dep'])

if not get_option('enable_nv_exts').disabled()
    add_project_arguments('-DNV_EXTENSIONS', language : 'cpp')
endif

subdir('libshaderc_util')
subdir('libshaderc')
