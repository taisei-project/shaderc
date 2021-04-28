project('shaderc', 'cpp',
    version : run_command('meson-tools/get-version.py').stdout().strip(),
    meson_version : '>=0.47.0',
    default_options : [
        'cpp_std=gnu++11',
    ]
)

native_options = [
    'b_lto=false',
    'b_ndebug=true',
    'b_sanitize=none',
    'debug=false',
    'optimization=0',
]

glslang_dep = dependency('glslang', fallback : ['glslang', 'glslang_dep'])
spirv_tools_dep = dependency('SPIRV-Tools', fallback : ['SPIRV-Tools', 'spirv_tools_opt_dep'])
spirv_headers_dep = dependency('spirv-headers', fallback : ['SPIRV-Headers', 'spirv_headers_dep'])

glslang_native_dep = dependency('glslang', required : false, native : true, fallback : ['glslang', 'glslang_native_dep'])
spirv_tools_native_dep = dependency('SPIRV-Tools', required : false, native : true, fallback : ['SPIRV-Tools', 'spirv_tools_opt_native_dep'])
spirv_headers_native_dep = dependency('spirv-headers', required : false, native : true, fallback : ['SPIRV-Headers', 'spirv_headers_dep'])

project_args = [
    '-fno-strict-aliasing'
]

if not get_option('enable_nv_exts').disabled()
    project_args += '-DNV_EXTENSIONS'
endif

cxx = meson.get_compiler('cpp')
cxx_native = meson.get_compiler('cpp', native : true)

add_project_arguments(cxx.get_supported_arguments(project_args), language : 'cpp', native : false)
add_project_arguments(cxx_native.get_supported_arguments(project_args), language : 'cpp', native : true)

subdir('libshaderc_util')
subdir('libshaderc')
subdir('glslc')
