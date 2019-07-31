
subdir('src')
subdir('include')

libshaderc = static_library('shaderc',
    shaderc_src,
    dependencies : [shaderc_util_dep, glslang_dep, spirv_tools_dep],
    include_directories : shaderc_incdirs,
    build_by_default : not meson.is_subproject(),
)

shaderc_dep = declare_dependency(
    link_with : libshaderc,
    include_directories : shaderc_incdirs,
)
