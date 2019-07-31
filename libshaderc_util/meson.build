
subdir('src')
subdir('include')

libshaderc_util = static_library('shaderc_util',
    shaderc_util_src,
    dependencies : [glslang_dep, spirv_tools_dep],
    include_directories : shaderc_util_incdirs,
    build_by_default : false,
)

shaderc_util_dep = declare_dependency(
    link_with : libshaderc_util,
    include_directories : shaderc_util_incdirs,
)
